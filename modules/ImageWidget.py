from PyQt5.QtCore import QRect, QRectF, Qt, QPoint, QLineF, QSizeF
from PyQt5.QtGui import QPixmap, QPen, QImage, QPicture, QPainter
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QVBoxLayout, QGraphicsPixmapItem
import cv2
import math

__author__ = 'Lukas'
class ImageWidget(QWidget):

    viewportWidth = 800
    viewportHeight = 600

    cvImage = None
    img = None
    pixMap = None

    gridSize = 10
    points = []

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setGeometry(QRect(0, 0, self.viewportWidth, self.viewportHeight))

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

    def paintEvent(self, event):
        if(self.img is not None):
            self.scene.clear()
            width = self.img.width()
            height = self.img.height()
            pixMap = QPixmap.fromImage(self.img)

            #draw grid
            #self.drawGrid(pixMap, width, height, self.gridSize)

            #mark spots
            if(self.points):
                for point in self.points:
                    self.markSpot(pixMap, point)

            self.scene.mousePressEvent = self.onSceneClick
            self.scene.addPixmap(pixMap)

            #self.view.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatioByExpanding)

            #draw vertical lines
            for i in range(0, width, self.gridSize):
                self.scene.addLine(QLineF(QPoint(i, 0), QPoint(i, height)), QPen(Qt.black))

            #draw horizontal lines
            for i in range(0, height, self.gridSize):
                self.scene.addLine(QLineF(QPoint(0, i), QPoint(width, i)), QPen(Qt.black))

            self.view.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatio)

            self.scene.update()


    # def mousePressEvent(self, QMouseEvent):
    #     #pos of view
    #     point = QMouseEvent.pos()
    #
    #     aspectRatioX = self.img.width()/self.view.width()
    #     aspectRatioY = self.img.height()/self.view.height()
    #
    #     #compute coords for img (viewport can be smaller/higher than original image)
    #     x = math.floor(point.x()*aspectRatioX / self.gridSize)*self.gridSize
    #     y = math.floor(point.y()*aspectRatioY / self.gridSize)*self.gridSize
    #
    #     self.points.append(QPoint(x, y))
    #
    #     print("x: {}, y: {}".format(x, y))
    #
    #     self.view.repaint()

    def onSceneClick(self, QGraphicsSceneMouseEvent):
        #pos of view
        point = QGraphicsSceneMouseEvent.scenePos()

        #compute coords for img (viewport can be smaller/higher than original image)
        x = math.floor(point.x()/ self.gridSize)*self.gridSize
        y = math.floor(point.y()/ self.gridSize)*self.gridSize

        self.points.append(QPoint(x, y))

        print("x: {}, y: {}".format(x, y))

        self.view.repaint()

    def markSpot(self, paintDevice, point):
        rect = QRectF(point.x(), point.y(), self.gridSize, self.gridSize)

        painter = QPainter()
        painter.begin(paintDevice)
        painter.setOpacity(.5)
        painter.fillRect(rect, Qt.white)
        painter.end()

        self.scene.addRect(rect, Qt.green)

    def drawGrid(self, paintDevice, width, height, gridSize):
        painter = QPainter()
        painter.begin(paintDevice)
        painter.setPen(QPen(Qt.black))

        #draw vertical lines
        for i in range(0, width, gridSize):
            painter.drawLine(QLineF(QPoint(i, 0), QPoint(i, height)))

        #draw horizontal lines
        for i in range(0, height, gridSize):
            painter.drawLine(QLineF(QPoint(0, i), QPoint(width, i)))

        painter.end()




