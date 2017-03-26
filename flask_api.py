# coding=utf-8
from flask import abort, Flask, jsonify, request
from Board import Board


app = Flask(__name__)
app.player_ids = []

@app.route("/sync", methods=['GET'])
def sync():
    pass




@app.route('/get_state', methods=['GET'])
def get_state():
    return jsonify(app.board.board_list)

# adresujemy od zera z początkiem układu w lewym dolnym rogu
@app.route('/send_state', methods=['POST'])
def get_state():
    id = request.form.get('player_id', None)
    x = request.form.get('x', None)
    y = request.form.get('y', None)
    if x is None or y is None or id is None:
        abort(404)
    was_move_made = app.board.run_move(x,y,id)
    if not was_move_made:
        abort(404)
        return
    return jsonify(app.board.board_list)






if __name__ == '__main__':
    app.run(debug=True)
    app.board = Board()
