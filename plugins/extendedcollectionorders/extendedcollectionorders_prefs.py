
import os
from gi.repository import Gtk, GObject

from xlgui.preferences import widgets
from xl.nls import gettext as _


name = _('Extended Collections')
basedir = os.path.dirname(os.path.realpath(__file__))
ui = os.path.join(basedir, "eco_pane.ui")

def init(dialog, builder):
    grid = builder.get_object('preferences_pane')



    custom_orders = [
        {'name': "Artist - Genre - By Date", 'levels': 'artist, genre', 'display': '$date - $title', 'sorting': 'date, title'},
        {'name': "Genre - Artist - By Date", 'levels': 'genre, artist', 'display': '$date - $title', 'sorting': 'date, title'}
    ]

    i = 0
    for order in custom_orders:
        line = build_order_line(order, i)
        grid.attach(line, 0, i, 1, 1)
        i += 1


def build_order_line(order, number):

    def insert_input(name: str, label_str: str, row: int, order):
        label = Gtk.Label()
        label.set_text(label_str)
        line_grid.attach(label, 0, row, 1, 1)

        input = Gtk.Button()  # comma list
        input.set_label(name)

        line_grid.attach(input, 1, row, 1, 1)

        input.connect("clicked", on_open_clicked, order)

    def on_open_clicked(w, order):
        win = order_line_window(order)
        win.show_all()

    line_grid = Gtk.Grid()

    insert_input(name, 'name', 0, order)

    return line_grid


class order_line_window(Gtk.Window):
    def __init__(self, order):
        self.order = order

        super().__init__(title="Order Line")
        self._layout()
        self._connect()
        self._fill()

    def _layout(self):
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.input_name = self._add_input('Name', self.order['name'], 0)
        self.input_tree_levels = self._add_input('tree levels', self.order['levels'], 1)
        self.input_display = self._add_input('Display', self.order['display'], 2)
        self.input_sorting = self._add_input('Sorting', self.order['sorting'], 3)

    def _add_input(self, label, value, position):

        input_url_label = Gtk.Label()
        input_url_label.set_text(label)
        self.grid.attach(input_url_label, 0, position, 1, 1)

        input_url = Gtk.Entry()
        input_url.set_text(value)
        self.grid.attach_next_to(input_url, input_url_label, Gtk.PositionType.RIGHT, 3, 1)

        return input_url

    def _connect(self):
        pass
        # self.close_button.connect("clicked", self._on_button_close_clicked)
        # self.save_button.connect("clicked", self._on_button_save_clicked)
        # self.connect("key-press-event", self._key_press_event)

    def _fill(self):
        pass
        # self.input_url.set_text(self._credentials.get_crm_url())
        # self.input_login.set_text(self._credentials.get_login())


class GenreArtistDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco1'

class ArtistGenreDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco2'


class ArtistTrackTrack(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco3'