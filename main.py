import sys
import io

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyPillow(QMainWindow):
    def __init__(self):
        self.size = 0
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.button_clicked)

    def paintEvent(self, event):
        p = QPainter(self)
        if self.size != 0:
            p.setPen(QColor(255, 255, 0))
            p.setBrush(QColor(255, 255, 0))
            p.drawEllipse(100, 100, self.size, self.size)
        else:
            pass

    def button_clicked(self):
        self.size = randint(1, 1000)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
