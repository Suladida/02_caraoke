import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("01", "Reasons To Be Cheerful Part 3", "Ian Dury and The Blockheads")
        self.song2 = Song("02", "I Will Survive", "Gloria Gaynor")

    # @unittest.skip("Delete this line to run the test")
    def test_song_has_title(self):
        self.assertEqual("Reasons To Be Cheerful Part 3", self.song1.title)

#TASKS ---

#ADD SONG TO ROOM PLAYLIST