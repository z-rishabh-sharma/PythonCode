from flask.views import MethodView
from ..models.All import db
from flask import request # catch all the data of the request(type, data and all)
from ..Common import get_shop
import json

class ShopsService(MethodView):
    
    def __init__(self):
        self.id = None
    
    def get(self, *args, **kwargs):
        result = get_shop()
        result = {"success":True, "result":result}
        return result

    
    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = get_shop(params["id"])
        if(result==None):
            return {"success":False, "result": "Not found!"}
        return result
