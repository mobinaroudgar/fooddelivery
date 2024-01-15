from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, ForeignKey


class Address(Base):
    __tablename__ = "address_tbl"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    region = Column(String(30))
    unit_number = Column(Integer)
    No = Column(Integer)
    Street = Column(String(30))
    Alley = Column(String(30))
    address = Column(String(300))

    customer_address = relationship("Customer", back_populates="addresses")
    order_address = relationship("FoodOrder", back_populates="address")

    def __init__(self, customer_address, region, unit, No, Street, Alley, address):
        self.customer_address = customer_address
        self.region = region
        self.unit_number = unit
        self.No = No
        self.Street = Street
        self.Alley = Alley
        self.address = address
