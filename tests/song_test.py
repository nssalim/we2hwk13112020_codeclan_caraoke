import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Kinks", "All of the day and all of the night")

    def test_song_has_artist(self):
        self.assertEqual("The Kinks", self.song.artist)

    def test_song_has_title(self):
        self.assertEqual("All of the day and all of the night", self.song.title)

if __name__ == '__main__':
    unittest.main()