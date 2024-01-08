from datetime import datetime
from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Float, Date, DateTime, ForeignKey
from model.entity import *


class FoodOrder(Base):
    __tablename__ = "food_order_tbl"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    status = Column(Boolean)
    date_time = Column(DateTime, default=datetime)
    total_amount = Column(Float)

    customer = relationship("Customer", back_populates="orders")
    order_item = relationship("OrderMenuItem", back_populates="food_order")

    def __init__(self, customer, status, date_time, total_amount):
        self.customer = customer
        self.status = status
        self.date_time = date_time
        self.total_amount = total_amount

