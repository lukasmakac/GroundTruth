import array

import gi
import cairo
import math

from modules.Constants import Constants
from modules.ImageProcesser import ImageProcesser as IP

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Handler:

    imageFile = None

    def __init__(self, builder):
        self.double_buffer = None

        self.builder = builder
        self.window = builder.get_object("main_window")

        self.gtkImage = self.builder.get_object(Constants.Builder.IMAGE)
        self.gtkImageFrame = self.builder.get_object(Constants.Builder.IMAGE_FRAME)

        self.drawing_area = self.builder.get_object(Constants.Builder.DRAW_AREA)
        # self.drawing_area.connect('configure-event', self.onConfigure)
        self.drawing_area.connect('draw', self.onDraw)

        self.window.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onOpenFileMenuItem(self, *args):
        self.fileChooserDialog = Gtk.FileChooserDialog("Pick a file", self.window,
                                            Gtk.FileChooserAction.OPEN,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                            Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        self.fileChooserDialog.set_local_only(False)
        self.fileChooserDialog.set_modal(True)
        self.fileChooserDialog.connect("response", self.onOpenFileMenuItemDialogConfirm)

        self.fileChooserDialog.show()

    def onOpenFileMenuItemDialogConfirm(self, dialog, response_id):
        open_dialog = dialog
        if response_id == Gtk.ResponseType.ACCEPT:         # if response is "ACCEPT" (the button "Open" has been clicked)

            self.imageFile = open_dialog.get_file()

            print("Opened: " + open_dialog.get_filename())
        elif response_id == Gtk.ResponseType.CANCEL:
            print("cancelled: FileChooserAction.OPEN")

        dialog.destroy() # destroy the FileChooserDialog

    def onDraw(self, drawing_area, cr):

        if (self.imageFile is not None):
            windowWidth = self.window.get_allocation().width
            windowHeight = self.window.get_allocation().height

            pixBuf = IP.processImage(self.imageFile, windowWidth, windowHeight)

            cr.paint()
        else:
            print('Invalid Image')

    def onQuitMenuItem(self, *args):
        Gtk.main_quit(*args)


