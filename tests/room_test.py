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
    
    # @unittest.skip("Delete this line to run the test")
    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest2)
        self.assertEqual(2, self.room.check_room_occupancy())

    # @unittest.skip("Delete this line to run the test")
    def test_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest2)
        self.room.remove_guest_from_room(self.guest)
        self.assertEqual(1, self.room.check_room_occupancy())

    # @unittest.skip("Delete this line to run the test")
    def test_add_song_to_room(self):
        song = Song("Reasons To Be Cheerful Part 3", "Ian Dury and The Blockheads")
        song2 = Song("Believe", "Cher")
        self.room.add_song_to_room(song)
        self.room.add_song_to_room(song2)
        self.assertEqual(2, self.room.check_room_songs())

#ADD SONG TO ROOM:

