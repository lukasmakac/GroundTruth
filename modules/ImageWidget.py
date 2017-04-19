from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import QRect, QCoreApplication, QRectF, Qt
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

    def display_image(self, path):
        self.scene.clear()
        img = Image.open(path)
        w, h = img.size
        pixMap = QPixmap(path)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.scene.update()
