import pygame
import sys
from Board import Board


class View:
    def __init__(self):
        pygame.init()

        # window specification
        self.size = Board.size
        self.pixels_per_square = 50
        self.lines_color = (80, 80, 80)
        self.lines_width = 2
        self.background_color = (50, 50, 50)
        self.frame_width = 20

        self.screen_size = (self.size - 1)*self.pixels_per_square + 2*self.frame_width
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

        self.draw_board()

    def draw_board(self):
        self.screen.fill(self.background_color)
        for i in range(self.size):
                pygame.draw.line(self.screen,
                                 self.lines_color,
                                 [i*self.pixels_per_square + self.frame_width, self.frame_width],
                                 [i*self.pixels_per_square + self.frame_width, self.screen_size - self.frame_width],
                                 self.lines_width)

        for i in range(self.size):
            pygame.draw.line(self.screen,
                             self.lines_color,
                             [self.frame_width, i*self.pixels_per_square + self.frame_width],
                             [self.screen_size - self.frame_width, i*self.pixels_per_square + self.frame_width],
                             self.lines_width)

        pygame.display.flip()



view = View()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


