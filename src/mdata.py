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

import sys

import mutagen


class MData:
    """ A place to store all of the metadata for a given file.
    
    This is currently a wrapper around mutagen's amazing tagging abilities.
    This requires a mutagen-1.17 or newer.

    """

    def __init__(self, filename):
        meta = mutagen.File(filename, easy=True)
        if meta is not None:
            self.mbtrack = meta.tags['musicbrainz_trackid']
            self.mbalbum = meta.tags['musicbrainz_albumid']
            self.mbartist = meta.tags['musicbrainz_artistid']
            self.track = meta.tags['title']
            self.album = meta.tags['album']
            self.artist = meta.tags['artist']

    def pprint(self):
        print 'artist =', self.artist
        print 'album =', self.album
        print 'track =', self.track
        print 'mbartist =', self.mbartist
        print 'mbalbum =', self.mbalbum
        print 'mbtrack =', self.mbtrack


if __name__ == "__main__" :
    metadata = MData(sys.argv[1])
    if metadata is not None:
        print metadata.pprint()
