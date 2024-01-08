from model.da.database import *
from model.entity import *


class CustomerDa(DataBaseManager):
    def find_by_email_password(self, email, password):
        self.make_engine()
        result = self.session.query(Customer).filter(
            and_(Customer.email == email, Customer.password == password)).all()
        if result:
            return result[0]

    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(Customer).filter(Customer.email == email).all()
        if result:
            return result[0]
