from PyQt5.QtCore import QCoreApplication

from modules.ImageWidget import ImageWidget
from modules.MenuBar import MenuBar

__author__ = 'Lukas Maruniak imaruniak@fit.vutbr.cz'

NAME = "Ground Truth Maker"
INITIAL_DIR = "c:/Users/Lukas/FIT/1DVI/DIZ/resources/Sitnice/MartinD/"

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.statusBar()

        self.setMenuBar(MenuBar(self))

        #Content

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.imageWidget = ImageWidget()

        self.layout.addWidget(self.imageWidget)

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

        self.imageWidget.display_image(imageFile)
        QCoreApplication.processEvents()  # let Qt do his work

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
