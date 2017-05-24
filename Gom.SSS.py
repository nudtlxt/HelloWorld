#
# GOM Small Scale Simulation
# Xuetao Lu
# 
# Released under the GNU General Public License

VERSION = "0.1"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    import fish
    import camera
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('GOM Small Scale Simulation')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialise fishes, camera
    


    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        ballsprite.update()
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
