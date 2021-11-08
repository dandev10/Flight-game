import pygame

pygame.init()


screen = pygame.display.set_mode((600, 800))

pygame.display.set_caption("Flight Game, v.0.0.1")

backgroundcolor = (93, 115, 240)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    screen.fill(backgroundcolor)

    
    pygame.display.update()



    