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
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

color = {
'red' : RED,
'blue' :BLUE,
'green' : GREEN,
'orange' : ORANGE,
'purple' : PURPLE,
'black' : BLACK,
'yellow' : YELLOW,
}
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
LETTERS = list(UPPERCASE) + list(LOWERCASE)


# DELAY
FIXATION_DELAY = 3
MASK_DELAY = 0.5
PRIME_DELAY = 0.005
TASK_DELAY = 0.002

dir_biscuits = './Logos/biscuits'
im_biscuits = []
name_biscuits = []

dir_chocobis = './Logos/choco_bis'
im_chocobis = []
name_chocobis = []

dir_juice = './Logos/juice'
im_juice = []
name_juice = []

dir_mnm = './Logos/mnm'
im_mnm = []
name_mnm = []

dir_skittles = './Logos/skittles'
im_skittles = []
name_skittles = []

dir_pool = './Logos/pool'
im_pool = []
name_pool = []

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

for dirpath, _, filenames in os.walk(dir_skittles):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_skittles.append(pygame.transform.scale(temp, (150,150)))
        name_skittles.append(path.split('/')[-1])

for dirpath, _, filenames in os.walk(dir_mnm):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_mnm.append(pygame.transform.scale(temp, (150,150)))
        name_mnm.append(path.split('/')[-1])

for dirpath, _, filenames in os.walk(dir_pool):
    for f in filenames:
        path = os.path.abspath(os.path.join(dirpath, f))
        temp = pygame.image.load(path)
        im_pool.append(pygame.transform.scale(temp, (150,150)))
        name_pool.append(path.split('/')[-1])


def render_mask(screen, font) :

    for i in range(0,WIDTH,15) :
        for j in range(0,HEIGHT,15) :

            tp = font.render(random.choice(LETTERS), True, BLACK, WHITE)
            textRect = tp.get_rect()
            textRect.center = (i, j)
            screen.blit(tp, textRect)

def render(screen, font, category, fix_delay):
    '''
    render the sequence of frames for Experiment
    '''

    primed_with = ''
    appeared_first = ''

    # Fixation frame
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()
    time.sleep(FIXATION_DELAY)

    # First mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen, font)
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
        primed_with = name_biscuits[choice].split('.')[0]

    elif category == 'choco_bis' :
        screen.blit(im_chocobis[choice], (x ,y))
        prime_color = name_chocobis[choice].split('.')[0].split('_')[1]
        task_color = name_chocobis[(choice+1)%2].split('.')[0].split('_')[1]
        primed_with = name_chocobis[choice].split('.')[0]

    elif category == 'juice' :
        screen.blit(im_juice[choice], (x ,y))
        prime_color = name_juice[choice].split('.')[0].split('_')[1]
        task_color = name_juice[(choice+1)%2].split('.')[0].split('_')[1]
        primed_with = name_juice[choice].split('.')[0]

    elif category == 'skittles' :
        screen.blit(im_skittles[choice], (x ,y))
        prime_color = name_skittles[choice].split('.')[0].split('_')[1]
        task_color = name_skittles[(choice+1)%2].split('.')[0].split('_')[1]
        primed_with = name_skittles[choice].split('.')[0]

    elif category == 'pool' :
        screen.blit(im_pool[choice], (x ,y))
        prime_color = name_pool[choice].split('.')[0].split('_')[1]
        task_color = name_pool[(choice+1)%2].split('.')[0].split('_')[1]
        primed_with = name_pool[choice].split('.')[0]

    elif category == 'mnm' :
        screen.blit(im_mnm[choice], (x ,y))
        prime_color = name_mnm[choice].split('.')[0].split('_')[1]
        task_color = name_mnm[(choice+1)%2].split('.')[0].split('_')[1]
        primed_with = name_mnm[choice].split('.')[0]
    # pygame.draw.circle(screen, RED, (HEIGHT//2, WIDTH//2), 100, 5)

    render_mask(screen, font)
    pygame.display.update()
    time.sleep(PRIME_DELAY)

    # Second mask
    for i in range(5) :
        screen.fill(WHITE)
        render_mask(screen, font)
        pygame.display.update()
        time.sleep(MASK_DELAY)


    # Fixation frame
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()
    time.sleep(int(fix_delay))


    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15)
    pygame.display.update()
    time.sleep(10)

    # Task frame
    screen.fill(WHITE)

    # NEW : Randomizing appearance order of circles in task frame
    order = dict()
    if random.randrange(0, 9999) % 2 == 0 :

        pygame.draw.circle(screen, color[task_color], (WIDTH//2 - 400, HEIGHT//2), 50)
        time.sleep(TASK_DELAY)
        pygame.draw.circle(screen, color[prime_color], (WIDTH//2 + 400, HEIGHT//2), 50)
        order['left'] = task_color
        order['right'] = prime_color
    else :

        pygame.draw.circle(screen, color[task_color], (WIDTH//2 - 400, HEIGHT//2), 50)
        time.sleep(TASK_DELAY)
        pygame.draw.circle(screen, color[prime_color], (WIDTH//2 + 400, HEIGHT//2), 50)
        order['left'] = task_color
        order['right'] = prime_color

    appeared_first = color[task_color]
    pygame.display.update()
    # print(task_color, 'printed first')

    return primed_with, appeared_first, order

def main(category, fix_delay) :

    ## Initialize pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Expt 1.0")
    clock = pygame.time.Clock()

    # Images and text init
    font = pygame.font.Font('freesansbold.ttf', 15)

    ## Game Loop
    running = True
    flag = 0
    keypress = ''
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
                if event.key == pygame.K_q :
                    keypress = "Left (Q)"
                    running = False
                elif event.key == pygame.K_p :
                    keypress = "Right (P)"
                    running = False
                else :
                    pass


        if flag == 0:
            primed_with, appeared_first, order = render(screen, font, category, fix_delay)
            flag = 1


        pygame.display.flip()

    pygame.quit()

    return keypress, primed_with, appeared_first, order


if __name__ == '__main__' :
    _, _, _ = main()
