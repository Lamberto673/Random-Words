import sys
import time
import datetime
import requests
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel, 
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QGridLayout, 
                             QFrame)
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap

class clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QLabel('0, 0, 0, 0')
        self.location = QLabel('Yogyakarta', self)
        self.temp = QLabel("temp", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")

        # Create a vertical layout for the main window
        vbox = QVBoxLayout()
        
        # Create a horizontal layout for time and temperature
        hbox = QHBoxLayout()
        hbox.addWidget(self.time)
        hbox.addWidget(self.temp)

        # Add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)
        vbox.addWidget(self.location)

        self.setLayout(vbox)

        # Align the labels
        self.time.setAlignment(Qt.AlignCenter)
        self.location.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        # frame = QFrame(self)
        # Set the style for the labels
        # label = QLabel(self)
        # pixmap = QPixmap("Clock/1868e0a1-80d5-40d5-8c50-7ed39a7c4cf1.jpeg")
        # pixmap.setDevicePixelRatio(2.0)
        # label.setPixmap(pixmap)
        self.time.setObjectName("Time")
        self.location.setObjectName("Location")
        self.temp.setObjectName("Temp")
        self.setStyleSheet(""" 
                           
                           }
                            QLabel#Time, QLabel#Location, QLabel#Temp {
                                font-family: helvetica;
                                font-size: 48px;
                                background-color: #faebd7; /* Inner light color */
                                border: 8px solid #8b4513; /* Dark brown */
                                padding: 6px;
                                border-top: 16px solid #ff8c00; /* Orange top */
                                border-bottom: 8px solid #a0522d; /* Saddle brown bottom */
                                border-left: 8px solid #cd853f; /* Peru left */
                                border-right: 8px solid #cd853f; /* Peru right */
                            }

                            
                           """)
        self.format_time()
        self.curr_Location()
        self.backgroundimage()

    def backgroundimage(self):
        self.setStyleSheet(
            """
            QWidget {
                background-image: url('Clock/Image.jpeg');
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }

            QLabel#Time, QLabel#Location, QLabel#Temp {
                font-family: helvetica;
                font-size: 48px;
                background-color: #faebd7;
                border: 8px solid #8b4513;
                padding: 6px;
                border-top: 16px solid #ff8c00;
                border-bottom: 8px solid #a0522d;
                border-left: 8px solid #cd853f;
                border-right: 8px solid #cd853f;
            }
            """
        )


        
    def format_time(self):
        self.time.setText(QTime.currentTime().toString('HH:mm:ss'))
        QTimer.singleShot(1000, self.format_time)
    def displaytime(self):
        self.format_time.show()
    def curr_Location(self):
        API = "d0a52ec4f5bba78cb06f0d5f6942552b"
        city = "Yogyakarta"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature_k = data['main']['temp']
        temperature_C = temperature_k - 273

        self.temp.setText(f"{temperature_C:.0f}°C")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    Project2 = clock()
    Project2.show()
    sys.exit(app.exec_())