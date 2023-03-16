from flask import Blueprint
from . import ShopRoute, ItemRoute




def init_app(app):
    app.register_blueprint(ShopRoute.routes)
    app.register_blueprint(ItemRoute.routes)
    
    
    return app