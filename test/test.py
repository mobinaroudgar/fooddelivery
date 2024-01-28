# from datetime import datetime
from datetime import datetime

from controller import *
# from model.da import OrderMenuDa, FoodOrderDa
# from model.da.customer_da import CustomerDa
# from model.da.database import *
from model.entity import *
from model.da.database import DataBaseManager
from model.entity import Customer, Address
from model.entity.menu_item import Menu

da = DataBaseManager()
customer1 = Customer("Mobina","roudgar","09384f54210","ro5udga80obina@gmail.com","mobinarou480")
da.save(customer1)

#customer = Customer("ali", "roudgaygdr","09929ff316y485","rouffdgayryasna@gmail.com","mobinarou91")
#da.save(customer)

addres1 = Address(customer1,"narmak",10,6,"Janbazan","hashtom","32sq")
da.save(addres1)

driver1=DeliveryDriver("Ali","alipour")
da.save(driver1)

foodord=FoodOrder(customer1,addres1,driver1,1,datetime.now(),5000,60000,65000)
da.save(foodord)

menu=Menu(1,"peperoni",12)

Order=Classification("PIZZA")
da.save(Order)

Order1=Classification("dessert")
da.save(Order1)




#menu1=Menu("peperoni",1,51)
#da.save(menu1)