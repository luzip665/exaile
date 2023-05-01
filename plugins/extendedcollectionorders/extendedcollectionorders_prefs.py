
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
        {'name': "Artist - Genre - By Date", 'levels': ['$artist', '$genre', '$date - $title']},
        {'name': "Genre - Artist - By Date", 'levels': ['$genre', '$artist', '$date - $title']}
    ]

    i = 0
    for order in custom_orders:
        line = build_order_line(order['name'], order['levels'], i)
        grid.attach(line, 0, i, 1, 1)
        i += 1


def build_order_line(name, levels, number):

    def insert_input(name: str, label_str: str, row: int):
        label = Gtk.Label()
        label.set_text(label_str)
        line_grid.attach(label, 0, row, 1, 1)

        input = Gtk.Entry()  # comma list
        input.set_text(name)
        line_grid.attach(input, 1, row, 1, 1)

    line_grid = Gtk.Grid()

    insert_input(name, 'name', 0)
    # insert_input('tree_levels', 'tree_levels', 1)
    # insert_input('sorting', 'tree_levels', 1)
    # insert_input('tree_levels', 'tree_levels', 1)
    # insert_input('tree_levels', 'tree_levels', 1)

    sorting = Gtk.Entry() #comma list
    track_display = Gtk.Entry #like $date - $title
    search_fields = Gtk.Entry #comma list

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