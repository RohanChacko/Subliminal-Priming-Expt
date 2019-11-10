import pygame
import time

## Ripped off AadilMehdi Sanchawala...like always

WIDTH = 1000
HEIGHT = 1000
FPS = 10

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## Initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Expt 1.0")
clock = pygame.time.Clock()
# display_surface = pygame.display.set_mode((X, Y ))


images = [pygame.image.load('Logos/biscuits/dansk_blue.jpg'), pygame.image.load('Logos/biscuits/tiffany_blue.jpg')]

def render() :
    '''
    render the sequence of frames for experiment 1
    '''

    screen.fill(BLACK)


    # Show a white circle initially
    pygame.draw.circle(screen, WHITE, (HEIGHT//2, WIDTH//2), 10, 2)
    pygame.display.update()

    # pygame delay does not do what we want
    # pygame.time.delay(150)
    time.sleep(2.001)
    screen.fill(BLACK)

    # display_surface.blit(images[0], (0, 0))


def main() :
    ## Game Loop
    running = True

    while running:

        clock.tick(FPS)     ## will make the loop run at the same speed all the time
        for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.

            ## listening for the the X button at the top or press escape
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                running = False

        render()

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__' :
    main()
