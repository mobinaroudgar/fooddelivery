from model.da.database import DataBaseManager
from model.entity import *


class OrderMenuDa(DataBaseManager):
    def find_by_food_order_id(self, food_order_id):
        self.make_engine()
        result = self.session.query(OrderMenuItem).filter(OrderMenuItem.food_order_id == food_order_id).all()
        self.session.close()
        return result

    def find_by_menu_item_id(self, menu_item_id):
        self.make_engine()
        result = self.session.query(OrderMenuItem).filter(OrderMenuItem.menu_item_id == menu_item_id).all()
        self.session.close()
        return result

    def find_by_quantity(self, quantity):
        self.make_engine()
        result = self.session.query(OrderMenuItem).filter(OrderMenuItem.quantity_ordered == quantity).all()
        self.session.close()
        return result


