from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QDateTime, Qt, QTimer, QTime
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QFormLayout, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QLCDNumber,
        QVBoxLayout, QWidget)

from datetime import datetime, timedelta

FONT = QFont()
FONT.setPointSize(16)  
DURATION = 3 * 60

class Timer(QGroupBox):
    start = False
    count = 300 # MS

    def __init__(self):
        super().__init__("Super Timer")
        self.initWidget()
        
    def initWidget(self):
        self.bStart = QPushButton("Start")
        self.bStart.setFont(FONT)
        self.bStart.clicked.connect(self.start_action)

        bStop = QPushButton("Stop")
        bStop.setFont(FONT)
        bStop.clicked.connect(self.pause_action)

        bReset = QPushButton("Reset")
        bReset.setFont(FONT)
        bReset.clicked.connect(self.reset_action)

        self.label = QLabel("00:00", self)
        self.label.setFont(QFont('Arial', 50))
        self.label.setAlignment(Qt.AlignCenter)
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100) # interval in ms (1000 ms = 1 sec)

        layout = QVBoxLayout()
        layout.addWidget(self.bStart)
        layout.addWidget(bStop)
        layout.addWidget(bReset)
        layout.addWidget(self.label)
        layout.addStretch(1)
        self.setLayout(layout)


    def showTime(self):
        if self.start:
            self.count -= 1
            text = f"{self.count / 10}  s: {self.count}"
            self.label.setText(self.timer_display)
            #self.label.setText(text)
            if self.count == 0:
                self.start = False
                self.label.setText("00:00:00")

    @property
    def timer_display(self):
        m = self.count // (1000 * 60)
        remaining_milliseconds = self.count % (1000 * 60)
        s = remaining_milliseconds // 1000
        ms = remaining_milliseconds % 1000
        #text = f"{self.count / 10}  s: {self.count}"
        return f"{m}:{s}:{ms}" 

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False
 
    def pause_action(self):
        self.start = False
 
    def reset_action(self):
        self.start = False
        self.count = 3000
        self.label.setText(str(self.count))


    def get_seconds(self):
        self.start = False
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')
        if done:
            self.label.setText(str(second))
            
class TimerDisplay(QLabel):
    def __init__(self, duration) -> None:
        super().__init__(self.current )

    def start(self):
        self.t_start = datetime.now().time()

    @property
    def current(self):
        return f""
