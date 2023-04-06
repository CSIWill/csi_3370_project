class Customer():
    def __init__(self, firstname, lastname, address, phone):
        self.__customer_firstname = firstname
        self.__customer_lastname = lastname
        self.__customer_address = address
        self.__customer_phone = phone
        self.__customer_gender = 0
        self.__weight = 0
        self.__height = 0
        self.__age = 0
        self.__customer_id = 0
    def registerCustomer(self,firstname,lastname, address, phone):
        customer = (firstname,lastname)
        checkCustomer = ("SELECT * FROM customer WHERE customer_fname = %s and customer_lname = %s")
        ifcheckCustomer
        
        # check to see if customer already exists in database
        # if not found, commit to database, and change customer_id to primary key value
        return
    def updateCustomer(self, firstname, lastname, address, phone):
        self.__customer_firstname = firstname
        self.__customer_lastname = lastname
        self.__customer_address = address
        self.__customer_phone = phone
        # push new info to existing customer with matching ID in database
        return
    def deleteCustomer(self):
        # delete entry in database
        return
    def updateInfoGoals(self, gender, weight, height, age):
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__age = age
        
        return
    def get_info(self):
        return f"{self.__customer_firstname}, {self.__custiner_lastname}"
    def requestRoutine(self):
        return
    def addRoutine(self):
        return
    def removeRoutine(self):
        return
    def trackWorkout(self):
        return
    
        
