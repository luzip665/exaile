from gi.repository import Gtk
from xl import event, settings
from xl.nls import gettext as _
from xlgui.panel.collection import Order

from . import extendedcollectionorders_prefs

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
        event.add_callback(self._on_option_activate, 'extendedcollectionorders_option_set')

        pass

    def _on_option_activate(self, event_name, event_source, option):
        self.add_orders()
        pass

    def disable(self, exaile):
        pass

    def on_gui_loaded(self):
        """
        Called when the gui is loaded
        Before that there is no panel
        """
        self.add_orders()

    def add_orders(self):
        self.collection_panel = self.exaile.gui.panel_notebook.panels['collection'].panel

        if settings.get_option('extendedcollectionorders/eco1', False):
            new_order = Order(_("Genre - Artist - By Date"),
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

        if settings.get_option('extendedcollectionorders/eco2', False):
            new_order = Order(_("Artist - Genre - By Date"),
              (
                  'artist', # Tree Level 1
                  'genre', # Tree Level 2
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

    def get_preferences_pane(self):
        return extendedcollectionorders_prefs

plugin_class = ExtendedCollectionOrders
