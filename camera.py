import numpy as np
import pygame
from pygame.locals import *

class bait(object):
    #docstring for bait
    def __init__(self, b_distance):
        self.b_distance = b_distance


class camera(pygame.sprite.Sprite):

    #Camera object in the simulation
    #Returns: Camera object
    #Functions: move, update_pos, update_home, update_sigma
    #Attributes: area, pos, home, sigma

    def __init__(self, pos, c_distance, bait):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('camera.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.pos = pos
        self.c_distance = c_distance
        self.bait = bait

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
