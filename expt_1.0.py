import pygame
import time
import random
import os
import sys

WIDTH = 1900
HEIGHT = 1000
FPS = 100

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 215, 0)

color = {
'red' : RED,
'blue' :BLUE,
'green' : GREEN,
'orange' : ORANGE,
}
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

dir_biscuits = './Logos/biscuits'
im_biscuits = []
name_biscuits = []

dir_chocobis = './Logos/choco_bis'
im_chocobis = []
name_chocobis = []

dir_juice = './Logos/juice'
im_juice = []
name_juice = []

for dirpath, _, filenames in os.walk(dir_biscuits):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_biscuits.append(pygame.transform.scale(temp, (150,150)))
        name_biscuits.append(path.split('/')[-1])

for dirpath, _, filenames in os.walk(dir_chocobis):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_chocobis.append(pygame.transform.scale(temp, (150,150)))
        name_chocobis.append(path.split('/')[-1])

for dirpath, _, filenames in os.walk(dir_juice):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_juice.append(pygame.transform.scale(temp, (150,150)))
        name_juice.append(path.split('/')[-1])


def render_mask(screen) :

    for i in range(0,WIDTH,15) :
        for j in range(0,HEIGHT,15) :

            tp = font.render(random.choice(LETTERS), True, BLACK, WHITE)
            textRect = tp.get_rect()
            textRect.center = (i, j)
            screen.blit(tp, textRect)

def render(category):
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
    choice = random.randrange(0,2)

    if category == 'biscuits' :
        screen.blit(im_biscuits[choice], (x ,y))
        prime_color = name_biscuits[choice].split('.')[0].split('_')[1]
        task_color = name_biscuits[(choice+1)%2].split('.')[0].split('_')[1]
        print("Primed with", name_biscuits[choice].split('.')[0])

    elif category == 'chocobis' :
        screen.blit(im_chocobis[choice], (x ,y))
        prime_color = name_chocobis[choice].split('.')[0].split('_')[1]
        task_color = name_chocobis[(choice+1)%2].split('.')[0].split('_')[1]
        print("Primed with", name_chocobis[choice].split('.')[0])

    elif category == 'juice' :
        screen.blit(im_juice[choice], (x ,y))
        prime_color = name_juice[choice].split('.')[0].split('_')[1]
        task_color = name_juice[(choice+1)%2].split('.')[0].split('_')[1]
        print("Primed with", name_juice[choice].split('.')[0])

    # pygame.draw.circle(screen, RED, (HEIGHT//2, WIDTH//2), 100, 5)

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

    pygame.draw.circle(screen, color[task_color], (WIDTH//2 - 400, HEIGHT//2), 50)
    time.sleep(TASK_DELAY)
    pygame.draw.circle(screen, color[prime_color], (WIDTH//2 + 400, HEIGHT//2), 50)
    pygame.display.update()
    print(task_color, 'printed first')



def main() :
    ## Game Loop
    running = True
    flag = 0
    # screen.fill(WHITE)

    # juice/chocobis/biscuits
    category = sys.argv[1]
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
            render(category)
            flag = 1


        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__' :
    main()
