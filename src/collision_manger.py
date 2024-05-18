from ball import Ball
from pad import Pad

class CollisionManger:

    def __init__(self, ball, left_pad, right_pad):
        self.ball = ball
        self.left_pad = left_pad
        self.right_pad = right_pad

    def detect_collision(self):
        if self.ball.rect.colliderect(self.left_pad.rect):
            self.ball.collision_left_pad()
        elif self.ball.rect.colliderect(self.right_pad.rect):
            self.ball.collision_right_pad()

