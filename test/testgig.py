import unittest
from gig import GigSearcher


class TestGigSearcher(unittest.TestCase):

    def test_create_gigsearcher(self):
        gigsearcher = GigSearcher()

    def test_gigsearcher_get_setlist_id(self):
        gigsearcher = GigSearcher()
        url = "http://www.setlist.fm/setlist/muse/2016/3arena-dublin-ireland-3f045a7.html"

        self.assertEqual("3f045a7",gigsearcher.get_setlist_id(url))
