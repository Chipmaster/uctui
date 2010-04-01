# This file is part of uctui.

# uctui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# uctui is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with uctui.  If not, see <http://www.gnu.org/licenses/>.

import gtk

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("uctui")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        menubar = self._createMenu()


        notebook = self._createNotebook()


        vbox = gtk.VBox(False, 2)
        vbox.pack_start(menubar, False, False, 0)
        vbox.pack_start(notebook, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def _createMenu(self):
        mb = gtk.MenuBar()

        #File menu
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("_File")
        filem.set_submenu(filemenu)

        agr = gtk.AccelGroup()
        self.add_accel_group(agr)

        exit = gtk.ImageMenuItem(gtk.STOCK_QUIT, agr)
        key, mod = gtk.accelerator_parse("Q")
        exit.add_accelerator("activate", agr, key, 
            mod, gtk.ACCEL_VISIBLE)

        exit.connect("activate", gtk.main_quit)
        
        filemenu.append(exit)


        #Options menu
        optionsmenu = gtk.Menu()
        optionsm = gtk.MenuItem("_Options")
        optionsm.set_submenu(optionsmenu)

        propertiesi = gtk.ImageMenuItem(gtk.STOCK_PROPERTIES, agr)
        optionsmenu.append(propertiesi)


        #Help menu
        helpmenu = gtk.Menu()
        helpm = gtk.MenuItem("_Help")
        helpm.set_submenu(helpmenu)

        abouti = gtk.ImageMenuItem(gtk.STOCK_ABOUT, agr)
        helpmenu.append(abouti)


        #Add menus to menubar
        mb.append(filem)
        mb.append(optionsm)
        mb.append(helpm)

        return mb

    def _createNotebook(self):
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        
        for i in ["Test", "Update"]:
            tframe = i;

            frame = gtk.Frame(tframe)
            frame.set_border_width(10)
            frame.set_size_request(100, 300)
            frame.show()

            label = gtk.Label(tframe)
            frame.add(label)
            label.show()

            label = gtk.Label(tframe)
            notebook.append_page(frame, label)

        return notebook



if __name__ == "__main__":
    PyApp()

