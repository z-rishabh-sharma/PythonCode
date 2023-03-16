# database definition

# table shops and items (Datbase name "inventory", u = "root")
# here we are includiong those thing that will going to be same in the dev and prod
import os

ROOT_DIR = os.path.join(os.path.dirname(__file__), "../")

class Base_Config(object):
    
    
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
        
        return conString
    
    SQLALCHEMY_DATABASE_URI = getDBConnectionString()