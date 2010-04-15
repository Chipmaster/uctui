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

import save
import web

def gather_collection(directory, file_dic):
    """
    Builds a dictionary with form:
    
    Path-->(mtime, mdata)
    """
    print "Checking for updated files..."
    for root, dirs, files in os.walk(directory):
        for name in files:
            try:
                entry = os.path.join(root,name)
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

def update(directory):
    file_dic = save.State().get_state()
    file_dic = gather_collection(directory, file_dic)
    uuids = set([file_dic[x][1].mbalbum[0] for x in file_dic])
    
    web.UserCollection().add_releases(uuids)

    save.State().save_state(file_dic)
