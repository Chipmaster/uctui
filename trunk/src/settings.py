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

import os.path

settings_file = "~/.config/MusicBrainz/uctui.conf"


class Settings:
    """
    Abstracts away the process of saving and loading configurations.
    Current method creates a file from a dictionary with format:
    key=value
    Uses the Borg design pattern to allow all instances to maintain same settings state
    """
    __shared_state = {}
    __settings = {}
    __instances = 0

    def __init__(self):
        self.__dict__ = self.__shared_state

        self.file = os.path.expanduser(settings_file)
        d = os.path.dirname(self.file)
        if not os.path.exists(d):
            os.makedirs(d)
            
        if self.__instances is 0:
            self.__settings = self.__get_settings()
        
        self.__instances = self.__instances + 1


    def __del__(self):
        self.__instances = self.__instances - 1
        if self.__instances is 0:
            self.__store_settings(self.__settings)


    def first_run(self):
        return not(os.path.isfile(self.file))


    def store_settings(self, settings):
        self.__settings = settings

    def __store_settings(self, settings):
        """
        Overwrites the save file with dictionary full of settings
        """
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
        return self.__settings


    def __get_settings(self):
        """
        Retrieve settings from settings file and store in a dictionary.
        Returns an empty dictionary if the file does not exist or is empty.
        """
        s = {}
        
        try:
            f = open(self.file, 'r')
            try:
                for line in f:
                    s[line.partition("=")[0]] = line.rstrip("\n\r").partition("=")[2]
        
            finally:
                f.close()
            
        except IOError:
            pass
        
        return s
