from dataclasses import dataclass
from datetime import datetime
from typing import List
from screen import red

EXERCISES = ["deadlift", "ohp", "squat"]

class BAD_EXERCISE(Exception): pass
        
@dataclass
class Set:
    weight: int
    reps: int

    def __init__(self, weight: int, reps: int):
        self.weight = weight
        self.reps = reps

class Exercise:
    def __init__(self, name: str):
        self.name = name
        self._check()
        self.set = None
    
    def _check(self):
        'check our inputs are valid'
        if self.name not in EXERCISES:
            red(f"{self.name} not found in exercise options")
            raise BAD_EXERCISE
            

@dataclass
class Workout:
    created: datetime
    end: datetime
    exercises: List[Exercise] 

    def __init__(self):
        self.start = datetime.now()
    
    def add(self, excersize): 
        self.exercises.append(excersize)
        