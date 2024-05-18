import pygame

class Ball:
    BALL_RADIUS = 10
    BALL_SPEED = 5
    __BALL_COLOR = "white"
    __DIR_UP_LEFT = pygame.Vector2(-1, -1)
    __DIR_DOWN_LEFT = pygame.Vector2(-1, 1)
    __DIR_UP_RIGHT = pygame.Vector2(1, -1)
    __DIR_DOWN_RIGHT = pygame.Vector2(1, 1)

    def __init__(self, screen, start_x, start_y):
        self.screen = screen
        self.start_position = pygame.Vector2(start_x, start_y)
        self.position = self.start_position.copy()
        self.direction = self.__DIR_UP_LEFT

    def draw(self):
        self.rect = pygame.draw.circle(self.screen, self.__BALL_COLOR, self.position, self.BALL_RADIUS)

    def move(self):
        if self.position.y <= 0 or self.position.y >= self.screen.get_height():
            self.direction.y = self.direction.y * -1

        self.position += self.direction * self.BALL_SPEED

    def reset(self):
        self.position = self.start_position.copy()
        self.direction = self.__DIR_UP_LEFT

    def collision_left_pad(self):
        self.direction = self.__DIR_DOWN_RIGHT

    def collision_right_pad(self):
        self.direction = self.__DIR_UP_LEFT
