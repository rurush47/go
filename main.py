# TODO move to main game loop
import pygame
import sys
import thread

from board import Board
from view import View
from flask_api import app

def flask_thread():
    app.run(host='0.0.0.0', port=5000, debug=False)

view = View()
board = Board()
app.view = view
app.board = board
thread.start_new_thread(flask_thread,())

while True:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
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
