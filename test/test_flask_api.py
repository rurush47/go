from multiprocessing import Process
from unittest import TestCase

import pygame

from board import Board
from flask_api import app
from view import View


class ApiTest(TestCase):

    def setUp(self):
        self.board = Board()
        self.view = View()
        app.view = self.view
        app.board = self.board
        self.view.draw_board(self.board.get_board())
        self.api_subprocess = Process(target=lambda:app.run(host='0.0.0.0', port=5000, debug=False))

    def test_sync(self):
        pass

    def test_getting_state_without_sync(self):
        pass

    def test_getting_state(self):
        pass

    def test_playing_stone_without_sync(self):
        pass

    def test_playing_stone_on_valid_position(self):
        pass

    def test_playing_stone_on_invalid_position(self):
        pass

    def test_playing_stone_on_the_same_position_twice(self):
        pass

    def test_playing_outside_of_your_turn(self):
        pass

    def tearDown(self):
        pygame.quit()
        self.api_subprocess.join()
        self.api_subprocess.terminate()

