# This file is part of uctui.

# uctui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import gtk

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("uctui")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

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

        mb.append(filem)

        
        optionsmenu = gtk.Menu()
        optionsm = gtk.MenuItem("_Options")
        optionsm.set_submenu(optionsmenu)

        propertiesi = gtk.ImageMenuItem(gtk.STOCK_PROPERTIES, agr)
        optionsmenu.append(propertiesi)

        mb.append(optionsm)

        
        helpmenu = gtk.Menu()
        helpm = gtk.MenuItem("_Help")
        helpm.set_submenu(helpmenu)

        abouti = gtk.ImageMenuItem(gtk.STOCK_ABOUT, agr)
        helpmenu.append(abouti)

        mb.append(helpm)
        

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
