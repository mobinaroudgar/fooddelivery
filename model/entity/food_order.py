from datetime import datetime
from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Float, Date, DateTime, ForeignKey
from model.entity import *


class FoodOrder(Base):
    __tablename__ = "food_order_tbl"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    customer_address_id = Column(Integer, ForeignKey("address_tbl.id"))
    delivery_driver_id = Column(Integer, ForeignKey("delivery_driver_tbl.id"))
    status = Column(Boolean)
    date_time = Column(DateTime, default=datetime)
    delivery_fee = Column(Float)
    cust_driver = Column(Float)
    total_amount = Column(Float)

    customer = relationship("Customer", back_populates="orders")
    order_item = relationship("OrderMenuItem", back_populates="food_order")
    address = relationship("Address", back_populates="order_address")
    delivery = relationship("DeliveryDriver", back_populates="foodorder")

    def __init__(self, customer, address, delivery, status, date_time, delivery_fee, cust_driver, total_amount):
        self.customer = customer
        self.address = address
        self.delivery = delivery
        self.status = status
        self.date_time = date_time
        self.delivery_fee = delivery_fee
        self.cust_driver = cust_driver
        self.total_amount = total_amount
