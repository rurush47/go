import pygame
import sys

from stone import Stone
from board import Board
from vector2 import Vector2
from stone_color import StoneColor


class View:
    def __init__(self):
        pygame.init()

        # window specification
        self.size = Board.size
        self.pixels_per_square = 50
        self.background_color = (50, 50, 50)
        self.lines_color = (80, 80, 80)
        self.white_color = (0, 0, 0)
        self.black_color = (255, 255, 255)
        self.circle_width = 2
        self.lines_width = 2
        self.frame_width = self.pixels_per_square / 2

        self.screen_size = (self.size - 1) * self.pixels_per_square + 2 * self.frame_width
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

        self.draw_board(None)

    def draw_board(self, board):
        self.screen.fill(self.background_color)
        for i in range(self.size):
            pygame.draw.line(self.screen,
                             self.lines_color,
                             [i * self.pixels_per_square + self.frame_width, self.frame_width],
                             [i * self.pixels_per_square + self.frame_width, self.screen_size - self.frame_width],
                             self.lines_width)

        for i in range(self.size):
            pygame.draw.line(self.screen,
                             self.lines_color,
                             [self.frame_width, i * self.pixels_per_square + self.frame_width],
                             [self.screen_size - self.frame_width, i * self.pixels_per_square + self.frame_width],
                             self.lines_width)

        if board is not None:
            for i in range(self.size):
                for j in range(self.size):
                    stone = board[i][j]
                    if isinstance(stone, Stone):
                        color = stone.get_color()
                        normalized_color = self.get_normalized_color(color)
                        pygame.draw.circle(self.screen,
                                           normalized_color,
                                           [i * self.pixels_per_square + self.frame_width,
                                            j * self.pixels_per_square + self.frame_width],
                                           self.pixels_per_square / 3,
                                           self.circle_width)

        pygame.display.flip()

    def get_normalized_click_pos(self, click_pos):
        x = click_pos[0] / self.pixels_per_square
        y = click_pos[1] / self.pixels_per_square
        vector2 = Vector2(x, y)
        return vector2

    def get_normalized_color(self, color):
        if color is StoneColor.BLACK:
            return self.black_color
        else:
            return self.white_color


# TODO move to main game loop
view = View()
board = Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            pos = view.get_normalized_click_pos(click_pos)
            print str(pos.x) + ' ' + str(pos.y)
            board.place_stone(pos)
            game_board = board.get_board()
            view.draw_board(game_board)
