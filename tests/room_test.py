import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 01")
        self.guest = Guest("Katya")
        self.guest2 = Guest("Trixie")

    @unittest.skip("Delete this line to run the test")
    def test_check_room_empty(self):
        self.assertEqual(0, self.room.check_room_occupancy())

    @unittest.skip("Delete this line to run the test")
    def test_check_room_occupancy(self):
        self.assertEqual(1, self.room.check_room_occupancy())
    
    @unittest.skip("Delete this line to run the test")
    def test_add_guest_to_list(self):
        self.room.add_guest_to_list(self.guest)
        self.room.add_guest_to_list(self.guest2)
        self.assertEqual(2, self.room.check_room_occupancy())

    # @unittest.skip("Delete this line to run the test")
    def test_remove_guest_from_list(self):
        self.room.add_guest_to_list(self.guest)
        self.room.add_guest_to_list(self.guest2)
        self.room.remove_guest_from_list(self.guest)
        self.assertEqual(1, self.room.check_room_occupancy())

    @unittest.skip("Delete this line to run the test")
    def test_add_song_to_room(self):
        self.room.add_song_to_room()

#ADD SONG TO ROOM:

