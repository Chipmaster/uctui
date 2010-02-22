#! /usr/bin/python

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
import web
from sets import Set

def gather_collection(directory):
    music = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                print "Parsing: ", os.path.join(root,name)
                f = mdata.MData(os.path.join(root,name))
                music.append(f)
            except: #mdata.NotAMusicFile:
                pass
    return music


if __name__ == '__main__':
    (options, args) = opts.read_opts()

    set = settings.Settings()
    settings = set.get_settings()

    if options.debug:
        print options.gui
        print set.first_run()

    if options.gui:
        uctgui.PyApp()
        uctgui.gtk.main()

    files = gather_collection(settings['collection_directory'])
    
    uuids = Set()
    for f in files:
        uuids.add(f.mbalbum[0])
    
    print "Uploading..."
    submit = web.UserCollection()
    submit.add_releases(uuids)



