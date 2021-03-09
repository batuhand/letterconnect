import json
from flask import Flask
from flask import request
from Controllers.gameController import create_new_game, make_move

app = Flask(__name__)
games = []

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return 'letterconnect'


# Route for creating new game
@app.route('/games', methods=['POST'])
def create_game():
    try:
        nodes = request.json["nodes"]
    except:
        return json.dumps({'error_type': "invalid_parameters"}), 400
    new_game = create_new_game(game_id=len(games), nodes=nodes)
    if new_game != False:
        games.append(new_game)
        return json.dumps({'game_id': str(new_game.game_id)}), 200
    else:
        return json.dumps({'error_type': "invalid_parameters"}), 400


# Route for getting the game info
@app.route('/games/<game_id>', methods=['GET'])
def get_game(game_id):
    try:
        result = games[int(game_id)].toJson()
        return result
    except:
        return json.dumps({"404": "Game not found"}), 404


# Route for making a move
@app.route('/games/<game_id>/move', methods=['POST'])
def move(game_id):
    if games[int(game_id)].winner is not None:
        return json.dumps({"error_type": "game_is_over"}), 400
    try:
        node_from = request.json["from"]
        node_to = request.json["to"]
    except:
        return json.dumps({'error_type': "invalid_parameters"}), 400
    try:
        result = make_move(game=games[int(game_id)], node_from=node_from, node_to=node_to)
        if result == False:
            return json.dumps({"error_type": "invalid_move"}), 400
        else:
            games[int(game_id)] = result
            return games[int(game_id)].toJson()

    except:
        return json.dumps({"404": "Game not found"}), 404
