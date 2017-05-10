#!/usr/bin/python

# [load modules here]
import pygame
import pygame.locals
import numpy as np
import Hit_run


# [resource handling functions here]

class Fish(pygame.sprite.Sprite):
	"""docstring for Fish"""
	def __init__(self, arg):
		pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        
		pos_now = np.array([])
		pos_home = np.array([])
		territory = np.array([[1,0],[0,1]])
		step_range = 1
        
# "Perform actual movement based on position_now, velocity and show up distribution"
    def move(self):
    	pos_next = binorm_hitrun_circle(pos_home,territory,pos_now,pos_now,step_range,1)
