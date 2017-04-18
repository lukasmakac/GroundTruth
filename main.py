__author__ = 'Lukas'

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from modules.Handler import Handler

NAME = "Ground Truth Maker 1.0"

if __name__ == '__main__':

    builder = Gtk.Builder()
    builder.add_from_file("design/design.glade")
    builder.connect_signals(Handler(builder))

    Gtk.main()

