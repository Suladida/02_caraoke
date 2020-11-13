import unittest

# from tests.guest_test import TestGuest
from classes.room import Room
# from tests.song_test import TestSong


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(11, 15.00)
        self.room1 = Room(12, 30.00)

    # @unittest.skip("Delete this line to run the test")
    def test_hello(self):
        self.assertEqual("Hello!", self.room.hello())

    # @unittest.skip("Delete this line to run the test")
    def test_check_guest_wallet(self):
        self.assertEqual(15.00, self.room.get_room_price(11))

    # @unittest.skip("Delete this line to run the test")




