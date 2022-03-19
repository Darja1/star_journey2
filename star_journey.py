import pygame
pygame.init()

#library of game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (120, 120, 120)

WIDTH = 564
HEIGHT = 846
background = pygame.image.load('pygirls.jpg')

icon = pygame.image.load('background4357j.png')
pygame.display.set_icon(icon)

starIMG = pygame.transform.scale(pygame.image.load('star.png'), (300, 300))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game variables
star_x = 210
star_y = 520
platforms = [[ 267, 730, 200, 20]]


#create screen 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Star Journey')

running = True
while running == True:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    screen.blit(background,(0, 0))
    screen.blit(starIMG, (star_x, star_y))
    blocks = []

    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, black, platforms[i], 0, 3)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()