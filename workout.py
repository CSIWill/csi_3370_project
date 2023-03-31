class Workout():
      def __int__(self, workoutname, sets, reps, weight):
            self.workout_workoutname = workoutname
            self.workout_reps = reps
            self.workout_sets = sets
            self.weight = weight
      def addRep(self, reps):
            #Add more reps to the workout
            self.workout_reps = reps
            return
      def removeRep(self, reps):
            #Remove reps from the workout
            self.workout_reps = reps
            return
      def addSet(self, sets):
            #Add sets to the workout
            self.workout_sets = sets
            return
      def removeSet(self, sets):
            #Remove sets from the workout
            self.workout_sets = sets
            return
      def get_workout_info(self):
            return f"Workout: {self.workoutname}, {self.reps}, {self.reps}"

