from ..models.All import Shops, Items


def get_shop(id=None):
    if id!=None:
        # this will give the particular row
        return Shops.query.filterby(id=id)
    
    # Print all the row present in shops table
    return Shops.objects.all()

def get_items(id=None):
    if id!=None:
        return Items.query.filterby(id=id)
    
    return Items.objects.all()