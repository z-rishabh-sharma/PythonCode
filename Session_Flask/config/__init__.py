import os
# import dotenv
from dotenv import load_dotenv

from .dev_config import DevelopmentConfig
from .prod_config import ProductionConfig

# tell the root directory to tell the path
# we have to back off the current folder and come in the root directory to give a direction
ROOT_DIR = os.path.join(os.path.dirname(__file__), "../")
DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")
# print(DOT_ENV_PATH)
load_dotenv(DOT_ENV_PATH) # this goes into memory


# this variable goes inside the function
# configs = os.getenv('DEBUG') # now we are fetching it from the memory

config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}


def init_app(app):
    # app.configs["debug"] = configs
    # return app
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(config[app_settings])
    return app
    # pass