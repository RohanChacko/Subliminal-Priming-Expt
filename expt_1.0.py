import pygame
import time
import random

WIDTH = 1000
HEIGHT = 1000
FPS = 100

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
LETTERS = list(UPPERCASE) + list(LOWERCASE)

## Initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Expt 1.0")
clock = pygame.time.Clock()
image = pygame.image.load('./Logos/juice/rawabi_orange.jpg') 
image = pygame.transform.scale(image, (150,150))
font = pygame.font.Font('freesansbold.ttf', 15)

def render_mask(screen) :
    INITIAL_X = INITIAL_Y = 25

    for i in range(0,HEIGHT,15) :
        for j in range(0,WIDTH,15) :

            tp = font.render(random.choice(LETTERS), True, BLACK, WHITE)
            textRect = tp.get_rect()
            textRect.center = (i+15, j+15)
            screen.blit(tp, textRect)

def render():
    '''
    render the sequence of frames for experiment 1
    '''

    screen.fill(WHITE)
    pygame.display.update()
    time.sleep(1)

    

    # First mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen)
        pygame.display.update()
        time.sleep(0.5)
    
    # pygame.draw.circle(screen, RED, (HEIGHT//2, WIDTH//2), 100, 5)
    # pygame.draw.circle(screen, GREEN, (150, 100), 8, 5)
    
    # Prime frame
    screen.fill(WHITE)
    screen.blit(image, (random.randrange(HEIGHT//2 - 200, HEIGHT // 2 + 200), random.randrange(WIDTH//2 - 200, WIDTH//2 + 200)))
       
    
    render_mask(screen)
    pygame.display.update()
    time.sleep(0.005)

    # Second mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen)
        pygame.display.update()
        time.sleep(0.5)

    

    screen.fill(WHITE)



def main() :
    ## Game Loop
    running = True
    flag = 0
    # screen.fill(WHITE)
    while running:
        # screen.fill(WHITE)
        clock.tick(FPS)     ## will make the loop run at the same speed all the time
        for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.

            ## listening for the the X button at the top or press escape
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                running = False

        if flag == 0:
            render()
            # print(time.time() - start)
            flag = 1


        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__' :
    main()
