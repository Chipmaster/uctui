# This file is part of uctui.

# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.


import version
from optparse import OptionParser


usage="%prog [-g]"

def readOpts():
    parser = OptionParser(usage=usage, version=version.version)
    parser.add_option("-g", "--gtk", action="store_true", 
                      dest="gui", default=False, help="run gtk interface")

#Last option
    parser.add_option("-D", "--debug", action="store_true",
                      dest="debug", default=False, help="enable debugging output")
    return parser.parse_args()
