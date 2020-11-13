import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Reasons To Be Cheerful Part 3", "Ian Dury and The Blockheads")
