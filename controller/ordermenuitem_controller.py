from controller import *
from model.da import *
from model.entity import *


class OrderMenuItemController:
    @classmethod
    def save(cls, food_order_id, menu_item_id, quantity_ordered):
        try:
            da = OrderMenuDa()
            food_orderr = FoodOrderController.find_by_id(food_order_id)[0]
            menu_itemm = MenuController.find_by_id(menu_item_id)[1]
            # print(da.find_by_food_order_id(food_order_id), (da.find_by_menu_item_id(food_order_id)))
            if not (da.find_by_food_order_id(food_order_id) and (da.find_by_menu_item_id(menu_item_id))):
                 ordermenuitem = OrderMenuItem(food_orderr, menu_itemm, quantity_ordered)
                 da.save(ordermenuitem)
                 return True, ordermenuitem
            else:
                raise DuplicateNameError("DuplicateNameError")
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, food_order_id, menu_item_id, quantity_ordered):
        try:
            da = OrderMenuDa()
            food_order = FoodOrderController.find_by_id(food_order_id)[0]
            menu_item = MenuController.find_by_id(menu_item_id)[1]
            ordermenuitem = OrderMenuItem(food_order, menu_item, quantity_ordered)
            ordermenuitem.id = id
            da.edit(ordermenuitem)
            return True, ordermenuitem
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_food_order_id(OrderMenuItem, id)
            return True, da.remove(ordermenuitem)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = OrderMenuDa()
            return True, da.find_all(OrderMenuItem)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_id(OrderMenuItem, id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no item!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_menu_item_id(cls, menu_item_id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_menu_item_id(menu_item_id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no item!")
        except  Exception as e:
            return False, str(e)

    @classmethod
    def find_by_food_order_id(cls, food_order_id):
        try:
            da = OrderMenuDa()
            ordermenuitem = da.find_by_food_order_id(food_order_id)
            if OrderMenuDa:
                return True, ordermenuitem
            else:
                raise NoContentError("There is no food order!")
        except Exception as e:
            return False, str(e)
