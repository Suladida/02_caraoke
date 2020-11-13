import unittest

from classes.guest import Guest
from classes.room import Room
# from tests.song_test import TestSong


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Trixie", 100.00)

    # @unittest.skip("Delete this line to run the test")
    def test_guest_cash(self):
        self.assertEqual(100.00, self.guest1.guest_cash("Trixie"))
