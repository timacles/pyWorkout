import time
import sys
from utils import * 

TIMER_DEFAULT = 3
WORKOUTS = ["deadlift", "ohp", "squat"]

def get_workout():
    workout = input("Choose Workout: ")
    if workout not in WORKOUTS:
        print(f"{workout} not found in workout list")
        sys.exit(1)
    return workout

def get_weight():
    weight = input("Enter Weight: ")

def get_reps():
    reps = input("Enter Reps: ")

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write("\rTime remaining: {:2d} seconds".format(i))
        sys.stdout.flush()
        time.sleep(1)
        clear_terminal()
    print("\nTime's up!")
    play_sound()

def main():
    get_weight()
    get_reps()
    countdown_timer(TIMER_DEFAULT)

if __name__ == "__main__":
    while True:
        clear_terminal()
        get_workout()
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting gracefully.")