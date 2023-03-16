from .BaseRoute import getNewRoute
from ..services.Shops import ShopsService

routes = getNewRoute('items')
routes.add_url_rule('/',view_func=ShopsService.as_view('shops'), methods=['get','post'])



