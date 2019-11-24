CONTROL_PATH = "Results/ControlGroup"
EXPERIMENTAL_PATH = "Results/ExperimentalGroup"


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
PURPLE = (128,0,128)
YELLOW = (255, 255, 0)
PINK = (255,20,147)
BROWN = (150,75,0)

color = {
'red' : RED,
'blue' :BLUE,
'green' : GREEN,
'orange' : ORANGE,
'purple' : PURPLE,
'black' : BLACK,
'yellow' : YELLOW,
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
PRIME_DELAY = 0.055
TASK_DELAY = 0.002