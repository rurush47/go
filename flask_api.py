# coding=utf-8
#TODO move authentication to a decorator called @authenticated
from flask import abort, Flask, jsonify, request
import os

from stone_color import StoneColor
from vector2 import Vector2

app = Flask(__name__)
app.player_ids = {}

@app.route("/sync", methods=['GET'])
def sync():
    players_online = len(app.player_ids)
    if players_online<0 or players_online>=2:
        return 'all players slots taken', 418
    new_player_id = os.urandom(24).encode('hex')
    app.player_ids[new_player_id] = StoneColor.WHITE if players_online == 0  else StoneColor.BLACK
    return jsonify(player_id=new_player_id, stone_color=StoneColor.enum_to_string_map[app.player_ids[new_player_id]])



@app.route('/get_state', methods=['POST'])
def get_state():
    player_id = request.form.get("player_id", None)
    if player_id is None or not player_id in app.player_ids:
        abort(418)
    is_your_turn = app.board.turn_manager.current_turn == app.player_ids[player_id]
    return jsonify(game_sate=app.board.board, previous_state = app.board.state_history.states, is_your_turn=is_your_turn)


# adresujemy od zera z początkiem układu w lewym górnym rogu
@app.route('/send_move', methods=['POST'])
def send_move():
    player_id = request.form.get("player_id", None)
    if player_id is None or not player_id in app.player_ids:
        abort(418)
    x = request.form.get('x', None)
    y = request.form.get('y', None)
    if x is None or y is None:
        return 'No x and y coordinates', 500
    if app.board.turn_manager.current_turn != app.player_ids[player_id]:
        return 'not your turn', 500
    game_response = app.board.make_move(Vector2(int(x),int(y)))
    if game_response is None:
        app.view.draw_board(app.board.get_board())
        return "valid move", 200
    return game_response, 500
