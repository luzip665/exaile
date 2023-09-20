from xl import event, settings
from xl.nls import gettext as _
from xlgui.panel.collection import Order

from . import extendedcollectionorders_prefs
import json

class ExtendedCollectionOrders:
    """
    Plugin adds some buttons on the bottom line of the playlists grid to
    change some settings quickly
    """

    collection_panel = None
    last_active_view = None
    custom_orders = []

    def enable(self, exaile):
        """
        Called on startup of exaile
        """
        self.exaile = exaile
        self.last_active_view = settings.get_option('gui/collection_active_view')
        event.add_callback(self._on_option_update, 'eco_option_set')

        pass

    def _on_option_update(self, event_name, event_source, option):
        self.populate_orders()
        pass

    def disable(self, exaile):
        pass

    def on_gui_loaded(self):
        """
        Called when the gui is loaded
        Before that there is no panel
        """
        self.populate_orders()

    def populate_orders(self):
        setting = settings.get_option('eco/orders', None)
        if setting is None:
            return

        self.collection_panel = self.exaile.gui.panel_notebook.panels['collection'].panel

        for order in self.custom_orders:
            self.collection_panel.orders.remove(order)
        self.custom_orders = []

        orders = json.loads(setting)

        for order in orders:
            levels = order['levels'].split(',')
            display = order['display'].split(',')

            final_sorting = display
            final_display = '$' + ' - $'.join(display)

            final = [final_sorting, final_display, final_sorting]
            levels.append(final)
            lvls = tuple(levels)

            new_order = Order(order['name'], lvls)
            self.collection_panel.orders.append(new_order)
            self.custom_orders.append(new_order)

        # if settings.get_option('extendedcollectionorders/eco1', False) or True:
        #     new_order = Order(_("Genre - Artist - By Date"),
        #       (
        #           'genre', #Tree Level 1
        #           'artist', # Tree Level 2
        #           (
        #               ('date', 'title'), # Sorting
        #               "$date - $title", # Track display
        #               ("title", 'date'), # Search fields
        #            )
        #       )
        #     )
        #     self.collection_panel.orders.append(new_order)
        #
        # if settings.get_option('extendedcollectionorders/eco2', False) or True:
        #     new_order = Order("Artist - Genre - By Date",
        #       (
        #           (('artist', 'album'), "$artist - $album", ("album",)), # Tree Level 1
        #           'genre', # Tree Level 2
        #           (
        #               ('date', 'title'), # Sorting
        #               "$date - $title", # Track display
        #               ("title", 'date'), # Search fields
        #            )
        #       )
        #     )
        #     self.collection_panel.orders.append(new_order)
        #
        # if settings.get_option('extendedcollectionorders/eco3', False) or True:
        #     new_order = Order(_("Artist - Track - By Track title"),
        #                       (
        #                           'artist',  # Tree Level 1
        #                           (
        #                               ('title', 'title'),  # Sorting
        #                               "$title",  # Track display
        #                               ("title", 'date'),  # Search fields
        #                           )
        #                       )
        #                       )
        #     self.collection_panel.orders.append(new_order)

        self.collection_panel.repopulate_choices()
        settings.set_option('gui/collection_active_view', self.last_active_view)

    def on_exaile_loaded(self):
        self.collection_panel.repopulate_choices()
        pass

    def get_preferences_pane(self):
        return extendedcollectionorders_prefs

plugin_class = ExtendedCollectionOrders
