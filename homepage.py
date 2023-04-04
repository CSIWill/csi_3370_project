import tkinter as tk

# Create a new window
root = tk.Tk()
root.title("Home Page")

# Define the function for button 1
def open_file1():
    import file1 # Import the other Tkinter file
    file1.main() # Call the main function from file1

# Define the function for button 2
def open_file2():
    import file2 # Import the other Tkinter file
    file2.main() # Call the main function from file2

# Create two buttons to access the other Tkinter files
button1 = tk.Button(root, text="Open File 1", command=open_file1)
button1.pack()

button2 = tk.Button(root, text="Open File 2", command=open_file2)
button2.pack()

# Run the window
root.mainloop()