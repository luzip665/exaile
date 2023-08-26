
import os
from gi.repository import Gtk, GObject, Gdk

from xlgui.preferences import widgets
from xl.nls import gettext as _
from xl import settings
from xlgui.widgets import common


name = _('Extended Collections')
basedir = os.path.dirname(os.path.realpath(__file__))
ui = os.path.join(basedir, "eco_pane.ui")

def init(dialog, builder):
    prefs = eco_prefs(builder)


class eco_prefs():

    def __init__(self, builder):
        self.builder = builder

        self.grid = self.builder.get_object('preferences_pane')
        self.model = self.builder.get_object('model')
        self.list = self.builder.get_object('orders_tree')

        """Show trash can"""
        remove_cellrenderer = common.ClickableCellRendererPixbuf()
        remove_cellrenderer.props.icon_name = 'edit-delete'
        remove_cellrenderer.props.xalign = 1
        remove_cellrenderer.connect('clicked', self._on_remove_cellrenderer_clicked)

        name_column = builder.get_object('name_column')
        name_column.pack_start(remove_cellrenderer, True)
        # name_column.add_attribute(remove_cellrenderer, 'visible', 8)

        self.list.connect("row-activated", self._on_row_activated)

        self.known_lines = []
        # self.custom_orders = settings.get_option('custom_orders', [])

        self.custom_orders = [
            {'name': "Artist - Genre - By Date", 'levels': 'artist, genre', 'display': '$date - $title',
             'sorting': 'date, title'},
            {'name': "Genre - Artist - By Date", 'levels': 'genre, artist', 'display': '$date - $title',
             'sorting': 'date, title'}
        ]

        self.list.set_model(None)
        self.model.clear()


        i = 0
        for order in self.custom_orders:

            it = self.model.append(
                None, (order['name'], i)
            )

            # line = self.build_order_line(order, i)
            # self.known_lines.append(line)
            # self.grid.attach(line, 0, i, 1, 1)
            # i += 1

        # add_button = Gtk.Button.new_with_mnemonic("_Add")
        # self.grid.attach(add_button, 0, i, 1, 1)
        # add_button.connect("clicked", self._on_button_add_clicked)

        self.list.set_model(self.model)

    def _on_button_add_clicked(self, w):
        order = {
            'name': "",
            'levels': '',
            'display': '',
            'sorting': ''
        }
        win = order_line_window(order, -1, self)
        win.show_all()

    def grid_refresh(self):
        for line in self.known_lines:
            line.remove()

        i = 2
        for order in self.custom_orders:
            line = self.build_order_line(order, i)
            self.known_lines.append(line)
            self.grid.attach(line, 0, i, 1, 1)
            i += 1
        self.grid.show_all()


    def build_order_line(self, order, number):

        def insert_input(name: str, label_str: str, row: int, order, number):
            label = Gtk.Label()
            label.set_text(label_str)
            line_grid.attach(label, 0, row, 1, 1)

            input = Gtk.Button()  # comma list
            input.set_label(name)

            line_grid.attach(input, 1, row, 1, 1)

            input.connect("clicked", on_open_clicked, order, number)

        def on_open_clicked(w, order, number):
            win = order_line_window(order, number, self)
            win.show_all()

        line_grid = Gtk.Grid()

        insert_input(name, 'name', 0, order, number)

        return line_grid

    def _on_row_activated(self,  model, path, iter):
        pass

    def _on_remove_cellrenderer_clicked(self, cellrenderer, path):
        pass


class order_line_window(Gtk.Window):
    def __init__(self, order, row, parent):
        self.order = order
        self.row = row
        self.parent = parent

        super().__init__(title="Order Line")
        self._layout()
        self._connect()

    def _layout(self):
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.input_name = self._add_input('Name', self.order['name'], 0)
        self.input_tree_levels = self._add_input('tree levels', self.order['levels'], 1)
        self.input_display = self._add_input('Display', self.order['display'], 2)
        self.input_sorting = self._add_input('Sorting', self.order['sorting'], 3)

        self.close_button = Gtk.Button.new_with_mnemonic("_Close")
        self.grid.attach_next_to(self.close_button, self.input_sorting, Gtk.PositionType.BOTTOM, 1, 1)

        self.save_button = Gtk.Button.new_with_mnemonic("_Save")
        self.grid.attach_next_to(self.save_button, self.close_button, Gtk.PositionType.RIGHT, 1, 1)


    def _add_input(self, label, value, position):

        input_url_label = Gtk.Label()
        input_url_label.set_text(label)
        self.grid.attach(input_url_label, 0, position, 1, 1)

        input_url = Gtk.Entry()
        input_url.set_text(value)
        self.grid.attach_next_to(input_url, input_url_label, Gtk.PositionType.RIGHT, 3, 1)

        return input_url

    def _connect(self):
        self.close_button.connect("clicked", self._on_button_close_clicked)
        self.save_button.connect("clicked", self._on_button_save_clicked)
        self.connect("key-press-event", self._key_press_event)

    def _on_button_close_clicked(self, widget):
        self.destroy()
        pass

    def _on_button_save_clicked(self, widget):
        self.order = {
            'name': "Artist - Genre - By Date",
            'levels': 'artist, genre',
            'display': '$date - $title',
            'sorting': 'date, title'
        }

        self.parent.custom_orders.append(self.order)
        self.parent.grid_refresh()
        self.destroy()
        pass

    def _key_press_event(self, widget, event):
        keyval = event.keyval
        keyval_name = Gdk.keyval_name(keyval)
        state = event.state
        ctrl = (state & Gdk.ModifierType.CONTROL_MASK)
        if ctrl and keyval_name == 's':
            self._on_button_save_clicked(widget)
        if keyval_name == 'Return':
            self._on_button_save_clicked(widget)
        if ctrl and keyval_name == 'c':
            self._on_button_close_clicked(widget)
        if keyval_name == 'Escape':
            self._on_button_close_clicked(widget)
