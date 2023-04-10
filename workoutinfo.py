import random
import tkinter as tk
from tkinter import ttk
from workoutClass import Workout


# Define the main window
root = tk.Tk()
root.title("Workout Information")
root.geometry("800x800")
#Set the background color
root.configure(bg = "#e4f5ec")
#Configuring the background color
input_frame = tk.Frame(root)
input_frame.config(bg=root["bg"])
input_frame.pack()

# Define a function to log the workout
def log_workout():
    exercise = exercise_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()
    sets = sets_entry.get()
    #workout1 = Workout(exercise, reps, weight)
    workout_text.insert(tk.END, f"\nExercise Name: {exercise}, Number of Sets: {sets}, Amount of Reps: {reps}, Weight in Lbs (If Applicable): {weight}")
    #------ For writing the workouts to a txt file, could help when we want to make a database. 
    #with open("workouts.txt", "a") as f:
        #f.write(f"Exercise: {exercise}, Reps: {reps}, Sets: {sets} Weight: {weight}\n")
    exercise_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    sets_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    #workout = (exercise, sets, reps, weight)


# Define a global variable for the exercises
exercises = ["Push-ups", "Squats", "Lunges", "Bicep curls", "Tricep dips", "Crunches", "Plank"]

#Function to generate workout that is pre made 
#--------This will have to access the database when it is created------------
def generate_workout():
    # Create a list of exercises that require weight
    weight_exercises = ["Bicep curls", "Tricep dips"]

    # Generate a random exercise
    exercise = random.choice(exercises)
    exercise_entry.delete(0, tk.END)
    exercise_entry.insert(0, exercise)

    # Generate random sets and reps
    sets = random.randint(1, 10)
    reps = random.randrange(5, 21, 5)

    # If the exercise requires weight, generate a random weight
    if exercise in weight_exercises:
        weight = random.randrange(5, 51, 5)
        weight_entry.delete(0, tk.END)
        weight_entry.insert(0, weight)
    else:
        # Put 0 for weight if doesnt require
        weight_entry.delete(0, tk.END)
        weight_entry.insert(0, 0)

    sets_entry.delete(0, tk.END)
    sets_entry.insert(0, sets)

    reps_entry.delete(0, tk.END)
    reps_entry.insert(0, reps)

# Define the input fields for the exercise, reps, and weight
exercise_label = ttk.Label(root, text="Exercise:")
exercise_entry = ttk.Entry(root, width=30)
reps_label = ttk.Label(root, text="Reps:")
reps_entry = ttk.Entry(root, width=30)
sets_label = ttk.Label(root, text="Sets: ")
sets_entry = ttk.Entry(root, width=30)
weight_label = ttk.Label(root, text="Weight (lbs):")
weight_entry = ttk.Entry(root, width=30)
workout_title_text = ttk.Label(root, text = "Current Workout:")


# Define the log button and its functionality
log_button = ttk.Button(root, text="Add Workout", command=log_workout)
generate_button = ttk.Button(root, text= "Generate Pre-Made Workout", command=generate_workout)
#To generate the text for workouts 
workout_text = tk.Text(root, font=("TkDefaultFont", 12), height=20, width=100)

# Pack the input fields and log button onto the window
exercise_label.pack(pady=10)
exercise_entry.pack(pady=10)
reps_label.pack(pady=10)
reps_entry.pack(pady=10)
sets_label.pack(pady=10)
sets_entry.pack(pady=10)
weight_label.pack(pady=10)
weight_entry.pack(pady=10)
log_button.pack(pady=20)
generate_button.pack(pady = 20)
workout_title_text.pack(pady = 20)
workout_text.pack(pady=10)
#Trying to interact with the class
#print(workout1.get_workout_info())

# Run the main loop
root.mainloop()