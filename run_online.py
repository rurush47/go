# TODO move to main game loop
from multiprocessing import Process
import pygame
import sys

from board import Board
from view import View
from flask_api import app
try:
    app.view = View() #type : View
    app.board = Board() #type : Board
    app.view.draw_board(app.board.get_board())
    app.run(host='0.0.0.0', port=5000, debug=False)
except :
    pygame.quit()
