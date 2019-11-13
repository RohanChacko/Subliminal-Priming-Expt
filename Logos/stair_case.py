import pygame 
import time
import random
import os
import sys

WIDTH = 1900
HEIGHT = 1000
FPS = 100

# Initialize pygame
pygame.init()

# Define the Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Staircase Task")
clock = pygame.time.Clock()

def draw_fixation_point(ready=false, time_delay=0.5):
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), 15, 2)
    pygame.display.update()

def draw_query_image(query_image, time_delay=0.5):
    screen.fill(WHITE)
    screen.blit(query_image, (x,y))
    pygame.display.update()

def draw():
    draw_fixation_point()
    

