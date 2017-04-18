__author__ = 'Lukas Maruniak imaruniak@fit.vutbr.cz'

NAME = "Ground Truth Maker"
INITIAL_DIR = "c:/Users/Lukas/FIT/1DVI/DIZ/resources/Sitnice/MartinD/"


import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog
from PyQt5.QtGui import QIcon

from modules.Handler import Handler

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Image File')
        openAction.triggered.connect(self.onOpenImageFile)
        
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
        fileMenu.addAction(openDirAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle(NAME)
        self.show()

    def onOpenImageFile(self):
        print("Open Image")

        imageFileDialog = QFileDialog();
        fname = imageFileDialog.getOpenFileName(self, 'Open file',INITIAL_DIR, self.tr("JPEG (*.jpg *.jpeg);; PNG (*.png);; BMP (*.bmp)"));

        if fname[0]:
            print(fname[0])

    def onOpenImageDir(self):
        print("Open Image Directory")

        imageFileDialog = QFileDialog();
        fname = imageFileDialog.getExistingDirectory(self, 'Open Directory', INITIAL_DIR);

        if fname:
            print(fname)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())