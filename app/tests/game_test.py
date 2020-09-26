import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Hayley", "Rock")
        self.player2 = Player("Aly", "Paper")
        self.player3 = Player("Chloe", "Scissors")

