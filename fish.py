#Fish class and container

try:
	import os
	import math
	import hit_run as hr
	import numpy as np
	import pygame
	from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def load_png_fish(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

class Fish(pygame.sprite.Sprite):

    #Fish
    #Functions: move, update_pos, update_home, update_sigma
    #Attributes: area, pos, home, sigma

    def __init__(self, pos, home, sigma,radius, camera):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png_fish('fish.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.pos = pos
        self.home = home
        self.sigma = sigma
        self.radius = radius
        self.camera = camera
	self.catched = 0

    def set_start_pos(self,p):
    	self.pos = p
    	self.rect = p

    def set_home(self,h):
    	self.home = h

    def set_sigma(self,s):
    	self.sigma = s

    def set_radius(self,r):
    	self.radius = r

	def vnorm(self,v):
		return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

    def update(self):
    	pos = hr.binorm_hitrun_circle(self.home,self.sigma,self.pos,self.pos,self.radius,1)
    	self.pos = pos
    	self.rect = pos

    	# calculate distance to check whether catched by camera, if catched update camera
    	d = vnorm(pos - self.camera.pos)
    	if d<=self.camera.bait.distance:
    		if d<=self.camera.distance:
			self.camera.update()
			self.catched = 1
		else:
			drawbin = self.camera.bait.bernoulli(self.camera.bait.distance-self.camera.distance)
    			if drawbin:
    				self.camera.update()
				self.catched = 1

class Group_fishes(pygame.sprite.Group):

	#Container for fishes

	def __init__(self, arg):
        pygame.sprite.Group.__init__(self)
		
