from model.da.database import DataBaseManager
from model.entity import *


class MenuitemDa(DataBaseManager):
    def find_by_item_name(self, item_name):
        self.make_engine()
        menuitem_list = self.session.query(Menu).filter(Menu.item_name.like(f"%{item_name}%")).all()
        self.session.close()
        return menuitem_list

    def find_by_order_menu(self, order_menu):
        self.make_engine()
        menuitem_list = self.session.query(Menu).filter(Menu.order_menu == order_menu).all()
        self.session.close()
        return menuitem_list

