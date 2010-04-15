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

import settings
import update

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
        
        self.settings = settings.Settings()
        self.s = self.settings.get_settings()

        self.set_title("uctui")
        #self.set_size_request(800, 600)
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
        update = self._updateTab()
        notebook.append_page(update, gtk.Label("Update"))

        return notebook

    def _updateTab(self):
        button = gtk.Button("Update")
        update = gtk.VBox(False, 15)
        info = gtk.Table(3,2)
        usr = gtk.Label("Username:")
        pss = gtk.Label("Password:")
        md = gtk.Label("Music Directory:")

        usre = gtk.Entry()
        usre.set_text(self.s['username'])
        psse = gtk.Entry()
        psse.set_visibility(False)
        psse.set_text(self.s['password'])
        mde = gtk.Entry()
        mde.set_text(self.s['collection_directory'])
        

        dialog = gtk.FileChooserDialog("Music Directory..",
                action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)


        info.attach(usr,0,1,0,1)
        info.attach(pss,0,1,1,2)
        info.attach(md,0,1,2,3)
        info.attach(usre,1,2,0,1)
        info.attach(psse,1,2,1,2)
        info.attach(mde,1,2,2,3)

        update.pack_start(info, False, False, 10)
        update.pack_end(button, False, False, 10)

        button.connect("clicked", self._update, mde.get_text())

        usre.connect("changed", self._save, 'username')
        psse.connect("changed", self._save, 'password')
        mde.connect("changed", self._save, 'collection_directory')

        return update	

    def _save(self, object, key):
        self.s[key] = object.get_text()
        self.settings.store_settings(self.s)

    def _update(self, object, music_dir):
        update.update(music_dir)

if __name__ == "__main__":
    PyApp()
    gtk.main()

