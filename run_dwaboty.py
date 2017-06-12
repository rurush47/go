import pygame
import sys

from board import Board
from view import View
from ai import Ai
from stone_color import StoneColor

board = Board()
view = View()
ai = Ai(StoneColor.WHITE)
ai2 = Ai(StoneColor.BLACK)

while True:
	board.make_move(ai2.get_best_move(board, 1))
	board.make_move(ai.get_best_move(board, 1))
	game_board = board.get_board()
	view.draw_board(game_board)

