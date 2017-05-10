import hit_run as hr
import numpy as np
import pygame
from pygame.locals import *

class fish(pygame.sprite.Sprite):

    #Fish object in the simulation Returns: fish object
    #Functions: move, update_pos, update_home, update_sigma
    #Attributes: area, pos, home, sigma

    def __init__(self, pos, home, sigma):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('fish.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.pos = pos
        self.home = home
        self.sigma = sigma

    def move(radius):
    	pos = hr.binorm_hitrun_circle(self.home,self.sigma,self.pos,self.pos,radius,1)
    	self.pos = pos
        return pos

    def update_pos(p):
    	self.pos = p

    def update_home(h):
    	self.home = h

    def update_sigma(s):
    	self.sigma = s
