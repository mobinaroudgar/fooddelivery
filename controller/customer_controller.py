from controller import *
from model.da import *
from model.entity import *


class CustomerController:
    @classmethod
    def save(cls, name, family, email, password):
        try:
            da = CustomerDa()
            if not da.find_by_email(email):
                customer = Customer(name, family, email, password)
                da.save(customer)
                return True, customer
            else:
                raise DuplicateEmailError("Duplicate email")
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, first_name, last_name, password, email):
        try:
            da = CustomerDa()
            customer = Customer(first_name, last_name, email, password)
            customer.id = id
            da.edit(customer)
            return True, customer
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = CustomerDa()
            customer = da.find_by_id(Customer, id)
            return True, da.remove(customer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CustomerDa()
            return True, da.find_all(Customer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = CustomerDa()
            customer = da.find_by_id(Customer, id)
            if customer:
                return True,customer
            else:
                raise NoContentError("There is no Customer!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_email(cls, email):
        try:
            da = CustomerDa()
            return True, da.find_by_email(email)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, email, password):
        try:
            da = CustomerDa()
            customer = da.find_by_email_password(email, password)
            if (customer):
                return True, customer
            else:
                raise AccessDeniedError("wrong email/password")
        except Exception as e:
            return False, str(e)
