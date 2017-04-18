from gi.repository import GdkPixbuf

__author__ = 'Lukas'

import cairo

from gi.repository import GdkPixbuf
from PIL import Image

class ImageProcesser:

    @staticmethod
    def drawMesh(self, context):
        """Draw something into the buffer"""
        if context is not None:
            # Create cairo context with double buffer as is DESTINATION
            cc = cairo.Context(context)

            # Scale to device coordenates
            cc.scale(context.get_width(), context.get_height())

            # Draw a white background
            cc.set_source_rgb(1, 1, 1)

            # Draw something, in this case a matrix


            # Flush drawing actions
            context.flush()

        else:
            print('Invalid double buffer')


    @staticmethod
    def processImage(file, width = 800, height=600):

        try:
            im = Image.open(file.get_path())

            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(file.get_path(), width, height)
            # pixbuf = pixbuf.scale_simple(480, 400, Gdk.INTERP_BILINEAR)

            # arr = array.array('B', im.tobytes())
            # width, height = im.size
            # return GdkPixbuf.Pixbuf.new_from_data(arr, GdkPixbuf.Colorspace.RGB, True, 8, width, height, width * 4)

            return pixbuf

        except IOError as e:
            print("Error: "+e.message)