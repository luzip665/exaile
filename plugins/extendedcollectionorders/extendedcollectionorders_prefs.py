
import os
from xlgui.preferences import widgets
from xl.nls import gettext as _

name = _('Extended Collections')
basedir = os.path.dirname(os.path.realpath(__file__))
ui = os.path.join(basedir, "eco_pane.ui")

class GenreArtistDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco1'

    # def change(self, *args):
    #     pass

class ArtistGenreDate(widgets.CheckPreference):
    default = False
    name = 'extendedcollectionorders/eco2'

    # def change(self, *args):
    #     pass