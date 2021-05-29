from gi.repository import Gtk
from xl import event, settings
from xl.nls import gettext as _
from xlgui.panel.collection import Order


class ExtendedCollectionOrders:
    """
    Plugin adds some buttons on the bottom line of the playlists grid to
    change some settings quickly
    """

    collection_panel = None
    last_active_view = None

    def enable(self, exaile):
        """
        Called on startup of exaile
        """
        self.exaile = exaile
        self.last_active_view = settings.get_option('gui/collection_active_view')
        pass

    def disable(self, exaile):
        pass

    def on_gui_loaded(self):
        """
        Called when the gui is loaded
        Before that there is no panel
        """
        self.collection_panel = self.exaile.gui.panel_notebook.panels['collection'].panel

        new_order = Order(_("Genre - Artist - Date"),
          (
              'genre', #Tree Level 1
              'artist', # Tree Level 2
              (
                  ('date', 'title'), # Sorting
                  "$date - $title", # Track display
                  ("title", 'date'), # Search fields
               )
          )
        )

        self.collection_panel.orders.append(new_order)
        settings.set_option('gui/collection_active_view', self.last_active_view)

    def on_exaile_loaded(self):
        self.collection_panel.repopulate_choices()
        pass


plugin_class = ExtendedCollectionOrders
