from app import app
from flask import render_template, request
from app.models.game import *
from app.models.player import *


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/game')
def game_page():
    return render_template("game.html")


@app.route('/result', methods=['POST', 'GET'])
def result_page():
    player1_name = request.form.get('player1_name')
    player1_choice = request.form.get('player1_choice')
    player1 = Player(player1_name, player1_choice)

    player2_name = request.form.get('player2_name')
    player2_choice = request.form.get('player2_choice')
    player2 = Player(player2_name, player2_choice) 

    game1 = Game(player1, player2)
    result = game1.rps_game(player1.choice, player2.choice)
    
    return render_template("results.html", result=result)


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


# @app.route('/')
# def index():
#     player_rock = Player("Hayley", "rock")
#     player_paper = Player("Aly", "paper")
#     player_scissors = Player("Mel", "scissors")

#     game1 = Game(player_rock, player_scissors)
#     result = game1.rps_game(player_rock.choice, player_scissors.choice)
#     return render_template("index.html", result=result)