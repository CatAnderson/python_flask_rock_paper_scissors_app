from app import app
from flask import render_template


@app.route('/<player1>/<player2>')
def index(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        return "player1 wins!!"
    elif player1 == "rock" and player2 == "paper":
        return "player2 wins!!"
    elif player1 == "rock" and player2 == "rock":
        return "draw!!"
    elif player1 == "scissors" and player2 == "rock":
        return "player2 wins!!"
    elif player1 == "scissors" and player2 == "paper":
        return "player1 wins!!"
    elif player1 == "scissors" and player2 == "scissors":
        return "draw!!"
    elif player1 == "paper" and player2 == "rock":
        return "player1 wins!!"
    elif player1 == "paper" and player2 == "scissors":
        return "player2 wins!!"
    elif player1 == "paper" and player2 == "paper":
        return "draw!!"