import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
import requests
import pygame
import random

class IDK(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Random Word", self)
        self.Bot = QLabel("Computer:", self)
        self.Computer = QLineEdit(self)
        self.Guess = QLabel("Your Guess:", self)
        self.Line = QLineEdit(self)
        self.Generate = QPushButton("Generate", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Random Word Generator")
        self.Line.setReadOnly(False)
        self.Computer.setReadOnly(True)
        self.setFixedSize(500, 400)

        Vbox = QVBoxLayout()
        Vbox.addWidget(self.title)
        Vbox.addWidget(self.Bot)
        Vbox.addWidget(self.Computer)
        Vbox.addWidget(self.Guess)
        Vbox.addWidget(self.Line)
        Vbox.addWidget(self.Generate)

        self.setLayout(Vbox)

        self.title.setAlignment(Qt.AlignCenter)

        self.Computer.setObjectName("Computer")
        self.Line.setObjectName("Line")
        self.Bot.setObjectName("Bot")
        self.Guess.setObjectName("Guess")
        self.title.setObjectName("Title")
        self.setStyleSheet(""" 
                            QWidget{
                            background-color: #805f0e;
                           }
                            QLabel#Title{
                            background-color: #57350c;
                            font-size: 24px;
                            border-radius: 10px;
                            border: 5px solid;
                            margin-bottom: 5px;
                            color: rgb(184, 157, 125);
                           }
                           QLabel#Bot{
                            font-size: 22px;
                            margin-bottom: 0px;
                            width: 10px;
                            height: 10px;
                            color: rgb(36, 21, 3);
                           }
                           QLabel#Guess{
                            font-size: 22px;
                           margin-bottom: 0px;
                           color: rgb(36, 21, 3);
                           }
                           QLineEdit#Line{
                            height: 30px;
                            width: 200px;
                            font-size: 24px;
                            background-color: #9c6e41;
                          
                           }
                           QLineEdit#Computer{
                            height: 30px;
                            width: 200px;
                            font-size: 24px;
                            background-color: #9c6e41;
                           }
                           QPushButton{
                            height: 30px;
                            width: 200px;
                            background-color: #38210a;
                            color: white;
                            font-weight: bold;
                           }

        
        """)
        self.Generate.clicked.connect(self.Random)
    def Random(self):
        num = random.randint(1, 10)
        self.Computer.setText(str(num))

        if self.Line.text() == self.Computer.text():
            sound_file = "basic games/Hidup Jokowi - Sound Effect.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        else:
            self.Line.setText("")
            sound = "basic games/videoplayback.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
    # def Random(self):
    #     Api = "https://random-word-api.vercel.app/api?words=1"

    #     try:
    #         response = requests.get(Api)
    #         response.raise_for_status()
    #         data =  response.json()

    #         self.Line.setText(requests.get("https://random-word-api.vercel.app/api?words=1").json()[0])
    #         self.Computer.setText(data[0])

    #         if self.Line.text() == self.Computer.text():
    #             sound_file = "basic games/Hidup Jokowi - Sound Effect.mp3"
    #             pygame.mixer.init()
    #             pygame.mixer.music.load(sound_file)
    #             pygame.mixer.music.play()

    #     except requests.exceptions.HTTPError:
    #         print("HTTP Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = IDK()
    project.show()
    sys.exit(app.exec_())