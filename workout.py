from trainer import Trainer
from exercise import BAD_EXERCISE
import utils
from screen import yellow
from database import Database

TIMER = 3

def main():
    trainer = Trainer()
    trainer.db = Database()

    while True:
        try:
            trainer.get_exercise()
            trainer.get_data()
        except BAD_EXERCISE:
            continue
        except KeyboardInterrupt:
            break
        while True:
            try:
                trainer.get_set()
                trainer.save_set()
                utils.countdown_timer(TIMER)
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
        utils.clear_terminal()
        main()
        yellow("\n\n... exiting workout.")