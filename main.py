# https://wiki.python.org/moin/PyQt/Tutorials

from dataPrompt import DataPrompt
from dataTable import WorkoutTable

import sys
import qdarkstyle

from exercise import EXERCISES

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
    def __init__(self, parent=None):
        super().__init__()

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(EXERCISES)
        styleComboBox.setFont(FONT)

        styleLabel = QLabel("&Exercise:")
        styleLabel.setBuddy(styleComboBox)
        styleLabel.setFont(FONT)

        # Create main sections 
        myWorkoutTable = WorkoutTable()
        myDataPrompt = DataPrompt()

        #self.initDataEntryGroup()
        self.initTimerGroup()
        #self.initDataTable()
        self.createProgressBar()

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(myDataPrompt, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(myWorkoutTable, 2, 0, 1, 2)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def initTimerGroup(self):
        self.topRightGroupBox = QGroupBox("Timer")

        bStart = QPushButton("Start")
        bStart.setFont(FONT)
        bStart.clicked.connect(self.start_action)

        bStop = QPushButton("Stop")
        bStop.setFont(FONT)
        bStop.clicked.connect(self.pause_action)

        bReset = QPushButton("Reset")
        bReset.setFont(FONT)
        bReset.clicked.connect(self.reset_action)

        self.label = QLabel("00:00", self)
        self.label.setFont(QFont('Arial', 50))
        self.label.setAlignment(Qt.AlignCenter)
        self.start = False
        self.count = 300 
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

        layout = QVBoxLayout()
        layout.addWidget(bStart)
        layout.addWidget(bStop)
        layout.addWidget(bReset)
        layout.addWidget(self.label)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def showTime(self):
        if self.start:
            self.count -= 1
            if self.count == 0:
                self.start = False
                self.label.setText("Completed !!!! ")
        if self.start:
            text = str(self.count / 10) + " s"
            self.label.setText(text)

    def get_seconds(self):
        self.start = False
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')
        if done:
            self.count = second * 10
            self.label.setText(str(second))

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False
 
    def pause_action(self):
        self.start = False
 
    def reset_action(self):
        self.start = False
        self.count = 300
        self.label.setText(str(self.count))


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
    
    