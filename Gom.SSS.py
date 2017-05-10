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

def load_png(name):
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

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('GOM Small Scale Simulation')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialise homes, fishes, camera
    speed = 13
    rand = ((0.1 * (random.randint(5,8))))
    ball = Ball((0,0),(0.47,speed))

    # Initialise sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)

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
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player1.moveup()
                if event.key == K_z:
                    player1.movedown()
                if event.key == K_UP:
                    player2.moveup()
                if event.key == K_DOWN:
                    player2.movedown()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_z:
                    player1.movepos = [0,0]
                    player1.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    player2.movepos = [0,0]
                    player2.state = "still"

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        ballsprite.update()
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()