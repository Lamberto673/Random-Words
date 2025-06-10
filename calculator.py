import sys
from PyQt5.QtWidgets import QWidget, QApplication, QBoxLayout, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QComboBox, QSpinBox, QDoubleSpinBox, QLineEdit
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QThread, QMutex, QWaitCondition, QTime, QTimer, Qt 
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen, QTransform, QFont, QFontDatabase, QPixmap, QIcon

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.display = QLineEdit()
        self.delete = QPushButton("C", self)
        self.title = QLabel("Calculator", self)
        self.back = QPushButton("<-")
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("basic games/profilepic_calc-removebg-preview.png"))

        self.setFixedSize(300, 450)

        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(False)
        self.display.setFixedHeight(50)

        layout = QVBoxLayout()
        # layout.addWidget(self.delete)
        layout.addWidget(self.title)
        self.title.setAlignment(Qt.AlignCenter)

        self.delete.setObjectName("C")
        self.back.setObjectName("Back")

        

        self.setStyleSheet("""
                        QWidget{
                           background-color: rgb(41, 38, 30);
                        }
                        QLabel {
                            border: 10px solid black;
                            background-color: white;
                            font-size: 30px;
                        }
    
                        QLineEdit {
                            font-size: 30px;
                        }
                        QPushButton{
                            padding: 10px 75px;
                            border-radius: 20px;
                            border: 3px solid;
                            background-color: rgb(173, 173, 42)
                            
                        }
                        QLineEdit{
                            color: white;   
                        }
                        QPushButton#C{
                            padding: 50px 75px;
                            font-weight: normal;
                            font-size: 20px;
                            background-color: rgb(224, 178, 61);
                        }
                        QPushButton#Back{
                            padding: 50px 75px;
                            font-weight: normal;
                            font-size: 20px;
                            background-color: rgb(224, 178, 61);
                        }
                        QPushButton#Back:hover{
                           background-color: rgb(255, 200, 59);   
                        }
                        QPushButton#C:hover{
                            background-color: rgb(255, 200, 59);   
                        }
                        QPushButton:hover{
                           background-color: rgb(204, 204, 57);
                           
                        }
                           
                    """)

        
        font_id = QFontDatabase.addApplicationFont("basic games/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 30)
        font_buttons = QFont(font_family, 20, 10)
        self.title.setFont(my_font)

        layout.addWidget(self.display)

        self.display.setFont(my_font)

        

        grid = QGridLayout()
        buttons = [
            ('(', 0, 0), (')', 0, 1), ('%', 0, 2), ('√', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(font_buttons)
            button.setFixedSize(50, 50)
            button.clicked.connect(self.on_click)
            grid.addWidget(button, row, col)
            

        layout.addWidget(self.delete)
        self.delete.setFixedSize(280, 30)

        self.delete.clicked.connect(self.delete_clicked)

        layout.addLayout(grid)
        self.setLayout(layout)

        layout.addWidget(self.back)
        self.back.setFixedSize(280, 30)

        self.back.clicked.connect(self.back_clicked)
        
    def delete_clicked(self):
        self.display.clear()
       

    def back_clicked(self):
        current = self.display.text()
        self.display.setText(current[:-1])

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                express = self.display.text()
                expression = express.replace("%", "/100").replace("√", "** 0.5")
                result = str(eval(expression))
                self.display.setText(result)
                
                
            except:
                self.display.setText("Error")

        elif text == "%":
            curr = self.display.text()
            self.display.setText(curr + "%")

        elif text == "√":
            curre = self.display.text()
            self.display.setText(curre + "√")
            
                    
        else:
            current = self.display.text()
            self.display.setText(current+text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Project3 = calculator()
    Project3.show()
    sys.exit(app.exec_())