import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Edu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.code = "jake maa chuda"
        self.flag = 0
        self.title = "Matrix Calculator"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.demomatrix = [[0 for i in range(3)] for j in range(3)]
        self.matrix3 = [[0 for i in range(3)] for j in range(3)]
        self.elements()
        self.initmain()

    def initmain(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def elements(self):
        self.PushButton_Add = QPushButton("+", self)
        self.PushButton_Add.move(250,10)
        self.PushButton_Subs = QPushButton("-", self)
        self.PushButton_Subs.move(150,10)
        self.PushBUtton_Mul = QPushButton("*", self)
        self.PushBUtton_Mul.move(50, 10)
        self.PushButton_next = QPushButton("Save ->>", self)
        self.PushButton_next.move(200,50)
        self.PushButton_next.setToolTip("save it and go to next matrix")
        self.PushButton_Previous = QPushButton("<<-Previous", self)
        self.PushButton_Previous.move(100, 50)
        self.PushButton_Previous.setToolTip("go to previous matrix")
        self.PushButton_Previous.clicked.connect(self.gotopre)
        self.val1 = QLineEdit(self)
        self.val1.move(50,100)
        self.val2 = QLineEdit(self)
        self.val2.move(150,100)
        self.val3 = QLineEdit(self)
        self.val3.move(250,100)
        self.val4 = QLineEdit(self)
        self.val4.move(50,150)
        self.val5 = QLineEdit(self)
        self.val5.move(150,150)
        self.val6 = QLineEdit(self)
        self.val6.move(250,150)
        self.val7 = QLineEdit(self)
        self.val7.move(50,200)
        self.val8 = QLineEdit(self)
        self.val8.move(150,200)
        self.val9 = QLineEdit(self)
        self.val9.move(250,200)
        self.PushButton_reset = QPushButton("Reset", self)
        self.PushButton_reset.move(150, 250)
        self.allzero()
        self.PushButton_next.clicked.connect(self.getvalues)
        self.PushButton_Add.clicked.connect(self.addmat)
        self.PushButton_Subs.clicked.connect(self.submat)
        self.PushBUtton_Mul.clicked.connect(self.mulmat)
        self.PushButton_reset.clicked.connect(self.resetprogram)
        self.PushButton_next.clicked.connect(self.gonext)
        self.show()

    def gotopre(self):
        self.val1.setText(str(self.matrix1[0][0]))
        self.val2.setText(str(self.matrix1[0][1]))
        self.val3.setText(str(self.matrix1[0][2]))
        self.val4.setText(str(self.matrix1[1][0]))
        self.val5.setText(str(self.matrix1[1][1]))
        self.val6.setText(str(self.matrix1[1][2]))
        self.val7.setText(str(self.matrix1[2][0]))
        self.val8.setText(str(self.matrix1[2][1]))
        self.val9.setText(str(self.matrix1[2][2]))
        self.flag = 0
	
    def allzero(self):
        self.val1.setText("0")
        self.val2.setText("0")
        self.val3.setText("0")
        self.val4.setText("0")
        self.val5.setText("0")
        self.val6.setText("0")
        self.val7.setText("0")
        self.val8.setText("0")
        self.val9.setText("0")
    def gonext(self):
        if(self.flag == 1):
            self.val1.setText(str(self.matrix3[0][0]))
            self.val2.setText(str(self.matrix3[0][1]))
            self.val3.setText(str(self.matrix3[0][2]))
            self.val4.setText(str(self.matrix3[1][0]))
            self.val5.setText(str(self.matrix3[1][1]))
            self.val6.setText(str(self.matrix3[1][2]))
            self.val7.setText(str(self.matrix3[2][0]))
            self.val8.setText(str(self.matrix3[2][1]))
            self.val9.setText(str(self.matrix3[2][2]))
            self.flag = 1
        else:
            print("skipped")
    def getvalues(self):
        if(self.flag == 0):
            self.matrix1 = [[0 for i in range(3)] for j in range(3)]
            self.matrix1[0][0] = int(self.val1.text())
            self.matrix1[0][1] = int(self.val2.text())
            self.matrix1[0][2] = int(self.val3.text())
            self.matrix1[1][0] = int(self.val4.text())
            self.matrix1[1][1] = int(self.val5.text())
            self.matrix1[1][2] = int(self.val6.text())
            self.matrix1[2][0] = int(self.val7.text())
            self.matrix1[2][1] = int(self.val8.text())
            self.matrix1[2][2] = int(self.val9.text())
            print(self.matrix1[0][0])
            print(self.matrix1[0][1])
            print(self.matrix1[0][2])
            print(self.matrix1[1][0])
            print(self.matrix1[1][1])
            print(self.matrix1[1][2])
            print(self.matrix1[2][0])
            print(self.matrix1[2][1])
            print(self.matrix1[2][2])
            self.allzero()
            self.flag = 1
        elif(self.flag == 1):
            self.matrix2 = [[0 for i in range(3)] for j in range(3)]
            self.matrix2[0][0] = int(self.val1.text())
            self.matrix2[0][1] = int(self.val2.text())
            self.matrix2[0][2] = int(self.val3.text())
            self.matrix2[1][0] = int(self.val4.text())
            self.matrix2[1][1] = int(self.val5.text())
            self.matrix2[1][2] = int(self.val6.text())
            self.matrix2[2][0] = int(self.val7.text())
            self.matrix2[2][1] = int(self.val8.text())
            self.matrix2[2][2] = int(self.val9.text())
            
            self.matrix3[0][0] = self.matrix2[0][0]
            self.matrix3[0][1] = self.matrix2[0][1]
            self.matrix3[0][2] = self.matrix2[0][2]
            self.matrix3[1][0] = self.matrix2[1][0]
            self.matrix3[1][1] = self.matrix2[1][1]
            self.matrix3[1][2] = self.matrix2[1][2]
            self.matrix3[2][0] = self.matrix2[2][0]
            self.matrix3[2][1] = self.matrix2[2][1]
            self.matrix3[2][2] = self.matrix2[2][2]
            self.flag = 2
        else:
            print("already filled!!")
    
    def resetprogram(self):
        self.flag = 0
        self.allzero()
    def addmat(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                self.demomatrix[i][j] = self.matrix1[i][j] + self.matrix2[i][j]
                j = j + 1
            i = i + 1
        self.printmat()

    def submat(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                self.demomatrix[i][j] = self.matrix1[i][j] - self.matrix2[i][j]
                j = j + 1
            i = i + 1
        self.printmat()

    def mulmat(self):
        i = 0
        summ = 0
        while(i<3):
            j = 0
            while(j<3):
                k = 0
                while(k<3):
                    self.demomatrix[i][j] += self.matrix1[i][k] * self.matrix2[k][j]
                    k = k + 1
                j = j + 1
            i = i + 1
        self.printmat()
    def printmat(self):
        self.val1.setText(str(self.demomatrix[0][0]))
        self.val2.setText(str(self.demomatrix[0][1]))
        self.val3.setText(str(self.demomatrix[0][2]))
        self.val4.setText(str(self.demomatrix[1][0]))
        self.val5.setText(str(self.demomatrix[1][1]))
        self.val6.setText(str(self.demomatrix[1][2]))
        self.val7.setText(str(self.demomatrix[2][0]))
        self.val8.setText(str(self.demomatrix[2][1]))
        self.val9.setText(str(self.demomatrix[2][2]))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Edu()
    sys.exit(App.exec())        
