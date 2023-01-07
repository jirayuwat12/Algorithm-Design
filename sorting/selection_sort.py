#selection sort algorithm with simulation

import pygame
import random
import time

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Selection Sort")

#clock
clock = pygame.time.Clock()

#variables
array = []
array_size = 100
array_width = screen_width/array_size
array_height = screen_height/array_size
array_color = white
array_selected_color = red
array_sorted_color = green
array_unsorted_color = blue
array_sorted = False
array_unsorted = True
array_selected = False
array_selected_index = 0
array_sorted_index = 0
array_unsorted_index = 0

#functions
def create_array():
    global array
    array = []
    for i in range(array_size):
        array.append(random.randint(0,screen_height))

def draw_array():
    global array
    for i in range(len(array)):
        pygame.draw.rect(screen,array_color,(i*array_width,screen_height-array[i],array_width,array[i]))

def draw_array_selected():
    global array
    for i in range(len(array)):
        if i == array_selected_index:
            pygame.draw.rect(screen,array_selected_color,(i*array_width,screen_height-array[i],array_width,array[i]))
        else:
            pygame.draw.rect(screen,array_color,(i*array_width,screen_height-array[i],array_width,array[i]))

def draw_array_sorted():
    global array
    for i in range(len(array)):
        if i <= array_sorted_index:
            pygame.draw.rect(screen,array_sorted_color,(i*array_width,screen_height-array[i],array_width,array[i]))
        else:
            pygame.draw.rect(screen,array_color,(i*array_width,screen_height-array[i],array_width,array[i]))

def draw_array_unsorted():
    global array
    for i in range(len(array)):
        if i >= array_unsorted_index:
            pygame.draw.rect(screen,array_unsorted_color,(i*array_width,screen_height-array[i],array_width,array[i]))
        else:
            pygame.draw.rect(screen,array_color,(i*array_width,screen_height-array[i],array_width,array[i]))

def selection_sort():
    global array
    global array_sorted
    global array_unsorted
    global array_selected
    global array_selected_index
    global array_sorted_index
    global array_unsorted_index

    if array_sorted == False:
        if array_unsorted == True:
            if array_selected == False:
                array_selected_index = array_unsorted_index
                array_selected = True
            else:
                if array[array_selected_index] > array[array_unsorted_index]:
                    array_selected_index = array_unsorted_index
                array_unsorted_index += 1
                if array_unsorted_index == len(array):
                    array_unsorted_index = array_sorted_index + 1
                    array[array_selected_index],array[array_sorted_index] = array[array_sorted_index],array[array_selected_index]
                    array_sorted_index += 1
                    array_selected = False
                    if array_sorted_index == len(array)-1:
                        array_sorted = True
                        array_unsorted = False

def main():
    global array
    global array_sorted
    global array_unsorted
    global array_selected
    global array_selected_index
    global array_sorted_index
    global array_unsorted_index

    create_array()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        if array_sorted == False:
            selection_sort()
            draw_array_selected()
        else:
            draw_array_sorted()
        pygame.display.update()
        clock.tick(400)

main()
