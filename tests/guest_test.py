import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Trixie", 100.00)

    # @unittest.skip("Delete this line to run the test")
    def test_guest_has_name(self):
        self.assertEqual("Trixie", self.guest.name)

