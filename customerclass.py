import mysql.connector
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
    )
cursor = cnx.cursor(buffered=True)

class Customer():
    def __init__(self, firstname, lastname, address, phone, email):
        self.__customer_firstname = firstname
        self.__customer_lastname = lastname
        self.__customer_address = address
        self.__customer_email = email
        self.__customer_phone = phone
        self.__customer_gender = 'NA'
        self.__weight = 0
        self.__height = 0
        self.__age = 0
        self.__customer_id = 0
    def registerCustomer(self):
        
        # check to see if customer already exists in database
        # if not found, commit to database, and change customer_id to primary key value
        addCustomer = "INSERT INTO customer (customer_fname, customer_lname, customer_phone, customer_email, customer_gender, customer_address, weight, height, age) VALUES (%s, %s, %s, %s, %s, %s, %i, %i, %i)"
        info = (self.__customer_firstname,self.__customer_lastname, self.__customer_phone, self.__customer_email, self.__customer_gender, self.__customer_address, self.__weight, self.__height, self.__age)
        cursor.execute(addCustomer,info)
        cnx.commit()
        cursor.close()
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
        cursor = cnx.cursor(buffered=True)
        self.__customer_gender = gender
        self.__weight = weight
        self.__height = height
        self.__age = age
        getIDquery = ("SELECT customer_id FROM customer WHERE customer_fname = %s AND customer_lname = %s AND customer_phone = %s")
        customerContact = (self.__customer_firstname, self.__customer_lastname, self.__customer_phone)
        cursor.execute(getIDquery,customerContact)
        results = cursor.fetchall()
        for result in results:
            customer_id = result[0]
        updateBodyInfo = ("UPDATE customer "
                          "SET gender = %s, "
                          "weight = %i, "
                          "height = %i, "
                          "age = %i "
                          "WHERE customer_id = %i")
        bodyInfo = (self.__customer_gender,self.__weight,self.__height,self.__age, customer_id)
        cursor.execute(updateBodyInfo,bodyInfo)
        cnx.commit()
        cursor.close()
        return
    def get_info(self):
        
        return (self.__customer_firstname, self.__customer_lastname, self.__customer_phone, self.__customer_email, self.__customer_gender, self.__customer_address, self.__weight, self.__height, self.__age)
    def contact_info(self):
        return (self.__customer_firstname, self.__customer_lastname, self.__customer_phone)
    def requestRoutine(self):
        return
    def addRoutine(self):
        return
    def removeRoutine(self):
        return
    def trackWorkout(self):
        return
    cnx.close()
        
