from sqlalchemy.orm import relationship
from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, ForeignKey


class Address(Base):
    __tablename__ = "address_tbl"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    address = Column(String(300))

    customer_address = relationship("Customer", back_populates="addresses")

    def __init__(self, customer_address, address):
        self.customer_address = customer_address
        self.address = address
