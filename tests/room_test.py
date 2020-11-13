import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(11, 15.00)
        self.room2 = Room(12, 30.00)
        self.rooms = [self.room1, self.room2]


    # @unittest.skip("Delete this line to run the test")
    def test_check_room_price(self):
        self.assertEqual(15.00, self.room1.price)

#TASKS ---

# CREATE NEW ROOM

    @unittest.skip("Delete this line to run the test")
    def test_add_room(self):
        new_room = Room(13, 40.00)
        self.room1.add_room(new_room)
        self.assertEqual(3, len(self.rooms))

# CHECK GUEST INTO ROOM

    @unittest.skip("Delete this line to run the test")
    def test_guest_check_in(self):
        self.assertEqual(0, self.room1.guest_check_in())

# CHECK GUEST OUT OF ROOM 

    @unittest.skip("Delete this line to run the test")
    def test_guest_check_out(self):
        self.assertEqual(0, self.room1.guest_check_out())

# ADD SONG TO ROOM PLAYLIST

    @unittest.skip("Delete this line to run the test")
    def test_add_song_to_room(self):
        self.assertEqual(0, self.room1.guest_check_out())








    # @unittest.skip("Delete this line to run the test")
    # def (self):
    #     self.assertEqual(,)





