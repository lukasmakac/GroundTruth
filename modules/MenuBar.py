from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenuBar, qApp

__author__ = 'Lukas'

class MenuBar(QMenuBar):

    def __init__(self, parent=None, handler=None):

        super(MenuBar, self).__init__(parent)

        #menu
        self.openAction = QAction('&Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open Image File')
        self.openAction.triggered.connect(handler.onOpenImageFile)

        self.openMultipleFilesAction = QAction('&Open Multiple Files', self)
        self.openMultipleFilesAction.setShortcut('Ctrl+A')
        self.openMultipleFilesAction.setStatusTip('Open multiple Image Files')
        self.openMultipleFilesAction.triggered.connect(handler.onOpenMultipleImageFiles)

        self.openDirAction = QAction('&Open Directory', self)
        self.openDirAction.setShortcut('Ctrl+D')
        self.openDirAction.setStatusTip('Open Image Directory')
        self.openDirAction.triggered.connect(handler.onOpenImageDir)

        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)

        self.fileMenu = self.addMenu('&File')
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.openMultipleFilesAction)
        self.fileMenu.addAction(self.openDirAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)


