from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(40), unique=True)
    password = Column(String(40))
    address = Column(String(300))

    orders = relationship("FoodOrder", back_populates="customer")

    def __init__(self, first_name, last_name, email, password, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address
