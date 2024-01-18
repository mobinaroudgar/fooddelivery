from sqlalchemy.orm import relationship

# from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, Float, ForeignKey, ColumnDefault, Nullable

from model.entity import Base


class Menu(Base):
    __tablename__ = "menu_item_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
  #  item_id = Column(Integer, ForeignKey("menu_item_tbl.id"), ColumnDefault("None"))
    price = Column(Float)

    # order_menu = relationship("OrderMenuItem", back_populates="menu_item")
    # item_name = relationship("Menu", back_populates="item")
    item = relationship("Menu", backref="name", remote_side=[id])

    def __init__(self, name, item_id, price):
        self.name = name
        self.item_id = item_id
        self.price = price
