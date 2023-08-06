from bson.objectid import ObjectId
from aliendev_api.config import mongo
from pydantic import BaseModel, Field
from enum import Enum

def _case(param: str):
    splitter = param.lower().replace(" ", "-")
    return splitter


method_name = ["GET", "POST", "PUT", "DELETE"]

class ParamType(Enum):
    param = 'Param'
    body = 'Body'

class ParamData(BaseModel):
    key: str = Field(..., example="name")
    data_type: str = Field(..., example="string|int|any")
    required: bool


class ApiGateway:
    def __init__(self, username, title) -> None:
        self.username = username
        self.title = title
        self.stack_name = _case(title)
        self.endpoint = []

    def addMethod(self, method, prefix, param_type:ParamType, data:ParamData):
        """
        Args:
            method (string): "GET|POST|PUT|DELETE"
            prefix (string): "/test-get"
            param_type (ParamType): "param|body"
            data (ParamData): [
                        {
                        "key": "name",
                        "data_type": "string",
                        "required": true
                        },
                        {
                        "key": "age",
                        "data_type": "int",
                        "required": false
                        }
                    ]
        """
        if method in method_name:
            endpoint = {
                "method": method,
                "prefix": prefix,
                "param_type":param_type,
                "data":data
            }
            self.endpoint.append(endpoint)

    def build(self):
        objId = ObjectId()
        result_data = {
            "_id": str(objId),
            "username": self.username,
            "title": self.title,
            "stack_name": self.stack_name,
            "endpoint": self.endpoint
        }
        client, db = mongo.connect()
        with client:
            finder = db['gateway'].find_one(
                {"$and": [{"username": self.username}, {"stack_name": self.stack_name}]})
            if finder:
                newvalues = {"$set": {"endpoint": self.endpoint}}
                db['gateway'].update_one({"_id": finder['_id']}, newvalues)
            else:
                db['gateway'].insert_one(result_data)

        return result_data
