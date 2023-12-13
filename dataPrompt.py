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
        self.promptWeight.editingFinished.connect(self.enterPress)
    
        labelWeight = QLabel("&Weight:")
        labelWeight.setBuddy(self.promptWeight)
        labelWeight.setFont(FONT)

        self.promptReps = QLineEdit()
        self.promptReps.setValidator(QIntValidator())
        self.promptReps.setMaxLength(2)
        self.promptReps.setAlignment(Qt.AlignRight)
        self.promptReps.setFont(FONT)
        self.promptReps.editingFinished.connect(self.enterPress)
    
        labelReps = QLabel("&Reps:")
        labelReps.setBuddy(self.promptWeight)
        labelReps.setFont(FONT)

        bInsert = QPushButton("Add +")
        bInsert.setFont(FONT)
        bInsert.clicked.connect(self.insertData)

        layout = QFormLayout()
        layout.addRow(labelWeight, self.promptWeight)
        layout.addRow(labelReps, self.promptReps)
        layout.addRow(bInsert)
        self.setLayout(layout)

    def insertData(self):
        stats = f"Insert pressed > Ex: {self.selector()} Weight: {self.weight} Reps: {self.reps}"
        print(stats)

    def enterPress(self):
        stats = f"Current Stats > Weight: {self.weight} Reps: {self.reps}"
        print(stats)
    
    @property
    def weight(self):
        return self.promptWeight.text()

    @property
    def reps(self):
        return self.promptReps.text()
    
    def register_selector(self, in_func):
        '''Register the function which will get the 
        current exercise selection. '''
        self.selector = in_func