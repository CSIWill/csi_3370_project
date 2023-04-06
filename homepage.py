import tkinter as tk

# Create a new window
root = tk.Tk()
root.title("Homepage Workout App")
root.geometry("400x700")

# Define the function for button 1
def open_file1():
    import customerinfo # Import the other Tkinter file
    customerinfo.main() # Call the main function from file1

# Define the function for button 2
def open_file2():
    import workout # Import the other Tkinter file
    workout.main() # Call the main function from file2
    
# Define the function for button 3
def open_file3():
    import testTrainer # Import the other Tkinter file
    testTrainer.main() # Call the main function from file2
    
# Define the function for button 4
def open_file4():
    import test2 # Import the other Tkinter file
    test2.main() # Call the main function from file2

# Create two buttons to access the other Tkinter files
button1 = tk.Button(root, text="Open File 1", command=open_file1)
button1.pack(padx=100)

button2 = tk.Button(root, text="Open File 2", command=open_file2)
button2.pack(pady=100)

button3 = tk.Button(root, text="Open File 3", command=open_file3)
button3.pack(padx=100)

button4 = tk.Button(root, text="Open File 4", command=open_file4)
button4.pack(pady=100)

# Run the window
root.mainloop()