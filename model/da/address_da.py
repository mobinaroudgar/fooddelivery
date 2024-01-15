'''from model.entity import *
from model.da.database import DataBaseManager, and_
'''

'''class AddressDa(DataBaseManager):

    def find_by_customer_id(self, customer_id):
        self.make_engine()
        result = self.session.query(Address).filter(Address.customer_id == customer_id).all()
        self.session.close()
        return result

    def find_by_customer_email(self, customer_email):
        self.make_engine()
        result = self.session.query(Address).filter(Address.customer_address.email == customer_email).all()
        self.session.close()
        return result

    def find_by_customer_phone_number(self, customer_email):
        self.make_engine()
        result = self.session.query(Address).filter(Address.customer_address.email == customer_email).all()
        self.session.close()
        return result

    def find_by_address(self, address):
        self.make_engine()
        result = self.session.query(Address).filter(Address.address == address).all()
        self.session.close()
        return result
'''