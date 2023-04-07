import tkinter as tk

class TrainerRegistrationGUI:

    def __init__(self, master):
        self.master = master
        master.title("Trainer Information Input")
        root.geometry("800x800")
        
        # Set background color
        root.configure(bg="#e4f5ec")

        # Labels for Trainer ID and Name
        self.trainer_id_label = tk.Label(master, text="Trainer ID")
        self.trainer_id_label.grid(row=0, column=0, padx=200, pady=100)

        self.name_label = tk.Label(master, text="Name")
        self.name_label.grid(row=1, column=0,  padx=200, pady=100)

        # Entries for Trainer ID and Name
        self.trainer_id_entry = tk.Entry(master)
        self.trainer_id_entry.grid(row=0, column=1)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        # Register Button
        self.register_button = tk.Button(master, text="Register", command=self.register_trainer)
        self.register_button.grid(row=2, column=0, pady=100)

        # Update Button
        self.update_button = tk.Button(master, text="Update", command=self.update_trainer)
        self.update_button.grid(row=2, column=1, pady=100)

        # Remove Button
        self.remove_button = tk.Button(master, text="Remove", command=self.remove_trainer)
        self.remove_button.grid(row=2, column=2, pady=100)
            
           

root = tk.Tk()
my_gui = TrainerRegistrationGUI(root)
root.mainloop()