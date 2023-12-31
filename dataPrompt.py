from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QFormLayout, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

FONT = QFont()
FONT.setPointSize(16)  # Set the desired font size

class DataPrompt(QGroupBox):
    def __init__(self):
        super().__init__("Data Prompt")

        self.promptWeight = QLineEdit()
        self.promptWeight.setValidator(QIntValidator())
        self.promptWeight.setMaxLength(4)
        self.promptWeight.setAlignment(Qt.AlignRight)
        self.promptWeight.setFont(FONT)
        #self.promptWeight.editingFinished.connect(self.enterPress)
    
        labelWeight = QLabel("&Weight:")
        labelWeight.setBuddy(self.promptWeight)
        labelWeight.setFont(FONT)

        self.promptReps = QLineEdit()
        self.promptReps.setValidator(QIntValidator())
        self.promptReps.setMaxLength(2)
        self.promptReps.setAlignment(Qt.AlignRight)
        self.promptReps.setFont(FONT)
        #self.promptReps.editingFinished.connect(self.enterPress)
    
        labelReps = QLabel("&Reps:")
        labelReps.setBuddy(self.promptWeight)
        labelReps.setFont(FONT)

        self.bInsert = QPushButton("+ ADD SET +")
        self.bInsert.setFont(FONT)
        self.bInsert.setStyleSheet("color: orange;")
        self.bInsert.setStyleSheet("background-color: purple")
        self.bInsert.clicked.connect(self.addSet_button_pressed)

        layout = QFormLayout()
        layout.addRow(labelWeight, self.promptWeight)
        layout.addRow(labelReps, self.promptReps)
        layout.addRow(self.bInsert)
        self.setLayout(layout)



    def addSet_button_pressed(self):
        "Events on ADD SET Button click"
       
        # do nothing if either value is empty 
        if self.weight == '' or self.reps == '':
            return

        self.inserter(self.exercise, self.weight, self.reps)
        self.refresher()
        self.sound_end()
        self.timer_reset()
        self.display_reset()

    def display_reset(self):
        self.promptReps.setText("")
        self.promptWeight.setText("")

    def enterPress(self):
        stats = f"Current Stats > Weight: {self.weight} Reps: {self.reps}"
        print(stats)
    
    def register_exercise(self, in_func):
        '''Register the function which will get the 
        current exercise selection. '''
        self.current_exercise = in_func

    def register_data_table_refresher(self, in_func):
        self.refresher = in_func
    
    def register_inserter(self, in_func):
        self.inserter = in_func

    def register_sound_end(self, in_func):
        self.sound_end = in_func

    def register_timer(self, in_func):
        self.timer_reset = in_func
        self.bInsert.clicked.connect(in_func)

    @property
    def exercise(self):
        return self.current_exercise()
    
    @property
    def weight(self):
        return self.promptWeight.text()

    @property
    def reps(self):
        return self.promptReps.text()
