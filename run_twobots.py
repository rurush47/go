import pygame
import sys

from board import Board
from view import View
from ai import Ai, Evaluators
from stone_color import StoneColor

board = Board()
view = View()
white_ai = Ai(StoneColor.WHITE, Evaluators.freedoms_evaluate)
black_ai = Ai(StoneColor.BLACK, Evaluators.simple_evaluate)

while True:
	board.make_move(black_ai.get_best_move(board, 1))
	board.make_move(white_ai.get_best_move(board, 2))
	game_board = board.get_board()
	view.draw_board(game_board)

