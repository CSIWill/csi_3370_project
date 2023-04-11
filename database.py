
from customerclass import Customer
#Test
myInput = ['muffin','man', '123 Blueberry lane','1234567890','muffin@bakery.com']
# instantiate class
myCustomer = Customer(myInput[0],myInput[1],myInput[2],myInput[3],myInput[4])

myCustomer.registerCustomer()
myCustomer.updateInfoGoals('M',155,72,50)

myCustomer.closecnx()