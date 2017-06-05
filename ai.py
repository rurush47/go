from board import Board
from vector2 import Vector2
from stone_color import StoneColor

class Ai:

	def __init__ (self, color):
		self.color = color

	@staticmethod
	def evaluate(state):
		score = 0
		for i in range (Board.size):
			for j in range (Board.size):
				if state[i][j] == StoneColor.WHITE:
					score += 1
				elif state[i][j] == StoneColor.BLACK:
					score -= 1

		# no counting fully-surrounded empty spots, at least for now
		# performance is already fairly bad and this would reduce it even more

		return score


	def alfa_beta(self, state, color, history, depth, alfa, beta):

		if depth == 0:
			score = Ai.evaluate(state)
			if self.color == StoneColor.WHITE:
				return +score
			else:
				return -score

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
		best_position = None

		history = board.state_history.get_state_list()
		opposite = StoneColor.get_opposite(self.color)
		for pos_state in board.valid_states_generator(board.board, self.color, history):
			score = self.alfa_beta(pos_state[1], opposite, history, depth - 1, alfa, 999999)
			if score > alfa:
				best_position = pos_state[0]
				alfa = score

		return best_position

