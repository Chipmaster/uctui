#! /usr/bin/env python

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


import os

import opts
import uctgui
import settings
import mdata
import save
import web
from sets import Set

def gather_collection(directory, file_dic):
    """
    Builds a dictionary with form:
    
    Path-->(mtime, mdata)
    """
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                entry = os.path.join(root,name)
                print "Parsing: ", entry
                if not entry in file_dic:
                    #New file
                    f = mdata.MData(entry)
                    file_dic[entry] = (os.path.getmtime(entry),f)
                elif not file_dic[entry][0] == os.path.getmtime(entry):
                    #file has been modified since last check
                    f = mdata.MData(entry)
                    file_dic[entry] = (os.path.getmtime(entry),f)
            except: #mdata.NotAMusicFile
                pass
    return file_dic


if __name__ == '__main__':
    (options, args) = opts.read_opts()

    set = settings.Settings()
    settings = set.get_settings()

    if options.debug:
        print options.gui
        print set.first_run()

    
    state = save.State()
    file_dic = state.get_state()

    if options.gui:
        uctgui.PyApp()
        uctgui.gtk.main()
    else:
        file_dic = gather_collection(settings['collection_directory'], file_dic)
    
        uuids = Set()
        for f in file_dic:
            uuids.add(file_dic[f][1].mbalbum[0])
    
        submit = web.UserCollection()
        submit.add_releases(uuids)


    state.save_state(file_dic)

