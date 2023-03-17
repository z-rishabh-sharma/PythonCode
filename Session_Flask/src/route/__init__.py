from flask import Blueprint
from . import ShopRoute, ItemRoute, BaseRoute




def init_app(app):
    app.register_blueprint(BaseRoute.routes)
    app.register_blueprint(ShopRoute.routes)
    app.register_blueprint(ItemRoute.routes)
    
    
    return app