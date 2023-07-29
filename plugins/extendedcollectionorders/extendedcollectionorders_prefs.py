
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
        line = build_order_line(order['name'], order['levels'], order['display'], order['sorting'], i)
        grid.attach(line, 0, i, 1, 1)
        i += 1


def build_order_line(name, levels, display, sorting, number):

    def insert_input(name: str, label_str: str, row: int):
        label = Gtk.Label()
        label.set_text(label_str)
        line_grid.attach(label, 0, row, 1, 1)

        input = Gtk.Entry()  # comma list
        input.set_text(name)

        line_grid.attach(input, 1, row, 1, 1)

    line_grid = Gtk.Grid()

    insert_input(name, 'name', 0)
    insert_input(levels, 'tree_levels', 1)
    insert_input(sorting, 'sorting', 2)
    insert_input(display, 'display', 3)

    return line_grid

class GenreArtistDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco1'

class ArtistGenreDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco2'


class ArtistTrackTrack(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco3'