# import mysql.connector
# from customer import Customer
# cnx = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "csi3370!",
#     database ="predatory_elephants"
# )
# cursor = cnx.cursor(buffered=True)
# add_customer = ("INSERT INTO customer "
#                 "(customer_fname,customer_lname)"
#                 "VALUES (%s,%s) ")

# customerInfo = ('john', 'doe')

# read_customer = ("(SELECT * FROM customer WHERE customer_fname = %s and customer_lname = %s)")
# cursor.execute(read_customer, customerInfo)
# myresult = cursor.fetchall()
# for x in myresult:
    # print(x[1:3])
    # print(x)
    #if x[1:3] == customer:
    #    print("already matching")
    


# cursor.execute(add_customer,customer)
# cnx.commit()

#userInfo = Customer('john', 'doe','123 Blueberry Lane', '1234567890')
#userInfo.registerCustomer()


import mysql.connector
from customerclass import Customer
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
)
print(cnx)
cursor = cnx.cursor(buffered=True)
#input from screen
myInput = ['muffin','man', '123 Blueberry lane','1234567890','muffin@bakery.com']
# instantiate class
myCustomer = Customer(myInput[0],myInput[1],myInput[2],myInput[3],myInput[4])

#myCustomer.registerCustomer()
myInfo = myCustomer.get_info()
addCustomer = "INSERT INTO customer (customer_fname, customer_lname, customer_phone, customer_email, customer_gender, customer_address, weight, height, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
cursor.execute(addCustomer, myInfo)
cnx.commit()
getIDquery = ("SELECT customer_id FROM customer WHERE customer_fname = %s AND customer_lname = %s AND customer_phone = %s")
myContact = myCustomer.contact_info()
cursor.execute(getIDquery,myContact)
results = cursor.fetchall()
for result in results:
    customer_id = result[0]
updateBodyInfo = ("UPDATE customer "
                "SET customer_gender = %s, "
                "weight = %s, "
                "height = %s, "
                "age = %s "
                "WHERE customer_id = %s")
bodyInfo = ('M',200,72,45, customer_id)
cursor.execute(updateBodyInfo,bodyInfo)
cnx.commit()
        
cursor.close()
cnx.close()

cursor.close()
cnx.close()