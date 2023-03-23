class Routine():
      def __int__(self, name, date, description, customer_id):
            self.routine_name = name
            self.routine_date = date
            self.routine_description = description
            self.routine_customer_id = customer_id
      def addRoutine(self, name, date, description, customer_id):
            self.routine_name = name
            self.routine_date = date
            self.routine_description = description
            self.routine_customer_id = customer_id
            #Adds routine to database
            return
      def updateRoutine(self, name, date, description, customer_id):
            self.routine_name = name
            self.routine_date = date
            self.routine_description = description
            self.routine_customer_id = customer_id
            #Updates routine in database
            return
      def deleteRoutine(self):
            #Deletes routine from database
            return
      def addWorkout(self):
            #Adds workout to routine.
            return
      def removeWorkout(self):
            #Remove workout item from routine.
            return
      def updateWorkout(self):
            #Update workout in routine.
            return
      def deleteWorkout(self):
            #Delete workout from database.
            return