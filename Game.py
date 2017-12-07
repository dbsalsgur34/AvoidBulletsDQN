import sys
import threading

from Bullet import Bullet
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPalette
from PyQt5.QtCore import Qt
from random import randint
from Plain import Plain

ex = None
width = 300
height = 300
plain_width = 10
plain_height = 10
bullet_num = 100
bullets = []
#init
plain = Plain(width, height, plain_width, plain_height)

index = 0
while index < bullet_num:
    x = randint(0, width)
    y = randint(0, height)
    if pow(x-150, 2) + pow(y-150, 2) < 10000:
        continue

    bullets.append(Bullet((x, y), plain, width, height))
    index += 1


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('AvoidBullets')

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.yellow)

        #draw bullets
        for i in range(bullets.__len__()):
            qp.drawPoint(bullets[i].position[0], bullets[i].position[1])

        #draw plain
        qp.setPen(Qt.darkBlue)
        for i in range(int(-plain_width/2), int(plain_width/2)):
            for j in range(int(-plain_height/2), int(plain_height/2)):
                qp.drawPoint(i + plain.position[0], j + plain.position[1])

        qp.end()


def task():
    is_crash = False
    for index in range(bullets.__len__()):
        is_crash = bullets[index].move()
        
    ex.repaint()

    threading.Timer(0.03, task).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    task()
    sys.exit(app.exec_())
