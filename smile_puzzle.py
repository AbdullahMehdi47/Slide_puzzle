import pygame, sys
from pygame.locals import *
import random

pygame.init()

# Display Screen
display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width, display_height))
display_rect = display.get_rect()

# Essentials
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Display Picture
Image_display = pygame.image.load("SmileScreen_Background.png")

# Center Rectangle
center_rectangle = Rect(0, 0, 498, 498)
center_rectangle.center = display_width // 2, display_height // 2

# Pictures of Rectangles
Image_1 = pygame.image.load("SmileScreen_1.png").convert()
rectangle_1 = Image_1.get_rect()
rectangle_1.update(391, 111, 166.6, 166.6)
Image_2 = pygame.image.load("SmileScreen_2.png").convert()
rectangle_2 = Image_2.get_rect()
rectangle_2.update(557, 111, 166.6, 166.6)
Image_3 = pygame.image.load("SmileScreen_3.png").convert()
rectangle_3 = Image_3.get_rect()
rectangle_3.update(723, 111, 166.6, 166.6)
Image_4 = pygame.image.load("SmileScreen_4.png").convert()
rectangle_4 = Image_4.get_rect()
rectangle_4.update(391, 277, 166.6, 166.6)
Image_5 = pygame.image.load("SmileScreen_5.png").convert()
rectangle_5 = Image_5.get_rect()
rectangle_5.update(557, 277, 166.6, 166.6)
Image_6 = pygame.image.load("SmileScreen_6.png").convert()
rectangle_6 = Image_6.get_rect()
rectangle_6.update(723, 277, 166.6, 166.6)
Image_7 = pygame.image.load("SmileScreen_7.png").convert()
rectangle_7 = Image_7.get_rect()
rectangle_7.update(391, 443, 166.6, 166.6)
Image_8 = pygame.image.load("SmileScreen_8.png").convert()
rectangle_8 = Image_8.get_rect()
rectangle_8.update(557, 443, 166.6, 166.6)

# List of all rectangles
all_rectangles = [rectangle_1, rectangle_2, rectangle_3, rectangle_4, rectangle_5, rectangle_6, rectangle_7, rectangle_8, center_rectangle]

# Movement Necessities
current_image = None
LeftButton = 0

rectangle_draging = False

# Game Title and Icon
pygame.display.set_caption("Smile Puzzle")
icon = pygame.image.load("smile.png")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("SansitaOne.tff", 25)

# Main Loop of game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Working on movement of rectangle
        if event.type == MOUSEBUTTONDOWN:
            if rectangle_8.collidepoint(event.pos):
                current_image = 1
            elif rectangle_7.collidepoint(event.pos):
                current_image = 2
            elif rectangle_6.collidepoint(event.pos):
                current_image = 3
            elif rectangle_5.collidepoint(event.pos):
                current_image = 4
            elif rectangle_4.collidepoint(event.pos):
                current_image = 5
            elif rectangle_3.collidepoint(event.pos):
                current_image = 6
            elif rectangle_2.collidepoint(event.pos):
                current_image = 7
            elif rectangle_1.collidepoint(event.pos):
                current_image = 8
            else:
                current_image = None

        if event.type == MOUSEMOTION:
            if event.buttons[LeftButton]:
                rel = event.rel
                if current_image == 1:
                    rectangle_8.x += rel[0]
                    rectangle_8.y += rel[1]
                    rectangle_8.clamp_ip(center_rectangle)
                elif current_image == 2:
                    rectangle_7.x += rel[0]
                    rectangle_7.y += rel[1]
                    rectangle_7.clamp_ip(center_rectangle)
                elif current_image == 3:
                    rectangle_6.x += rel[0]
                    rectangle_6.y += rel[1]
                    rectangle_6.clamp_ip(center_rectangle)
                elif current_image == 4:
                    rectangle_5.x += rel[0]
                    rectangle_5.y += rel[1]
                    rectangle_5.clamp_ip(center_rectangle)
                elif current_image == 5:
                    rectangle_4.x += rel[0]
                    rectangle_4.y += rel[1]
                    rectangle_4.clamp_ip(center_rectangle)
                elif current_image == 6:
                    rectangle_3.x += rel[0]
                    rectangle_3.y += rel[1]
                    rectangle_3.clamp_ip(center_rectangle)
                elif current_image == 7:
                    rectangle_2.x += rel[0]
                    rectangle_2.y += rel[1]
                    rectangle_2.clamp_ip(center_rectangle)
                elif current_image == 8:
                    rectangle_1.x += rel[0]
                    rectangle_1.y += rel[1]
                    rectangle_1.clamp_ip(center_rectangle)


    display.fill((0, 0, 0))
    pygame.draw.rect(display, RED, center_rectangle, 1)
    display.blit(Image_display, (0, 0))
    display.blit(Image_1, rectangle_1)
    display.blit(Image_2, rectangle_2)
    display.blit(Image_3, rectangle_3)
    display.blit(Image_4, rectangle_4)
    display.blit(Image_5, rectangle_5)
    display.blit(Image_6, rectangle_6)
    display.blit(Image_7, rectangle_7)
    display.blit(Image_8, rectangle_8)

    pygame.display.update()
