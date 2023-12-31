import sys, os
import time
import winsound
from datetime import datetime

def play_sound():
    #winsound.PlaySound(, winsound.SND_FILENAME)
    winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 milliseconds

def clear_terminal():
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Linux and macOS
        os.system('clear')

def flash_screen():
    for i in range(1,3):
        print("\033[41m\033[2J", end="")
        time.sleep(1)
        print("\033[0m")
        time.sleep(1)

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write("\rTime remaining: {:2d} seconds".format(i))
        sys.stdout.flush()
        time.sleep(1)
    print("\nTime's up!")
    play_sound()
    
def today():
    return datetime.now().strftime('%Y-%m-%d')