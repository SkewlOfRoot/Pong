import pygame
from collision_manger import CollisionManger
from ball import Ball
from pad import Pad

class GameManager:

    def __init__(self, screen):
        self.screen = screen
        self.ball = Ball(screen, screen.get_width() / 2, screen.get_height() / 2)
        self.left_pad = Pad(screen, 0, 10)
        self.right_pad = Pad(screen, screen.get_width() - 20, 10)
        self.collision_manager = CollisionManger(self.ball, self.left_pad, self.right_pad)
        self.score_left = 0
        self.score_right = 0
        self.font = pygame.font.SysFont("Consolas", 54)

    def go(self, delta_time):
        self.draw_game_objects()
        self.move_pads()
        self.move_ball()
        self.collision_manager.detect_collision()
        self.print_score()

    def draw_game_objects(self):
        self.ball.draw()
        self.left_pad.draw()
        self.right_pad.draw()

    def move_pads(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        max_y = self.screen.get_height() - Pad.PAD_HEIGHT
        pad_y = mouse_y if mouse_y <= max_y else max_y
        if mouse_x > self.screen.get_width() / 2:
            self.right_pad.position.y = pad_y
        else:
            self.left_pad.position.y = pad_y

    def move_ball(self):
        self.ball.move()

        position = self.ball.position

        if position.x < 0:
            self.score_right += 1
            self.ball.reset()
        elif position.x > self.screen.get_width():
            self.score_left += 1
            self.ball.reset()

        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_w]:
        #    self.ball.position.y -= 300 * delta_time
        #if keys[pygame.K_s]:
        #    self.ball.position.y += 300 * delta_time
        #if keys[pygame.K_a]:
        #    self.ball.position.x -= 300 * delta_time
        #if keys[pygame.K_d]:
        #    self.ball.position.x += 300 * delta_time

    def print_score(self):
        img_score_left = self.font.render(str(self.score_left), True, "white")
        img_score_right = self.font.render(str(self.score_right), True, "white")
        self.screen.blit(img_score_left, (self.screen.get_width() / 2 - 200 - (img_score_left.get_width() / 2), self.screen.get_height() - 100))
        self.screen.blit(img_score_right, (self.screen.get_width() / 2 + 200 - (img_score_right.get_width() / 2), self.screen.get_height() - 100))