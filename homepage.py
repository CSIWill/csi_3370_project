import tkinter as tk

# Create a new window
root = tk.Tk()
root.title("Homepage Workout App")
root.geometry("800x800")

# Set background color
root.configure(bg="#e4f5ec")

# Define the function for button 1
def open_file1():
    import customerinfo 
    #customerinfo.main() # Call the main function from customerinfo

# Define the function for button 2
def open_file2():
    import workoutinfo 
    #workout.main() # Call the main function from workoutinfo
    
# Define the function for button 3
def open_file3():
    import testTrainer 
    #testTrainer.main() # Call the main function from testTrainer
    
title = tk.Label(root, text = "Predatory Elephants Workout App")
title.pack(pady = 20)
# Create two buttons to access the other Tkinter files
button1 = tk.Button(root, text="Open Customer Info", command=open_file1)
button1.pack(padx=100)

button2 = tk.Button(root, text="Open Workout Info", command=open_file2)
button2.pack(pady=100)

button3 = tk.Button(root, text="Open Trainer Info", command=open_file3)
button3.pack(padx=100)

# Run the window
root.mainloop()