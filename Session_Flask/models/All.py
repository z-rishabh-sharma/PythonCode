from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from . import db

base = db.Model
metadata = base.metadata

class Shops(base):
    __tablename__ = "Shops"
    id = Column(INTEGER(20),primary_key = True)
    name = Column(String(45))
    description = Column(String(100))
    
    # Creation of foreign key
    item_id = Column(ForeignKey("Items.id"), index = True)


class Items(base):
    __tablename__ = "Items"
    id = Column(INTEGER(20),primary_key = True)
    name = Column(String(45))
    description = Column(String(100))
    
    