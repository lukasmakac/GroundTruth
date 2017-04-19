from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import QRect, QCoreApplication, QRectF, Qt, QLine, QPoint, QLineF
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout
import time
import cv2

__author__ = 'Lukas'
class ImageWidget(QWidget):

    cvImage = None
    img = None
    pixMap = None

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setGeometry(QRect(0, 0, 800, 600))

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

    def display_image(self, path):
        self.cvImage = cv2.imread(path)
        height, width, byteValue = self.cvImage.shape
        byteValue = byteValue * width
        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)

        self.img = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)

        self.scene.update()

    def paintEvent(self, QPaintEvent):
        grid_size = 10
        if(self.img is not None):
            self.scene.clear()
            width = self.img.width()
            height = self.img.height()

            pixMap = QPixmap.fromImage(self.img)
            self.scene.addPixmap(pixMap)

            # self.view.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatio)
            self.view.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatioByExpanding)

            #draw vertical lines
            for i in range(0, width, grid_size):
                self.scene.addLine(QLineF(QPoint(i, 0), QPoint(i, height)), QPen(Qt.black))

            #draw horizontal lines
            for i in range(0, height, grid_size):
                self.scene.addLine(QLineF(QPoint(0, i), QPoint(width, i)), QPen(Qt.black))

            self.scene.update()




