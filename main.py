import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Load background image
try:
    BG = pygame.transform.scale(pygame.image.load("bg.jpeg")
except pygame.error:
    print("Error: Unable to load 'bg.jpeg'. Please check the file path.")
    exit()

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()  # Fixed typo

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()
    
if __name__ == "__main__":
    main()
