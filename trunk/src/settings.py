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

import os.path

settings_file = "~/.config/MusicBrainz/uctui.conf"


class Settings:
    def __init__(self):
        self.file = os.path.expanduser(settings_file)
        d = os.path.dirname(self.file)
        if not os.path.exists(d):
            os.makedirs(d)


    def first_run(self):
        return not(os.path.isfile(self.file))


    def store_settings(self, settings):
        # Overwrites the save file with dictionary full of settings
        try:
            f = open(self.file, 'w')
            try:
                sortList = settings.keys() # Print alphabetically so at least we save consistently
                sortList.sort()
                for key in sortList:
                    f.write(key + '=' + settings[key] +'\n')
            
            finally:
                f.close()
        except IOError:
            pass


    def get_settings(self):
        # Retrieve settings from settings file and store in a dictionary.
        # Returns an empty dictionary if the file does not exist or is empty.
        settings = {}
        try:
            f = open(self.file, 'r')
            try:
                for line in f:
                    settings[line.partition("=")[0]] = line.rstrip("\n\r").partition("=")[2]
        
            finally:
                f.close()
            
        except IOError:
            pass
        
        return settings
