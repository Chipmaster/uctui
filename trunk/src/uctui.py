#! /usr/bin/python

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


import opts
import uctgui
import settings

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

