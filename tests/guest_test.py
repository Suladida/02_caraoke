import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Trixie", 100.00)

    # @unittest.skip("Delete this line to run the test")
    def test_guest_has_name(self):
        self.assertEqual("Trixie", self.guest1.name)

#TASKS ---

# CHECK GUEST INTO ROOM

    @unittest.skip("Delete this line to run the test")
    def test_guest_check_in(self):
        self.assertEqual(0, self.room1.guest_check_in())

# CHECK GUEST OUT OF ROOM

    @unittest.skip("Delete this line to run the test")
    def test_guest_check_out(self):
        self.assertEqual(0, self.room1.guest_check_out())






# # Notes:
#     # @unittest.skip("Delete this line to run the test")
#     def test_guest_cash(self):
#         self.assertEqual(100.00, self.guest1.guest_cash("Trixie"))