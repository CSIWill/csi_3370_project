import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image

# Create a new window
root = tk.Tk()
root.title("Predatory Elephants Workout App")
root.geometry("1150x800")

# Set background color and fonts
root.configure(bg="#e4f5ec")
title_font = font.Font(family='arial', size=40, weight='bold')
button_font = font.Font(family='arial', size=20, weight='bold')
#Frame for picture
frame = Frame(root, width=300, height=300, bg="#e4f5ec")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.35)
logo_pic = ImageTk.PhotoImage(Image.open("predatoryelephant.png"))

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
    import routineinfo
    #routineinfo.main() # Call the main function from routineinfo

# Define the function for button 4
def open_file4():
    import customerupdate 
    #testTrainer.main() # Call the main function from customerupdate

# Define the function for button 5
def open_file5():
    import testTrainer 
    #testTrainer.main() # Call the main function from testTrainer
    
#Title labels, logo, and buttons
logo_label = Label(frame, image = logo_pic, bg="#e4f5ec")
logo_label.pack(pady = 20)

title_label = tk.Label(root, text="Predatory Elephants Workout App", font=title_font,bg="#e4f5ec")
title_label.pack(pady = 20)


button_frame = tk.Frame(root, bg="#e4f5ec")
button_frame.pack(pady = 50)

button1 = tk.Button( text="Customer Info", font=button_font,  bg="#e4f5ec", command=open_file1)
button1.pack(side=tk.LEFT, padx = 20)

button2 = tk.Button( text="Workout Info", font=button_font,  bg="#e4f5ec", command=open_file2)
button2.pack(side=tk.LEFT, padx = 20)

button3 = tk.Button( text="Routine Info", font=button_font,  bg="#e4f5ec", command=open_file3)
button3.pack(side=tk.LEFT, padx = 20)

button4 = tk.Button( text="Update Info", font=button_font,  bg="#e4f5ec", command=open_file4)
button4.pack(side=tk.LEFT, padx = 20)

button5 = tk.Button( text="Trainer Info", font=button_font,  bg="#e4f5ec", command=open_file5)
button5.pack(side=tk.LEFT, padx = 20)

# Run the window
root.mainloop()