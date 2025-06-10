import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
import pygame
from background import change_styles

class Timerr(QWidget):
    def __init__(self):
        super().__init__()
        self.Title = QLabel("TIMER", self)
        self.curr_time = QLabel("00:00:00", self)  # Corrected format
        self.Timeset = QLineEdit(self)
        self.Timeset.setPlaceholderText("HH:MM:SS")
        self.button = QPushButton("Start", self)
        self.timer_running = False
        self.target_time = None
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("TIMER")

        Vbox = QVBoxLayout()
        Vbox.addWidget(self.Title)
        Vbox.addWidget(self.curr_time)
        Vbox.addWidget(self.Timeset)
        Vbox.addWidget(self.button)

        self.setLayout(Vbox)
        self.Title.setAlignment(Qt.AlignCenter)
        self.curr_time.setAlignment(Qt.AlignCenter)
        self.Timeset.setAlignment(Qt.AlignCenter)

        self.Timeset.setObjectName('Timeset')
        self.curr_time.setObjectName('Curr_Time')

        self.setStyleSheet("""
           
         
            QLabel, QLineEdit {
                font-size: 50px;
                border: 5px solid black;
                background-color: #f9e9a9;
                border-top: 16px solid #ff8c00;
                border-bottom: 10px solid #a0522d;
                border-left: 8px solid #cd853f;
                border-right: 8px solid #cd853f;
            }
                QLineEdit#Timeset{
                    font-size: 30 px;
            }
                QLabel#Curr_Time{
                    font-size: 100 px;
            }
            QPushButton {
                font-size: 40px;
                background-color: #f9e9a9;
                border-top: 16px solid #ff8c00;
                border-bottom: 10px solid #a0522d;
                border-left: 8px solid #cd853f;
                border-right: 8px solid #cd853f;
            }
                
        """)
        font_id = QFontDatabase.addApplicationFont('Clock/DS-DIGIT.TTF')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 500) 
        self.curr_time.setFont(my_font) 
        self.Timeset.setFont(my_font)
        self.button.clicked.connect(self.Time_set)

        self.current_timer = QTimer(self)
        self.current_timer.timeout.connect(self.Time_curr)
        self.current_timer.start(1000)
    

        pygame.mixer.init()


    def Time_curr(self):
        current_time = QTime.currentTime()
        self.curr_time.setText(current_time.toString('HH:mm:ss'))
        
        if self.timer_running and self.target_time.secsTo(current_time) == 0:
            self.Timeset.setText("SET")
            self.play_sound()  
            self.timer_running = False

    def Time_set(self):
        time_str = self.Timeset.text()
        try:
            self.target_time = QTime.fromString(time_str, 'HH:mm:ss')
            if self.target_time.isValid():
                self.timer_running = True
                self.Timeset.setText(time_str)  
            else:
                self.curr_time.setText("Invalid Time Format")
        except Exception as e:
            self.curr_time.setText("Error: " + str(e))

    def play_sound(self):
        sound_file = 'Clock/Pay money To my Pain - Rain (Music Video).mp3'
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            self.curr_time.setText("Error playing sound: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Project2 = Timerr()
    Project2.show()
    sys.exit(app.exec_())



