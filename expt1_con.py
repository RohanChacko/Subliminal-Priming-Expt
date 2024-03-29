# USAGE python expt1_con.py <(time delay b/w prime and task in  ms)> <(cgroup (control group) / exp (experimental group))> <Output file name> 


import pygame
import time
import random
import os
import sys
import csv
from config import *

def render_mask(screen, font) :

    for i in range(0,WIDTH,15) :
        for j in range(0,HEIGHT,15) :

            tp = font.render(random.choice(LETTERS), True, BLACK, WHITE)
            textRect = tp.get_rect()
            textRect.center = (i, j)
            screen.blit(tp, textRect)

def render(screen, font, fix_delay):
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
    for i in range(6) :
        screen.fill(WHITE)
        render_mask(screen, font)
        pygame.display.update()
        time.sleep(MASK_DELAY)


    # Prime frame
        
    x = random.randrange(WIDTH//2 - 250, WIDTH//2 + 250)
    y = random.randrange(HEIGHT//2 - 250, HEIGHT // 2 + 250)
    choice = random.randrange(0,4)
    category = random.randrange(0,4)


    color_disp = pool_color_1[choice]
    op_color = pool_color_2[category]

    prime_color = pool_color_1_label[choice]
    task_color = pool_color_2_label[category]

    if sys.argv[2] != 'cgroup':
        screen.fill(WHITE)
        pygame.draw.circle(screen, color_disp, (x, y),50)
        render_mask(screen, font)
        pygame.display.update()
        time.sleep(PRIME_DELAY)
        primed_with = color_disp
    else:
        primed_with = 'control group'

    # Second mask
    for i in range(6) :
        screen.fill(WHITE)
        render_mask(screen, font)
        pygame.display.update()
        time.sleep(MASK_DELAY)



    # Fixation frame
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()
    time.sleep(int(fix_delay))

    pygame.mixer.music.load('./sound/ding.mp3')
    pygame.mixer.music.play(0)
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15)
    pygame.display.update()
    time.sleep(10)


    # Task frame
    screen.fill(WHITE)

    # NEW : Randomizing appearance order of circles in task frame
    order = dict()
    if random.randrange(0, 9999) % 2 == 0 :

        pygame.draw.circle(screen, op_color, (WIDTH//2 - 400, HEIGHT//2), 50)
        time.sleep(TASK_DELAY)
        pygame.draw.circle(screen, color_disp, (WIDTH//2 + 400, HEIGHT//2), 50)
        order['left'] = color_disp
        order['right'] = op_color
    else :
        pygame.draw.circle(screen, op_color, (WIDTH//2 + 400, HEIGHT//2), 50)
        time.sleep(TASK_DELAY)
        pygame.draw.circle(screen, color_disp, (WIDTH//2 - 400, HEIGHT//2), 50)
        order['right'] = color_disp
        order['left'] = op_color

    pygame.display.update()

    appeared_first = op_color

    return primed_with, appeared_first, order

def main(fix_delay) :

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
            primed_with, appeared_first, order = render(screen, font, fix_delay)
            flag = 1


        pygame.display.flip()

    pygame.quit()

    return keypress, primed_with, appeared_first, order



if __name__ == '__main__' :

    # Create the Control and Experimental Result Directories if they do not exist already
    if not os.path.exists(CONTROL_PATH):
        os.makedirs(CONTROL_PATH)
    if not os.path.exists(EXPERIMENTAL_PATH):
        os.makedirs(EXPERIMENTAL_PATH)

    print(sys.argv)
    file_name = None
    file_name_csv = None
    if sys.argv[2] == 'cgroup':
        file_name = CONTROL_PATH + '/' + sys.argv[3]
        file_name_csv = file_name + '.csv'
    else:
        file_name = EXPERIMENTAL_PATH + '/' + sys.argv[3]
        file_name_csv = file_name + '.csv'

    keypress, primed_with, appeared_first, order = main(sys.argv[1])
    print(appeared_first)
    print(order)
    append_string = "Experiment 1 :: Keypress: {} | Primed With: {} | Appeared First: {} | Order: {} | Time: {}\n".format(keypress, primed_with, appeared_first, order, sys.argv[1])
    with open(file_name, "a+") as f:
        f.write(append_string)

    csv_columns = [
        "Experiment Number",
        "Keypress",
        "Primed With",
        "Appeared First",
        "Order",
        "Time",
    ]
    append_dict = [{
        "Experiment Number" : "1",
        "Keypress" : keypress,
        "Primed With" : primed_with,
        "Appeared First" : appeared_first,
        "Order" : order,
        "Time" : sys.argv[1],
    }]

    with open(file_name, "a+") as f:
        f.write(append_string)

    try:
        with open(file_name_csv, 'a+') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=csv_columns)

            if os.stat(file_name_csv).st_size == 0:
                writer.writeheader()
            for data in append_dict:
                writer.writerow(data)
    except IOError:
        print("I/O Error")
    
