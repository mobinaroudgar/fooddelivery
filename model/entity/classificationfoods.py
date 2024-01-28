from sqlalchemy.orm import relationship

# from model.entity import *
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, Float, ForeignKey, ColumnDefault, Nullable

from model.entity import Base


class Classification(Base):
    __tablename__ = "classification_food_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))

    foods = relationship("Menu", back_populates="classification")

    def __init__(self, name):
        self.name = name
