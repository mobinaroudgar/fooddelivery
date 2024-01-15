from sqlalchemy.orm import relationship

from model.entity import Base
from sqlalchemy import Integer, String, Column, Boolean, Float, Date, DateTime, ForeignKey

class DeliveryDriver(Base):
    __tablename__ = "delivery_driver_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    family = Column(String(40))

    foodorder=relationship("FoodOrder")

    def __init__(self, name, family):
        self.name = name
        self.family = family
