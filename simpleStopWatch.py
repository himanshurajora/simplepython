import sys
import time
from PyQt5.QtWidgets import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 300
        self.top = 100
        self.left  =100
        self.initui()

    def initui(self):
        Start_Button = QPushButton("Start", self)
        self.timeLabel = QLabel("0.0",self)
        Stop_Button = QPushButton("Stop", self)
        Reset_Button = QPushButton("Reset", self)

        self.timeLabel.move(50,100)
        Start_Button.move(100,100)
        Stop_Button.move(100,150)
        Reset_Button.move(100,200)
        Start_Button.clicked.connect(self.StartWatch)
        Stop_Button.clicked.connect(self.StopWatch)
        Reset_Button.clicked.connect(self.reset)
        self.setWindowTitle("Stop Watch")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()
    def StartWatch(self):
        self.startTime = time.time()

    def StopWatch(self):
        self.stopTime = time.time()
        self.timeLabel.setText(str(self.stopTime - self.startTime))

    def reset(self):
        self.timeLabel.setText("0.0")
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())