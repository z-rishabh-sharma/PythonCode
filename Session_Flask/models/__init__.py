from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# sql ORM (Object Relational Mapper)will create the object of query(SQLALCEMY)


db = SQLAlchemy() # calling the sqlalchemy instance create

def init_app(app):
    db.init_app(app)
    # migrate = Migrate(app, db)
    return app
