from gi.repository import Gtk
from xl import event, settings
from xl.nls import gettext as _
from xlgui.collection import *


class ExtendedCollectionOrders:
    """
    Plugin adds some buttons on the bottom line of the playlists grid to
    change some settings quickly
    """

    def enable(self, exaile):
        """
        Called on startup of exaile
        """
        self.exaile = exaile
        pass

    def disable(self, exaile):
        pass

    def on_gui_loaded(self):
        """
        Called when the gui is loaded
        Before that there is no status bar
        """
        target = self.exaile.gui.panel_notebook.panels['collection'].panel.orders
        pass

    def on_exaile_loaded(self):
        pass


plugin_class = ExtendedCollectionOrders
