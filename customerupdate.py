import tkinter as tk
import mysql.connector
#from customerclass import Customer
#sudo pip install mysql-connector-python

# Define the main window of the application
root = tk.Tk()
root.title("Body Update Form")

# Set window size
root.geometry("800x800")

# Set background color
root.configure(bg="#e4f5ec")

# Create a frame to contain the input fields
input_frame = tk.Frame(root)
input_frame.config(bg=root["bg"])
input_frame.pack()

title_label = tk.Label(input_frame, text="Body Update Form", font=("arial bold", 20), bg=root["bg"])  

# Create labels and entry fields for each piece of information
gender_label = tk.Label(input_frame, text="Gender: ", font=("arial", 12), bg=root["bg"])
gender_entry = tk.Entry(input_frame)

weight_label = tk.Label(input_frame, text="Weight (lbs):", font=("arial", 12), bg=root["bg"])
weight_entry = tk.Entry(input_frame)

height_label = tk.Label(input_frame, text="Height (cm):", font=("arial", 12), bg=root["bg"])
height_entry = tk.Entry(input_frame)

age_label = tk.Label(input_frame, text="Age: ", font=("arial", 12), bg=root["bg"])
age_entry = tk.Entry(input_frame)



# Add the labels and entry fields to the frame
title_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

gender_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
gender_entry.grid(row=1, column=1, padx=5, pady=5)

weight_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
weight_entry.grid(row=2, column=1, padx=5, pady=5)

height_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
height_entry.grid(row=3, column=1, padx=5, pady=5)

age_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=4, column=1, padx=5, pady=5)

# Connect to the Cloud SQL database
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "csi3370!",
    database ="predatory_elephants"
)
cursor = cnx.cursor(buffered=True)

# Create a function to handle the button click event
def submit_info():
    if not gender_entry.get() or not weight_entry.get() or not height_entry.get() or not age_entry.get():
        error_label.config(text="Please Ensure All Fields Are Filled", fg="red")
        return
    
    try:
        customer_weight = int(weight_entry.get())
    except ValueError:
        error_label.config(text="Enter A Valid Weight In Pounds", fg="red")
        return
    
    try:
        customer_height = int(height_entry.get())
    except ValueError:
        error_label.config(text="Enter A Valid Height In Centimeters", fg="red")
        return
    
    try:
        customer_age = int(age_entry.get())
    except ValueError:
        error_label.config(text="Enter a Valid Age", fg="red")
        return
    
    # Retrieve the highest customer_id
    sql = "SELECT MAX(customer_id) FROM customer"
    cursor.execute(sql)
    result = cursor.fetchone()
    customer_id = result[0] 


    # All entries are valid, submit form
    customer_gender = gender_entry.get()
    customer_weight = int(weight_entry.get())
    customer_height = int(height_entry.get())
    customer_age = int(age_entry.get())

    # Do something with the user's information (Print to console)
    print(f"New Gender: {customer_gender}")
    print(f"New Weight (lbs): {customer_weight}")
    print(f"New Height (cm): {customer_height}")
    print(f"New Age: {customer_age}")
    print(f"Customer ID: {customer_id}")

    #Update customer function
    sql = "UPDATE customer SET customer_gender = %s, weight = %s, height = %s, age = %s WHERE customer_id = %s"
    val = (customer_gender, customer_weight, customer_height, customer_age, customer_id)
    cursor.execute(sql, val)
    cnx.commit()
    cursor.close()
    cnx.close()

    # Clear entries and error label updated
    gender_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    error_label.config(text="Information Successfully Updated. Closing Window...", fg="green")
    #close the screen 4 seconds after the button is pressed
    root.after(4000, root.destroy)

# Add a label to display errors to the user
error_label = tk.Label(root, text="", fg="red", font=("arial",12), bg=root["bg"])
error_label.pack()

# Add a button to submit the information
submit_button = tk.Button(root, text="Submit", font=("arial",10), command=submit_info, relief="raised", borderwidth=5, fg="white", bg="grey", padx=5, pady=5)
submit_button.pack(pady=10)

# Start the application
root.mainloop()
