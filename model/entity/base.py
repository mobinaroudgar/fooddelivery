from sqlalchemy.orm import DeclarativeBase
import json

class Base(DeclarativeBase):
    def to_json(self):
        return json.dumps({c.name: getattr(self, c.name) for c in self.__table__.columns})

    def __repr__(self):
        return str(self.__dict__)