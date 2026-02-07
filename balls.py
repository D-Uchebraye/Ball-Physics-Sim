import pygame
import numpy as np
import os

#get direcotry where scipt is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH= os.path.join(BASE_DIR,"assets","BouncingBall.png")

class ball:
    def __init__(self,pos):
        self.velocity = np.array([0,0],dtype=float)
        self.pos = np.array(pos,dtype=float)
        self.surface = pygame.image.load(IMAGE_PATH).convert_alpha()
        self.hitbox = self.surface.get_rect()    

    
    def draw(self,screen):
        screen.blit(self.surface,self.pos)
        self.hitbox.x = self.pos[0]
        self.hitbox.y = self.pos[1]

    def collide(self,ball_2_velocity):
        self.velocity += ball_2_velocity


    def update_pos(self):
        self.pos += self.velocity
        self.velocity[1] += 2



