from board import Board
from vector2 import Vector2
from stone_color import StoneColor
import random

class Evaluators:
	@staticmethod
	def freedoms_evaluate(state, color):
		score = 0
		for i in range(Board.size):
			for j in range(Board.size):
				if state[i][j] == color:
					score += 1
				elif state[i][j] == StoneColor.get_opposite(color):
					score -= 1
			score -= Board.get_total_liberties_count(state, StoneColor.get_opposite(color), Board.size)
			score += Board.get_total_liberties_count(state, color, Board.size)
		return score

	@staticmethod
	def simple_evaluate(state, color):
		score = 0
		for i in range(Board.size):
			for j in range(Board.size):
				if state[i][j] == color:
					score += 1
				elif state[i][j] == StoneColor.get_opposite(color):
					score -= 1
		return score


class Ai:

	def __init__ (self, color, evaluate):
		self.color = color
		self.evaluate = evaluate



		# no counting fully-surrounded empty spots, at least for now
		# performance is already fairly bad and this would reduce it even more




	def alfa_beta(self, state, color, history, depth, alfa, beta):

		if depth == 0:
			return self.evaluate(state, color)

		history.append(state)
		opposite = StoneColor.get_opposite(color)
		if color == self.color:
			for pos_state in Board.valid_states_generator(state, color, history):
				beta = min(beta, self.alfa_beta(pos_state[1], opposite, history, depth - 1, alfa, beta))
				if alfa >= beta:
					break
			history.pop()
			return beta
		else:
			for pos_state in Board.valid_states_generator(state, color, history):
				alfa = max(alfa, self.alfa_beta(pos_state[1], opposite, history, depth - 1, alfa, beta))
				if alfa >= beta:
					break
			history.pop()
			return alfa

	def get_best_move (self, board, depth):

		alfa = -999999
		best_positions = []

		history = board.state_history.get_state_list()
		opposite = StoneColor.get_opposite(self.color)
		for pos_state in board.valid_states_generator(board.board, self.color, history):
			score = self.alfa_beta(pos_state[1], opposite, history, depth - 1, alfa, 999999)
			if score > alfa:
				best_positions = [ pos_state[0] ]
				alfa = score
			elif score == alfa:
				best_positions.append(pos_state[0])

		if len(best_positions) == 0:
			return None

		return random.choice(best_positions)

