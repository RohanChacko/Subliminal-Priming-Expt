import pygame
import time
import random
import os
import sys

WIDTH = 1000
HEIGHT = 1000
FPS = 100

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 215, 0)
PURPLE = (128,0,128)
YELLOW = (255, 255, 0)
PINK = (255,20,147)
BROWN = (150,75,0)

color = {
}

pool_color_1 = [RED, ORANGE, YELLOW, GREEN]
pool_color_1_label = ["RED", "ORANGE", "YELLOW", "GREEN"]

pool_color_2 = [BROWN, PINK, BLUE, PURPLE]
pool_color_2_label = ["BROWN", "PINK", "BLUE", "PURPLE"]

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
LETTERS = list(UPPERCASE) + list(LOWERCASE)


# DELAY
FIXATION_DELAY = 3
MASK_DELAY = 0.5
PRIME_DELAY = 0.005
TASK_DELAY = 0.002

## Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Expt 1.0")
clock = pygame.time.Clock()

# Images and text init
font = pygame.font.Font('freesansbold.ttf', 15)

def render_mask(screen) :

    for i in range(0,WIDTH,15) :
        for j in range(0,HEIGHT,15) :

            tp = font.render(random.choice(LETTERS), True, BLACK, WHITE)
            textRect = tp.get_rect()
            textRect.center = (i, j)
            screen.blit(tp, textRect)

def render():
    '''
    render the sequence of frames for Experiment
    '''

    # Fixation frame
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()
    time.sleep(FIXATION_DELAY)

    # First mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen)
        pygame.display.update()
        time.sleep(MASK_DELAY)


    # Prime frame
    screen.fill(WHITE)
    x = random.randrange(WIDTH//2 - 250, WIDTH//2 + 250)
    y = random.randrange(HEIGHT//2 - 250, HEIGHT // 2 + 250)
    choice = random.randrange(0,4)
    category = random.randrange(0,4)

    
    color_disp = pool_color_1[choice]
    op_color = pool_color_2[category]

    pygame.draw.circle(screen, color_disp, (x, y),50)
    prime_color = pool_color_1_label[choice] 
    task_color = pool_color_2_label[category]
    print("Primed with", color_disp)


    render_mask(screen)
    pygame.display.update()
    time.sleep(PRIME_DELAY)

    # Second mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen)
        pygame.display.update()
        time.sleep(MASK_DELAY)


    # Fixation frame
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()
    time.sleep(FIXATION_DELAY)


    # Task frame
    screen.fill(WHITE)

    pygame.draw.circle(screen, color_disp, (WIDTH//2 - 400, HEIGHT//2), 50)
    time.sleep(TASK_DELAY)
    pygame.draw.circle(screen, op_color, (WIDTH//2 + 400, HEIGHT//2), 50)
    pygame.display.update()
    print(task_color, 'printed first')



def main() :
    ## Game Loop
    running = True
    flag = 0
    # screen.fill(WHITE)

    # juice/chocobis/biscuits
    # category = sys.argv[1]
    while running:
        # screen.fill(WHITE)
        clock.tick(FPS)     ## will make the loop run at the same speed all the time
        for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.

            ## listening for the the X button at the top or press escape
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                running = False

            if event.type == pygame.KEYDOWN and flag == 1:
                if event.key == pygame.K_SPACE :
                    print("SPACEBAR PRESSED")
                    running = False
                elif event.key == pygame.K_q :
                    print("Left (Q) key pressed")
                    running = False
                elif event.key == pygame.K_p :
                    print("Right (P) key pressed")
                    running = False
                else :
                    pass


        if flag == 0:
            render()
            flag = 1


        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__' :
    main()
