# TODO move to main game loop
from multiprocessing import Process

import pygame
import sys

from board import Board
from view import View
from flask_api import app

view = View()
board = Board()
app.view = view
app.board = board
# flask_subprocess = Process(target=lambda:app.run(host='0.0.0.0', port=5000, debug=False))
# flask_subprocess.start()

while True:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            # flask_subprocess.terminate()
            # flask_subprocess.join()
            sys.exit()
        if pressed[pygame.K_w]:
            # Pass
            board.make_move(None)
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            pos = view.get_normalized_click_pos(click_pos)
            print str(pos.x) + ' ' + str(pos.y)
            board.make_move(pos)
            game_board = board.get_board()
            view.draw_board(game_board)

