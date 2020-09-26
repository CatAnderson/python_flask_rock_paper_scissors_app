import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_rock = Player("Hayley", "rock")
        self.player_paper = Player("Aly", "paper")
        self.player_scissors = Player("Mel", "scissors")

        self.game1 = Game(self.player_rock, self.player_scissors)

    def test_has_players(self):
        self.assertEqual(self.player_rock, self.game1.player1)
        self.assertEqual(self.player_scissors, self.game1.player2)

    def test_rps_game__player1_wins__with_rock(self):
        result = self.game1.rps_game(self.player_rock.choice, self.player_scissors.choice)
        self.assertEqual("Player 1 wins!!", result)

    def test_rps_game__player1_wins__with_scissors(self):
        result = self.game1.rps_game(self.player_scissors.choice, self.player_paper.choice)
        self.assertEqual("Player 1 wins!!", result)

    def test_rps_game__player1_wins__with_paper(self):
        result = self.game1.rps_game(self.player_paper.choice, self.player_rock.choice)
        self.assertEqual("Player 1 wins!!", result)

    def test_rps_game__player2_wins__with_rock(self):
        result = self.game1.rps_game(self.player_scissors.choice, self.player_rock.choice)
        self.assertEqual("Player 2 wins!!", result)

    def test_rps_game__player2_wins__with_scissors(self):
        result = self.game1.rps_game(self.player_paper.choice, self.player_scissors.choice)
        self.assertEqual("Player 2 wins!!", result)

    def test_rps_game__player2_wins__with_paper(self):
        result = self.game1.rps_game(self.player_rock.choice, self.player_paper.choice)
        self.assertEqual("Player 2 wins!!", result)