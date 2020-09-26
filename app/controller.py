from app import app
from flask import render_template
from app.models.game import *
from app.models.player import *


# @app.route('/<player1>/<player2>')
# def index(player1, player2):
#     if player1 == "rock" and player2 == "scissors":
#         return "player1 wins!!"
#     elif player1 == "rock" and player2 == "paper":
#         return "player2 wins!!"
#     elif player1 == "rock" and player2 == "rock":
#         return "draw!!"
#     elif player1 == "scissors" and player2 == "rock":
#         return "player2 wins!!"
#     elif player1 == "scissors" and player2 == "paper":
#         return "player1 wins!!"
#     elif player1 == "scissors" and player2 == "scissors":
#         return "draw!!"
#     elif player1 == "paper" and player2 == "rock":
#         return "player1 wins!!"
#     elif player1 == "paper" and player2 == "scissors":
#         return "player2 wins!!"
#     elif player1 == "paper" and player2 == "paper":
#         return "draw!!"

@app.route('/')
def index():
    player_rock = Player("Hayley", "rock")
    player_paper = Player("Aly", "paper")
    player_scissors = Player("Mel", "scissors")

    game1 = Game(player_rock, player_scissors)
    result = game1.rps_game(player_rock.choice, player_scissors.choice)
    return render_template("index.html", result=result)