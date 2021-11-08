import pygame

pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width, height))




pygame.display.set_caption("Flight Game, v.0.0.1")


sea = pygame.image.load('data/sea.png')
pygame.display.set_icon(sea)

cloud = pygame.image.load('data/cloud.png')

plane = pygame.image.load('data/plane.png')



backgroundcolor = (48, 131, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    screen.fill(backgroundcolor)

    screen.blit(sea, (1, 346))
    screen.blit(sea, (462, 346))
    screen.blit(cloud, (400, 100))
    screen.blit(cloud, (700, 100))
    
    pygame.display.update()



    