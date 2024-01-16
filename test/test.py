# from datetime import datetime
from datetime import datetime

from controller import *
# from model.da import OrderMenuDa, FoodOrderDa
# from model.da.customer_da import CustomerDa
# from model.da.database import *
from model.entity import *
from model.da.database import DataBaseManager
from model.entity import Customer, Address

da = DataBaseManager()
customer1 = Customer("Mobina","roudgar","093898745210","roudga80mdddobina@gmail.com","mobinarou80")
da.save(customer1)

#customer = Customer("ali", "roudgaygdr","09929ff316y485","rouffdgayryasna@gmail.com","mobinarou91")
#da.save(customer)

#addres1 = Address(customer1,"32 sq ")
#da.save(addres1)

#driver1=DeliveryDriver("Ali","alipour")
#da.save(driver1)

#foodord=FoodOrder(customer1,addres1,driver1,1,datetime.now(),5000)
#da.save(foodord)