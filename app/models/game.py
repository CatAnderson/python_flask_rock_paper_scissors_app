class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def rps_game(self, player1_choice, player2_choice):
        if (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "scissors" and player2_choice == "paper") or (player1_choice == "paper" and player2_choice == "rock"):
            return "Player 1 wins!!"

        elif (player1_choice == "rock" and player2_choice == "paper") or (player1_choice == "scissors" and player2_choice == "rock") or (player1_choice == "paper" and player2_choice == "scissors"):
            return "Player 2 wins!!"

        elif player1_choice == player2_choice:
            return "Draw!!"