from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv
from models.All import Shops,Items
import os
import json

ROOT_DIR = os.path.join(os.path.dirname(__file__), "./")
DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")
# print(DOT_ENV_PATH)
load_dotenv(DOT_ENV_PATH) # this goes into memory


def getDBConnectionString():
    # mysql has connection string by default
        
    config = {}
    config["username"] = os.getenv("DB_USERNAME")
    config["password"] = os.getenv("DB_PASSWORD")
    config["host"] = os.getenv("DB_HOST")
    config["database"] = os.getenv("DATABASE")
    config["app_setting"] = os.getenv("APP_SETTING")
    config["port"] = os.getenv("DB_PORT")
        
    conString = f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    # print(conString)
    return conString

engine = create_engine(getDBConnectionString())

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    items =Items(id=1, name="XYX", description="This is a description")
    db_session.add(items)
    shop = Shops(id=1, name="General", description="this is a description")
    db_session.add(shop)
    db_session.commit()