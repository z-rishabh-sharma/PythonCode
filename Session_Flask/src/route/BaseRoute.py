from flask import Blueprint
# import os
# # import dotenv
# from dotenv import load_dotenv

# ROOT_DIR = os.path.join(os.path.dirname(__file__), "../..")
# print("ROOT_DIR :",ROOT_DIR)
# DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")
# # print(DOT_ENV_PATH)
# load_dotenv(DOT_ENV_PATH) # this goes into memory
# print(os.getenv('DATABASE'))

def getNewRoute(name):
    return Blueprint(name,__name__, url_prefix='/'+name)


def check():
    return "Welcome to the app base!"

routes = Blueprint("base", __name__, url_prefix='/')
routes.add_url_rule('/', view_func=check) # this means whenever we come to / we will invoke it

