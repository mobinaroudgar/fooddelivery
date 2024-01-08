from model.entity import *
from model.da.database import DataBaseManager, and_


class FoodOrderDa(DataBaseManager):
    def find_by_customer_id(self, customer_id):
        self.make_engine()
        result = self.session.query(FoodOrder).filter(FoodOrder.customer_id == customer_id).all()
        self.session.close()
        return result

    def find_by_customer_email(self, customer_email):
        self.make_engine()
        result = self.session.query(FoodOrder).filter(FoodOrder.customer.email == customer_email).all()
        self.session.close()
        return result

    def find_by_datetime(self, date_time):
        self.make_engine()
        result = self.session.query(FoodOrder).filter(FoodOrder.date_time == date_time).all()
        self.session.close()
        return result

    def find_by_order_item(self, order_item):
        self.make_engine()
        result = self.session.query(FoodOrder).filter(FoodOrder.order_item == order_item).all()
        self.session.close()
        return result
