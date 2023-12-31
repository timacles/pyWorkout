from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import ( QGroupBox, QLabel, QPushButton, QVBoxLayout)

from sounds import Sounds


FONT = QFont()
FONT.setPointSize(16)  
DURATION = 3 * 60 * 10
#DURATION = 10 * 10

class Timer(QGroupBox):
    start = True
    count = DURATION

    def __init__(self):
        super().__init__("Super Serious Timer")
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

        self.label = QLabel(self.timer_display)
        self.label.setFont(QFont('Arial', 50))
        self.label.setStyleSheet("color: orange;")
        
        self.sounds = Sounds(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100) # interval in ms (1000 ms = 1 sec)

        layout = QVBoxLayout()
        layout.addWidget(self.bStart)
        layout.addWidget(bStop)
        layout.addWidget(bReset)
        layout.addWidget(self.label)
        layout.setAlignment(self.label, Qt.AlignCenter)
        layout.addStretch(1)
        self.setLayout(layout)


    def showTime(self):
        if self.start:
            self.count -= 1
            self.label.setText(self.timer_display)
            if self.count == 0:
                self.timeExpired()

    def timeExpired(self):
        self.start = False
        self.label.setText("00:00:00")
        self.sounds.gameover()

    @property
    def timer_display(self):
        """Convert the MS count to a timer display showing `00:00:00` """
        c = self.count
        m = int(c / 10 / 60) 
        s = int(c / 10) - (m * 60)
        ms = str(c)[-1:]
        return f"{m:0>2}:{s:0>2}:{ms:0>2}" 

    def start_action(self):
        self.start = True
        if self.count == 0:
            self.start = False
 
    def pause_action(self):
        self.start = False
 
    def reset_action(self):
        self.start = True
        self.count = DURATION
        self.label.setText(self.timer_display)

            


if __name__ == "__main__":
    Sounds.gameover.play()
