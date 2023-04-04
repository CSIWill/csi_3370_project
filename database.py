import mysql.connector

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
)
cursor = cnx.cursor(buffered=True)
add_customer = ("INSERT INTO customer "
                "(customer_fname,customer_lname)"
                "VALUES (%s,%s)")



customer = ('john', 'doe')


cursor.execute(add_customer,customer)
cnx.commit()

read_customer = ("Select * From customer")

print(cursor.execute(read_customer))

cursor.close()
cnx.close()