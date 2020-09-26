import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Hayley", "Rock")
        self.player2 = Player("Aly", "Paper")

    def test_player_has_name(self):
        self.assertEqual("Hayley", self.player1.name)

    def test_player_has_a_choice(self):
        self.assertEqual("Paper", self.player2.choice)