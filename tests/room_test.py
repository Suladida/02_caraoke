import unittest

# from tests.guest_test import TestGuest
from classes.room import Room
# from tests.song_test import TestSong


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(11,15.00, 2)
        self.room2 = Room(12,40,4)
        self.room3 = Room(13, 40, 8)

    
    
    
    # self.assertEqual(EXPECTED, ACTUAL)
