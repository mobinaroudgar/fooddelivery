from sqlalchemy.orm import relationship

from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, Float


class Menu(Base):
    __tablename__ = "menu_item_tbl"

    id = Column(Integer, primary_key=True)
    item_name = Column(String(45))
    price = Column(Float)

    order_menu = relationship("OrderMenuItem", back_populates="menu_item")

    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
