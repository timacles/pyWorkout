# https://wiki.python.org/moin/PyQt/Tutorials

from dataPrompt import DataPrompt
from dataTable import DataDisplay, insert_data 
from timer import Timer

import sys
import qdarkstyle

from exercise import EXERCISES, ExerciseSelector

from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QFormLayout, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

FONT = QFont()
FONT.setPointSize(16)  # Set the desired font size



class WorkoutApp(QDialog):
    def __init__(self):
        super().__init__()

        self.originalPalette = QApplication.palette()

        # Main sections 
        selector = ExerciseSelector()
        data_display = DataDisplay()
        data_prompt = DataPrompt()
        data_prompt.register_selector(selector.get_value)
        data_display.register_selector(selector.get_value)
        data_prompt.register_inserter(insert_data)
        data_prompt.register_refresher(data_display.refresh)
        selector.register_refresher(data_display.refresh)
        
        timer = Timer()

        self.createProgressBar()

        mainLayout = QGridLayout()
        mainLayout.addLayout(selector, 0, 0, 1, 2)
        mainLayout.addWidget(data_prompt, 1, 0)
        mainLayout.addWidget(timer, 1, 1)
        mainLayout.addWidget(data_display, 2, 0, 1, 2)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)

        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Tim's Workout App")

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    gallery = WorkoutApp()
    gallery.show()
    sys.exit(app.exec())
    
    