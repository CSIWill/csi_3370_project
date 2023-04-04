import tkinter as tk

class TrainerRegistrationGUI:

    def __init__(self, master):
        self.master = master
        master.title("Trainer Registration")

        # Labels for Trainer ID and Name
        self.trainer_id_label = tk.Label(master, text="Trainer ID")
        self.trainer_id_label.grid(row=0, column=0)

        self.name_label = tk.Label(master, text="Name")
        self.name_label.grid(row=1, column=0)

        # Entries for Trainer ID and Name
        self.trainer_id_entry = tk.Entry(master)
        self.trainer_id_entry.grid(row=0, column=1)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        # Register Button
        self.register_button = tk.Button(master, text="Register", command=self.register_trainer)
        self.register_button.grid(row=2, column=0)

        # Update Button
        self.update_button = tk.Button(master, text="Update", command=self.update_trainer)
        self.update_button.grid(row=2, column=1)

        # Remove Button
        self.remove_button = tk.Button(master, text="Remove", command=self.remove_trainer)
        self.remove_button.grid(row=2, column=2)

    def register_trainer(self):
        # Code to register trainer with given Trainer ID and Name
        trainer_id = self.trainer_id_entry.get()
        name = self.name_entry.get()

        # Code to add trainer to log
        # ...

        print("Trainer registered successfully.")

    def update_trainer(self):
        # Code to update trainer with given Trainer ID and Name
        trainer_id = self.trainer_id_entry.get()
        name = self.name_entry.get()

        # Code to update trainer in log
        # ...

        print("Trainer updated successfully.")

    def remove_trainer(self):
        # Code to remove trainer with given Trainer ID
        trainer_id = self.trainer_id_entry.get()

        # Code to remove trainer from log
        # ...

        print("Trainer removed successfully.")

root = tk.Tk()
my_gui = TrainerRegistrationGUI(root)
root.mainloop()