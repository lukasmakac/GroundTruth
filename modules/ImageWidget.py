from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import QRect, QCoreApplication, QRectF
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout
import time

__author__ = 'Lukas'
class ImageWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setGeometry(QRect(0, 0, 800, 600))

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

    def do_test(self):
        img = Image.open('image.png')
        for i in range(1, 8):
            self.display_image(img)
            QCoreApplication.processEvents()  # let Qt do his work
            time.sleep(0.5)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.scene.update()
