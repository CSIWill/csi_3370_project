import tkinter as tk
from customer import Customer


# Define the main window of the application
root = tk.Tk()
root.title("User Information")
root.geometry("400x700")

# Create a frame to contain the input fields
input_frame = tk.Frame(root)
input_frame.pack()

# Create labels and entry fields for each piece of information  
fname_label = tk.Label(input_frame, text="First Name: ")
fname_entry = tk.Entry(input_frame)

lname_label = tk.Label(input_frame, text="Last Name: ")
lname_entry = tk.Entry(input_frame)

phone_label = tk.Label(input_frame, text="Phone: ")
phone_entry = tk.Entry(input_frame)

gender_label = tk.Label(input_frame, text="Gender: ")
gender_entry = tk.Entry(input_frame)

address_label = tk.Label(input_frame, text="Address: ")
address_entry = tk.Entry(input_frame)

weight_label = tk.Label(input_frame, text="Weight: ")
weight_entry = tk.Entry(input_frame)

height_label = tk.Label(input_frame, text="Height: ")
height_entry = tk.Entry(input_frame)

age_label = tk.Label(input_frame, text="Age: ")
age_entry = tk.Entry(input_frame)



# Add the labels and entry fields to the frame
fname_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
fname_entry.grid(row=0, column=1, padx=5, pady=5)

lname_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
lname_entry.grid(row=1, column=1, padx=5, pady=5)

phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

gender_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
gender_entry.grid(row=3, column=1, padx=5, pady=5)

address_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
address_entry.grid(row=4, column=1, padx=5, pady=5)

weight_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
weight_entry.grid(row=0, column=3, padx=5, pady=5)

height_label.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
height_entry.grid(row=1, column=3, padx=5, pady=5)

age_label.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=2, column=3, padx=5, pady=5)

# Create a function to handle the button click event
def submit_info():
    fname = fname_entry.get()
    lname = lname_entry.get()
    phone = phone_entry.get()
    gender = gender_entry.get()
    address = address_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    age = age_entry.get()
    
    # Do something with the user's information (e.g. print it to the console)
    print(f"First Name: {fname}")
    print(f"Last Name: {lname}")
    print(f"Phone: {phone}")
    print(f"Gender: {gender}")
    print(f"Address: {address}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    #Interact with customer class and create an object.
    customer1 = Customer(fname, lname, address, phone)
    #Write to text doc
    with open("customers.txt", "a") as f:
        f.write(f"\nFirst Name: {fname}\nLast Name: {lname}\nPhone: {phone}\nGender: {gender}\nAddress: {address}\nWeight: {weight}\nHeight: {height}\nAge: {age}\n---------------")

# Add a button to submit the information
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.pack(pady=10)
# Start the application
root.mainloop()
