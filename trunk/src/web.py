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

import musicbrainz2.webservice as ws
from musicbrainz2.wsxml import MbXmlParser, ParseError

import settings

class UserCollection:
    """This class provides an abstraction over MusicBrainz Webservice.

    This provides a convenient way to add to a users collection while
    still abstracting away all of the network IO that is inherent.

    """


    def _get_webservice(self):
        s = settings.Settings()
        x = s.get_settings()
        if not x:
            pass #implement no settings handling here
        return ws.WebService(username=x['username'].lower(), password=x['password'])


    def _make_add(self, releases):
        rel_list = ','.join(releases)
        return 'addAlbums=' + rel_list


    def _make_remove(self, releases):
        rel_list = ','.join(releases)
        return 'removeAlbums=' + rel_list


    def get_releases(self, maxitems=25, offset=0):
        w = self._get_webservice()
        f = {'maxitems': maxitems, 'offset': offset}
        result = w.get('collection', '', f)
        parser = MbXmlParser()
        return parser.parse(result)


    def add_releases(self, releases):
        w = self._get_webservice()
        release_string = self._make_add(releases)
        print "Adding releases..."
        result = w.post('collection', '', release_string)
        parser = MbXmlParser()
        return parser.parse(result)


    def remove_releases(self, releases):
        w = self._get_webservice()
        release_string = self._make_remove(releases)
        print "Removing releases..."
        result = w.post('collection', '', release_string)
        parser = MbXmlParser()
        return parser.parse(result)


if __name__ == "__main__":
    u = UserCollection()
    r = u.get_releases()
    tupac = [u'f5e7ddad-e38e-4621-9173-6bad2f126c33'] # All Eyez on Me
    v = u.add_releases(tupac)
    print 'Your releases:'
    for release in r.getReleaseResults():
        print release.getRelease().getId()
