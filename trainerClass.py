class Trainer:
    def __init__(self, trainer_id, trainer_fname, trainer_lname):
        self.trainer_id = trainer_id
        self.trainer_fname = trainer_fname
        self.trainer_lname = trainer_lname
        self.trainerDone = True

    def register_trainer(self):
        # Code to register trainer with given Trainer ID and Name
        trainer_id = self.trainer_id_entry.get()
        name = self.name_entry.get()

        # Code to add trainer to log
        # ...

        print("Trainer registered successfully.")
        
        
    def remove_trainer(self):
        # Code to remove trainer with given Trainer ID
        trainer_id = self.trainer_id_entry.get()

        # Code to remove trainer from log
        # ...

        print("Trainer removed successfully.")
    
    def updateTrainer(self,trainer_id, trainer_fname, trainer_lname):
        #Update trainer details through function. 
        self.trainer_id = trainer_id
        self.trainer_fname = trainer_fname
        self.trainer_lname = trainer_lname
        return 

    def update_trainer(self):
        # Code to update trainer with given Trainer ID and Name
        trainer_id = self.trainer_id_entry.get()
        name = self.name_entry.get()

        # Code to update trainer in log
        # ...

        print("Trainer updated successfully.")

    