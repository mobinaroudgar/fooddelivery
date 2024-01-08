from controller import *
from model.da import *
from model.entity import *


class FoodOrderController:
    @classmethod
    def save(cls, customer_id, status, date_time, total_amount):
        try:
            da = FoodOrderDa()
            customer = CustomerController.find_by_id(customer_id)[1]
           # print(da.find_by_customer_id(customer_id))

           # if not da.find_by_customer_id(customer_id):
            foodorder = FoodOrder(customer, status, date_time, total_amount)
            da.save(foodorder)
            return True, foodorder
        # else:
        #     raise DuplicateCustomerError("Duplicate customer")
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, customer_id, status, datetime, total_amount):
        try:
            da = FoodOrderDa()
            customer = CustomerController.find_by_id(customer_id)[0]
            foodorder = FoodOrder(customer, status, datetime, total_amount)
            foodorder.id = id
            da.edit(foodorder)
            return True, foodorder
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = FoodOrderDa()
            foodorder = da.find_by_id(FoodOrder, id)
            return True, da.remove(foodorder)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = FoodOrderDa()
            return True, da.find_all(FoodOrder)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = FoodOrderDa()
            foodorder = da.find_by_id(FoodOrder, id)
            if foodorder:
                return True, foodorder
            else:
                raise NoContentError("There is no order!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            da = FoodOrderDa()
            return True, da.find_by_customer_id(customer_id)
        except Exception as e:
            return False, str(e)
