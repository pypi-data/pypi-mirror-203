from bson.objectid import ObjectId
from aliendev_api.config import mongo

def _case(param: str):
    splitter = param.lower().replace(" ", "-")
    return splitter


method_name = ["GET", "POST", "PUT", "DELETE"]


class ApiGateway:
    def __init__(self, username, title) -> None:
        self.username = username
        self.title = title
        self.stack_name = _case(title)
        self.endpoint = []

    def addMethod(self, method, prefix):
        if method in method_name:
            endpoint = {
                "method": method,
                "prefix": prefix
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
            finder = db['gateway'].find_one({"$and":[{"username":self.username},{"stack_name":self.stack_name}]})
            if finder:
                newvalues = { "$set": { "endpoint": self.endpoint } }
                db['gateway'].update_one({"_id":finder['_id']},newvalues)
            else:
                db['gateway'].insert_one(result_data)
                
        return result_data
