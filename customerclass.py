import mysql.connector

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
    )


class Customer():
    def __init__(self, firstname, lastname, address, phone, email, gender='NA',weight=0,height=0,age=0):
        self.__customer_firstname = firstname
        self.__customer_lastname = lastname
        self.__customer_address = address
        self.__customer_email = email
        self.__customer_phone = phone
        self.__customer_gender = gender
        self.__weight = weight
        self.__height = height
        self.__age = age
        self.__customer_id = 0
    def get_info(self):
        return (self.__customer_firstname, self.__customer_lastname, self.__customer_phone, self.__customer_email, self.__customer_gender, self.__customer_address, self.__weight, self.__height, self.__age)
    def contact_info(self):
        return (self.__customer_firstname, self.__customer_lastname, self.__customer_phone)

    def getCustomerID(self):
        cursor = cnx.cursor(buffered=True)
        getIDquery = ("SELECT customer_id FROM customer WHERE customer_fname = %s AND customer_lname = %s AND customer_phone = %s")
        contact = (self.__customer_firstname,self.__customer_lastname,self.__customer_phone)
        cursor.execute(getIDquery,contact)
        results = cursor.fetchall()
        if len(results) < 1:
            self.__customer_id = 0
        else:
            self.__customer_id = results[0][0]
        cursor.close()
        # cnx.close()
        return self.__customer_id
    def registerCustomer(self):
        cursor1 = cnx.cursor(buffered=True)
        # check to see if customer already exists in database
        
        if self.getCustomerID() == 0:
            print("creating customer")
            addCustomer = "INSERT INTO customer (customer_fname, customer_lname, customer_phone, customer_email, customer_gender, customer_address, weight, height, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            info = self.get_info()
            
            
            cursor1.execute(addCustomer,info)
            cnx.commit()
        else:
            print("customer already exists")
        # if not found, commit to database, and change customer_id to primary key value
        
        cursor1.close()
        # cnx.close()
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
    def updateInfoGoals(self, gender='NA', weight=0, height=0, age=0):
        cursor2 = cnx.cursor(buffered=True)
        self.__customer_gender = gender
        self.__weight = weight
        self.__height = height
        self.__age = age
        updateBodyInfo = ("UPDATE customer "
                          "SET customer_gender = %s, "
                          "weight = %s, "
                          "height = %s, "
                          "age = %s "
                          "WHERE customer_id = %s")
        self.getCustomerID()
        bodyInfo = (self.__customer_gender,self.__weight,self.__height,self.__age, self.__customer_id)
        cursor2.execute(updateBodyInfo,bodyInfo)
        cnx.commit()
        cursor2.close()
        return
    def requestRoutine(self):
        return
    def addRoutine(self):
        return
    def removeRoutine(self):
        return
    def trackWorkout(self):
        return
    def closecnx(self):
        cnx.close()
        return
