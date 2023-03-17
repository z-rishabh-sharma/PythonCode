from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from . import db
# import os

# val = os.getenv("APP_SETTINGS")
# print(val)
base = db.Model
metadata = base.metadata

class Shops(base):
    __tablename__ = "shops"
    id = Column(INTEGER(20),primary_key = True)
    name = Column(String(45))
    description = Column(String(100))
    
    # Creation of foreign key
    # item_id = Column(ForeignKey("Items.id"), index = True)
    # def __dict__(self):
    #     result = {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #         "item_id":self.item_id
    #     }
    #     return result
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}


class Items(base):
    __tablename__ = "items"
    id = Column(INTEGER(20),primary_key = True)
    name = Column(String(45))
    description = Column(String(100))
    # def __dict__(self):
    #     result = {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description
    #     }
    #     return result
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
# Creation of Stocks 
class Stocks(base):
    __tablename__ = "stocks"
    id = Column(INTEGER(20),primary_key = True)
    item_id = Column(String(45))
    shop_id = Column(String(100))
    unit_count = Column(INTEGER(50))
    unit_price = Column(INTEGER(50))
    
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # QUERY OF TAbLE
# CREATE TABLE items(     
# item_id INT(20) PRIMARY KEY NOT NULL,
# item_name VARCHAR(50) NOT NULL,
# item_description VARCHAR(100) NOT NULL);

# CREATE TABLE shops(
# shop_id INT(20) PRIMARY KEY NOT NULL,
# shop_name VARCHAR(50) NOT NULL,
# shop_description VARCHAR(100) NOT NULL,
# item_id INT(20)
# );

# create table stocks( 
# id INT(20) Primary key not null AUTO_INCREMENT, 
# item_id INT(20), 
# foreign key (item_id) references items(item_id), 
# shop_id INT(20), 
# Foreign key (shop_id) references shops(shop_id), 
# unit_count INT(50), 
# unit_price float(50)
# );