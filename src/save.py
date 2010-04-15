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

import pickle
import os

state_file = "~/.config/MusicBrainz/uctui.pck"


class State:
    """
    Abstracts the process of saving the state of files we have parsed.
    Currently using pickle instead of cpickle as we used classes.
    """

    def __init__(self):
        self.file = os.path.expanduser(state_file)
        d = os.path.dirname(self.file)
        if not os.path.exists(d):
            os.makedirs(d)

    def get_state(self):
        if not os.path.exists(self.file):
            return {}
        f = open(self.file, 'r')
        print "Loading state..."
        file_dic = pickle.load(f)
        f.close()
        return file_dic

    def save_state(self, file_dic):
        f = open(self.file, 'w')
        print "Saving state..."
        pickle.dump(file_dic, f)
        f.close()
        return
