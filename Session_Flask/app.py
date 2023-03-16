from flask import Flask, request

app = Flask(__name__)  

stores = [
    {
        "name": "My Store",
        "items": 
        {
            "name": "Chair",
            "price": 94
        }
    }
]

@app.route("/store")
def get_stores():
    return {"stores": stores}


# created a end point where we have to deal the post and get request
@app.post("/store")
def create_store():
    #using request method from the flask to get the request from the url
    request_data = request.get_json()
    # creating a new store data for the previous store data 
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store) # Append it
    return new_store, 201 # Return need to be compulsory


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

