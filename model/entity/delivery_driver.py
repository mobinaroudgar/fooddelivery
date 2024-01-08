'''

from model.entity import Base
from sqlalchemy import Integer, String, Column, Boolean, Float, Date, DateTime, ForeignKey


class DeliveryDriver(Base):
    __tablename__ = "delivery_driver_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    family = Column(String(40))

    def __init__(self, name, family):
        self.name = name
        self.family = family
'''