#
# GOM Small Scale Simulation
# Xuetao Lu
# 
# Released under the GNU General Public License

VERSION = "0.1"

try:
    import sys
    import fish
    import camera
    import pygame
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('GOM Small Scale Simulation')

    # Fill background, here I need to load the map as the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Create fishe & camera groups
    fish_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    # 

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

        fish_group.clear()
        camera_group.clear()
        fish_group.update()
        camera_group.update()
        fish_group.draw()
        camera_group.draw()
        pygame.display.flip()


if __name__ == '__main__': main()
