from PyQt5.QtCore import QRect
import cv2

__author__ = 'Lukas Maruniak imaruniak@fit.vutbr.cz'

NAME = "Ground Truth Maker"
INITIAL_DIR = "c:/Users/Lukas/FIT/1DVI/DIZ/resources/Sitnice/MartinD/"

import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QVBoxLayout, QWidget, QLabel, \
    QGraphicsView
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QImage

from modules.Handler import Handler

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        #menu

        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Image File')
        openAction.triggered.connect(self.onOpenImageFile)

        openMultipleFilesAction = QAction('&Open Multiple Files', self)
        openMultipleFilesAction.setShortcut('Ctrl+A')
        openMultipleFilesAction.setStatusTip('Open multiple Image Files')
        openMultipleFilesAction.triggered.connect(self.onOpenMultipleImageFiles)

        openDirAction = QAction('&Open Directory', self)
        openDirAction.setShortcut('Ctrl+D')
        openDirAction.setStatusTip('Open Image Directory')
        openDirAction.triggered.connect(self.onOpenImageDir)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(openMultipleFilesAction)
        fileMenu.addAction(openDirAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        #Content

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.label = QLabel()

        self.layout.addWidget(self.label)

        self.centralWidget.setLayout(self.layout)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle(NAME)
        self.show()

    def onOpenImageFile(self):
        print("Open Image")

        imageFileDialog = QFileDialog()
        fname = imageFileDialog.getOpenFileName(self, 'Open file', INITIAL_DIR,
                                                self.tr("JPEG (*.jpg *.jpeg);; PNG (*.png);; BMP (*.bmp)"))

        if fname[0]:
            print(fname[0])
            self.paintImage(fname[0])

    def onOpenMultipleImageFiles(self):
        print("Select multiple Image Files")

        imageFileDialog = QFileDialog()
        fname = imageFileDialog.getOpenFileNames(self, 'Open file', INITIAL_DIR,
                                                 self.tr("JPEG (*.jpg *.jpeg);; PNG (*.png);; BMP (*.bmp)"))

        if fname:
            for name in fname:
                print(name, sep=", ")

    def onOpenImageDir(self):
        print("Open Image Directory")

        imageFileDialog = QFileDialog()
        fname = imageFileDialog.getExistingDirectory(self, 'Open Directory', INITIAL_DIR)

        if fname:
            print(fname)


    def paintImage(self, imageFile):
        # self.cvImage = cv2.imread(r"126.JPG")
        # height, width, byteValue = self.cvImage.shape
        # byteValue = byteValue * width
        #
        # cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        #
        # self.mQImage = QImage(self.cvImage, width, height, byteValue, QImage.Format_RGB888)

        img = imageFile
        pixmap = QPixmap(img)

        # painter = QPainter()
        # painter.begin(pixmap)
        # painter.drawImage(0, 0, self.mQImage)
        # painter.end()

        self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
