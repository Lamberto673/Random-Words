import sys
import string
import random
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QLineEdit, QDesktopWidget, QSizePolicy
from PyQt5.QtGui import QFont, QPalette, QColor, QBrush, QPixmap, QIcon
from PyQt5.QtCore import Qt, QTime, QTimer

class Encryption(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Encrypting pass", self)
        self.char = QLabel(self)
        self.display = QLineEdit(self)
        self.code = QLineEdit(self)
        self.confirm = QPushButton("Convert", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Encrypt Code")
        self.setWindowIcon(QIcon("basic games/encryption-10.png"))
        self.setFixedSize(310, 420)

        chara = string.ascii_letters + string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits + " "
        self.display.setPlaceholderText("Enter your password")
        self.char.setText(chara)
        self.char.setWordWrap(True)
        self.char.setFixedWidth(280)
        self.char.setFixedHeight(180)
        self.char.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.code.setReadOnly(True)
        self.code.setFixedWidth(280)

        self.confirm.setFixedWidth(280)
        self.display.setFixedWidth(280)
        self.title.setFixedWidth(280)
        Vbox = QVBoxLayout()
        Vbox.setContentsMargins(5, 10, 10, 10)
        Vbox.setSpacing(5)

        self.title.setAlignment(Qt.AlignCenter)
        Vbox.addWidget(self.title, alignment=Qt.AlignTop | Qt.AlignCenter)

        Vbox.addWidget(self.char, alignment=Qt.AlignTop | Qt.AlignCenter)
        Vbox.addWidget(self.code, alignment=Qt.AlignCenter)
        Vbox.addWidget(self.display, alignment=Qt.AlignCenter)
        Vbox.addWidget(self.confirm, alignment=Qt.AlignCenter)

        self.setLayout(Vbox)

        self.display.setObjectName("Display")
        self.char.setObjectName("Char")
        self.code.setObjectName("code")
        # self.title.setObjectName("title")

        self.setStyleSheet("""
            QWidget{
                background-color: rgb(79, 49, 32);               
            }
            QLabel {
                border-radius: 20px;
                border: 5px solid black;
                margin: 10px 0px;
                font-size: 20px;
                padding: 5px;
                background: rgb(112, 51, 18);
                color: rgb(255, 255, 255);
            }
            QLineEdit#Display {
                margin-top: 10px;
                padding: 5px;
                border: 5px solid black;
                font-size: 20px;
                background-color: rgb(122, 111, 105);
            }
            QLineEdit#code {
                margin-top: 10px;
                padding: 5px;
                border: 5px solid black;
                font-size: 20px;
                background-color: rgb(122, 111, 105);
            }              
            QLabel#Char {
                border: 5px solid black;
                font-size: 20px;
                padding: 1px 2px;
            }QPushButton{
                background-color: rgb(179, 165, 21);
                font-size: 20px;
                border: 5px solid black;
                border-radius: 10px;               
            }QPushButton:hover{
                background-color: rgb(219, 202, 20);
                font-size: 20px;
                border: 5px solid black;
                border-radius: 10px;               
            }
        """)
        

        self.confirm.clicked.connect(self.Encrypting)

    def Encrypting(self):
        button = self.display.text()

        chara = string.ascii_letters + string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits + " "
        chara = list(chara)
        code = chara.copy()
        random.shuffle(code)
        result = ""

        for i in button:
            index = chara.index(i)
            result += code[index]
        self.code.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ecnrypt = Encryption()
    Ecnrypt.show()
    sys.exit(app.exec_())