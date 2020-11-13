import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("01", "Reasons To Be Cheerful Part 3", "Ian Dury and The Blockheads")
        self.song2 = Song("02", "I Will Survive", "Gloria Gaynor")
        self.songs = [self.song1, self.song2]

    # @unittest.skip("Delete this line to run the test")
    def test_song_has_title(self):
        self.assertEqual("Reasons To Be Cheerful Part 3", self.song1.title)

#TASKS ---

#CREATE NEW SONG
    @unittest.skip("Delete this line to run the test")
    def test_create_new_song(self):
        self.assertEqual(2, len(self.songs))


#ADD SONG TO ROOM PLAYLIST
    @unittest.skip("Delete this line to run the test")
    def test_add_song_to_room(self):

        self.assertEqual(2, len(self.songs))