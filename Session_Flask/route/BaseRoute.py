from flask import Blueprint

def getNewRoute(__name__):
    return Blueprint(__name__, url_prefix='/name')


def check():
    return "Welcome to the app base!"

routes = Blueprint("base", __name__, url_prefix='/')
routes.add_url_rule('/', view_function=check) # this means whenever we come to / we will invoke it

