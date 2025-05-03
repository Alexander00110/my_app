from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.hello_text = QLabel( txt_hello )
        self.instruction = QLabel( txt_instruction )
        self.button = QPushButton( txt_next,self )
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text,alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction,alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.button,alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def connects(self): 
        self.button.clicked.connect(self.next_click)
    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()