import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QPen, QPainter, QColor, QPolygon, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint
from ui_file import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)
        self.r = -1
        self.x, self.y = 0, 0
        self.clckd = False
        self.color = QColor(255, 255, 0)

    def button_click(self):
        self.r = randint(40, self.width() // 2)
        self.x = randint(10, self.width())
        self.y = randint(10, self.height())
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    def paintEvent(self, event):
        if self.r != -1:
            h = QPainter()
            h.begin(self)

            self.drawC(h)
            h.end()

    def drawC(self, h):
        h.setBrush(self.color)
        h.drawEllipse(QPoint(self.x, self.y), self.r, self.r)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mv = MainWindow()
    mv.show()
    sys.exit(app.exec_())
