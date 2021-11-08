import pygame, time
pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flight Game, v.0.2.0")


move_forward = False
move_down = False
move_up = False
planeX = 50 
planeY = 175
black = (0, 0, 0)
white = (255, 255, 255)


sea = pygame.image.load('data/sea.png')
pygame.display.set_icon(sea)
cloud = pygame.image.load('data/cloud.png')
plane = pygame.image.load('data/plane.png')
backgroundcolor = (48, 131, 255)


def create_plane():
    screen.blit(plane, (planeX, planeY))

def create_sea(posx, posy):
    screen.blit(sea, (posx, posy))

def create_cloud(posx, posy):
    screen.blit(cloud, (posx, posy))

def create_text():
    font = pygame.font.SysFont("arial",  20, bold = pygame.font.Font.bold)
    whole_text = ("plane 1: X: ", planeX, "Y: ", planeY)
    text = font.render(str(whole_text), True, black, backgroundcolor)
    screen.blit(text, (width/2, height/2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_forward = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_forward = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False
        
    if move_forward:
        planeX += 0.3
    if move_up:
        planeY -= 0.3
    if move_down:
        planeY += 0.3

    #if planeY >= 190:
        #running = False

    if planeX >= 700:
        planeX = -100

    #planeX += 0.1

    screen.fill(backgroundcolor)

    create_text()
    create_sea(1, 392)
    create_sea(462, 392)
    create_cloud(400, 100)
    create_cloud(700, 100)
    create_plane()
    
    
    
    pygame.display.update()



    