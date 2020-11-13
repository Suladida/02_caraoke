import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 01")

    # @unittest.skip("Delete this line to run the test")
    def test_check_room_empty(self):
        self.assertEqual(0, self.room.check_room_occupancy())

    @unittest.skip("Delete this line to run the test")
    def test_check_room_occupancy(self):
        self.assertEqual(1, self.room.check_room_occupancy())
    
    # @unittest.skip("Delete this line to run the test")
    def test_add_guest_to_list(self):
        new_guest = Guest("Katya")
        self.room.add_guest_to_list(self.room)
        self.room.add_guest_to_list(new_guest)
        self.assertEqual(2, self.room.check_room_occupancy())

# #TASKS---

# #ADD GUEST TO ROOM
#     # @unittest.skip("Delete this line to run the test")
#     def test_add_guest_to_room(self):
#         self.add_guest_to_room(self.guest)
#         print (self.room.check_room_occupancy())
#         self.assertEqual(1, self.room.check_room_occupancy())
        

#     def test_check_room_occupancy(self):
#         self.room.check_room_occupancy()

# #REMOVE GUEST FROM ROOM





#ADD SONG TO ROOM





    # # @unittest.skip("Delete this line to run the test")
    # def test_has_route_number(self):
    #     self.assertEqual(22, self.bus.route_number)