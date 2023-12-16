from dataclasses import dataclass
from datetime import datetime
from typing import List
from screen import red
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QFormLayout, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

EXERCISES = ["deadlift", "ohp", "squat"]

FONT = QFont()
FONT.setPointSize(16)  

class ExerciseSelector(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.options = Options()

        text = QLabel("&Exercise:")
        text.setBuddy(self.options)
        text.setFont(FONT)

        self.addWidget(text)
        self.addWidget(self.options)
        self.addStretch(1)

    def get_value(self):
        return self.options.value()
    
    def register_refresher(self, in_func):
        self.options.currentIndexChanged.connect(in_func)


class Options(QComboBox):
    def __init__(self) -> None:
        super().__init__()
        self.addItems(EXERCISES)
        self.setFont(FONT)
    
    def value(self):
        ##return self.itemData(self.currentIndex())
        return self.currentText()


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
            

class BAD_EXERCISE(Exception): pass

@dataclass
class Workout:
    created: datetime
    end: datetime
    exercises: List[Exercise] 

    def __init__(self):
        self.start = datetime.now()
    
    def add(self, excersize): 
        self.exercises.append(excersize)
        