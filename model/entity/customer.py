from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime


class Customer(Base):
    __tablename__ = "customer_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    phone_number = Column(String(30), unique=True)
    email = Column(String(40), unique=True)
    password = Column(String(40))

    #orders = relationship("FoodOrder", back_populates="customer")
    addresses = relationship("Address", back_populates="customer_address")

    def __init__(self, name, family, phone_number, email, password):
        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.email = email
        self.password = password
