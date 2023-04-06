class Trainer:
    def __init__(self, trainer_id, trainer_fname, trainer_lname):
        self.trainer_id = trainer_id
        self.trainer_fname = trainer_fname
        self.trainer_lname = trainer_lname
        self.trainerDone = True

    def registerTrainer(self):
        #Check if trainer is already registered in database
        return 
    def removeTrainer(self):
        #Delete trainer from database
        return
    
    def updateTrainer(self,trainer_id, trainer_fname, trainer_lname):
        #Update trainer details through function. 
        self.trainer_id = trainer_id
        self.trainer_fname = trainer_fname
        self.trainer_lname = trainer_lname
        return 


    

    