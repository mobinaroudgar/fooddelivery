# from datetime import datetime
from controller import *
# from model.da import OrderMenuDa, FoodOrderDa
# from model.da.customer_da import CustomerDa
# from model.da.database import *
# from model.entity import *
from model.da.database import DataBaseManager
from model.entity import Customer, Address

da = DataBaseManager()
#customer1 = Customer("Mobina","roudgar","09389874210","roudgarmobina@gmail.com","mobinarou80")
#da.save(customer1)

#customer = Customer("ali", "roudgaygdr","09929ff316y485","rouffdgayryasna@gmail.com","mobinarou91")
#da.save(customer)

addres1 = Address(None,"htyyykolyh hy85")
da.save(addres1)
