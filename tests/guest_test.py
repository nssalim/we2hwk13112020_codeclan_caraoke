import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Viper Room", 150, 5, 20)

        self.song1 = Song("The Rolling Stones", "She's a rainbow")
        self.song2 = Song("The Kinks", "All day and all of the night")
        self.song3 = Song("The Beatles", "Norwegian Wood")
        self.song4 = Song("The Troggs", "Wild Thing")

        self.songs = [self.song1, self.song2, self.song3, self.song4]

        self.guest1 = Guest("Holly Golighty", 20, 50, self.song1, 4)
        self.guest2 = Guest("Paul Varjak", 27, 100, self.song2, 8)
        self.guest3 = Guest("Cat", 100, 0, self.song4, 2)

        self.guests = [self.guest1, self.guest2, self.guest3]

    def test_guest_name(self):
        self.assertEqual("Holly Golighty", self.guest1.name)

    def test_guest_has_fave_song(self):
        self.assertEqual("She's a rainbow", self.guest1.fave_song.title)

    def test_guest_rendition_of_song(self):
        self.assertEqual(4, self.guest1.rendition_of_song)

    def test_guest_can_change_favourite_song(self):
        song = Song("Bill Haley", "Rock around the clock")
        self.guest1.fave_song = song
        self.assertEqual("Rock around the clock", self.guest1.fave_song.title)

    def test_guest_wallet(self):
        self.assertEqual(50.00, self.guest1.wallet)

if __name__ == '__main__':
    unittest.main()