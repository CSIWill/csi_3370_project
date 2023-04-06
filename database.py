import mysql.connector
from customer import Customer
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
)
cursor = cnx.cursor(buffered=True)
add_customer = ("INSERT INTO customer "
                "(customer_fname,customer_lname)"
                "VALUES (%s,%s) ")

customerInfo = ('john', 'doe')

read_customer = ("(SELECT * FROM customer WHERE customer_fname = %s and customer_lname = %s)")
cursor.execute(read_customer, customerInfo)
myresult = cursor.fetchall()
for x in myresult:
    # print(x[1:3])
    print(x)
    #if x[1:3] == customer:
    #    print("already matching")
    


# cursor.execute(add_customer,customer)
# cnx.commit()

#userInfo = Customer('john', 'doe','123 Blueberry Lane', '1234567890')
#userInfo.registerCustomer()


cursor.close()
cnx.close()