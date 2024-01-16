from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, ForeignKey, PrimaryKeyConstraint


class OrderMenuItem(Base):
    __tablename__ = "order_menu_item"

    # id = Column(Integer, primary_key=True)
    food_order_id = Column(Integer, ForeignKey("food_order_tbl.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_item_tbl.id"))
    __table_args__ = (PrimaryKeyConstraint(food_order_id, menu_item_id), {})
    quantity_ordered = Column(Integer)

    food_order = relationship("FoodOrder", back_populates="order_item")
    menu_item = relationship("Menu", back_populates="order_menu")

    def __init__(self, food_order, menu_item, quantity_ordered):
        self.food_order = food_order
        self.menu_item = menu_item
        self.quantity_ordered = quantity_ordered
