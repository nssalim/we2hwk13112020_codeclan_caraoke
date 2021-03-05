import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink
from classes.food import Food

class TestBar(unittest.TestCase): 
    def setUp(self):

        self.song1 = Song("The Rolling Stones", "She's a rainbow")
        self.song2 = Song("The Kinks", "All day and all of the night")
        self.song3 = Song("The Beatles", "Norwegian Wood")
        self.song4 = Song("The Troggs", "Wild Thing")

        self.songs = [self.song1, self.song2, self.song3, self.song4]

        self.drink = Drink("rum", 5.00, 30)
        self.food = Food("peanuts", 2.00, 25)
        self.guest1 = Guest("Holly Golighty", 20, 50, self.song1, 4)
        self.guest2 = Guest("Paul Varjak", 27, 100, self.song2, 8)
        self.guest3 = Guest("Cat", 100, 0, self.song4, 2)

        self.guests = [self.guest1, self.guest2, self.guest3]
  
    def test_guest_age(self):
        self.assertEqual(20, self.guest1.age)

    def test_guest_wallet(self):
        self.assertEqual(50.00, self.guest1.wallet)

    def test_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest1.sufficient_funds(self.drink))
 
    def test_sufficient_funds__false_if_not_enough(self):
        self.assertEqual(False, self.guest1.sufficient_funds(self.drink))


