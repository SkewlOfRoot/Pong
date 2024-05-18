import pygame

class Pad:
    PAD_WIDTH = 20
    PAD_HEIGHT = 120
    __PAD_COLOR = "white"

    def __init__(self, screen, start_x, start_y):
        self.screen = screen
        self.position = pygame.Vector2(start_x, start_y)

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.__PAD_COLOR,
                         pygame.Rect(self.position.x, self.position.y, self.PAD_WIDTH, self.PAD_HEIGHT))