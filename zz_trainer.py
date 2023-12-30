from exercise import Exercise, Set
from screen import red

INP_EXERCISE = "Input EXERCISE: "
INP_WEIGHT = "Input WEIGHT: "
INP_REPS = "Input REPS: "


class Trainer:
    db = None

    def __init__(self):
        self.set = None
    
    def get_exercise(self):
        self.exercise = Exercise(input(INP_EXERCISE))

    def get_set(self):
        weight = check_int_loop(INP_WEIGHT)
        reps = check_int_loop(INP_REPS)
        self.set = Set(weight, reps)
    
    def get_data(self):
        rows = self.db.get_exercise(self.exercise.name)
        for row in rows:
            print(row)

    def save_set(self):
        self.db.insert_set(
            self.exercise.name,
            self.set.weight,
            self.set.reps
        )


def check_int_loop(input_ques: str):
     while True:
        try:
            return int(input(input_ques))
        except ValueError:
            red("Invalid Input")
            pass

       