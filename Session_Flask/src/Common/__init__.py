from ..models.All import Shops, Items


def get_shop(id=None):
    if id==None:
        # this will give the particular row
        # result = Shops.query.filterby(id=id).as_dict()
        # result = Shops.query.filterby(id=id).as_dict()
        result = [s.as_dict() for s in Shops.query.all()]
        return result
    
    # Print all the row present in shops table
    # result = [s.as_dict() for s in Shops.query.all()]
    return [s.as_dict() for s in Shops.query.filter(Shops.id == id)]
    

def get_items(id=None):
    if id==None:
        # this will give the particular row
        result = [s.as_dict() for s in Items.query.all()]
        return result
    
    # Print all the row present in shops table
    return [s.as_dict() for s in Items.query.filter(Items.id == id)]


# here we have to define all the functionality that will reflect it
#---------------------------------------------------------------------------

# def get_shops_items(id=None):
#     if id==None:
#         result = [s.as_dict() for s in Shops.query.all()]
#         return result
    
#     return [s.as_dict() for s in Items.query.filter(Items.id == id)]


# def get_items_shops(id=None):
#     if id==None:
#         result = [s.as_dict() for s in Items.query.all()]
#         return result
    
#     return [s.as_dict() for s in Shops.query.filter(Shops.id == id)]
    
#---------------------------------------------------------------------------

