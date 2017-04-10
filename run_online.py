# TODO move to main game loop
from multiprocessing import Process
import pygame
import sys

from board import Board
from view import View
from flask_api import app

app.view = View()
app.board = Board()
app.view.draw_board(app.board.get_board())
app.run(host='0.0.0.0', port=5000, debug=False)
