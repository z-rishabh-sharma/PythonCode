# from flask import Flask, request

# app = Flask(__name__)  

# stores = [
#     {
#         "name": "My Store",
#         "items": 
#         {
#             "name": "Chair",
#             "price": 94
#         }
#     }
# ]

# @app.route("/store")
# def get_stores():
#     return {"stores": stores}


# # created a end point where we have to deal the post and get request
# @app.post("/store")
# def create_store():
#     #using request method from the flask to get the request from the url
#     request_data = request.get_json()
#     # creating a new store data for the previous store data 
#     new_store = {"name": request_data["name"], "items": []}
#     stores.append(new_store) # Append it
#     return new_store, 201 # Return need to be compulsory


# @app.post("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store["name"] == name:
#             new_item = {"name": request_data["name"], "price": request_data["price"]}
#             store["items"].append(new_item)
#             return new_item, 201
#     return {"message": "Store not found"}, 404

from . import route, config, models, services
from flask import Flask
from flask_cors import CORS # cross origin resouce sharing


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Now we will go through from each modules and add there functionality
    
    app = config.init_app(app)
    app = models.init_app(app)
    app = route.init_app(app)
    app = services.init_app(app)
    
    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0")
        