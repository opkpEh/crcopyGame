import pygame
from sys import exit  

pygame.init()
screen= pygame.display.set_mode((720, 1080))
pygame.display.set_caption("CR_COPY")
clock = pygame.time.Clock()

BattleArena= pygame.image.load('graphics/arena.png').convert()
tower= pygame.image.load('graphics/castle.png').convert()
barbrian = pygame.image.load('graphics/barbrian.png').convert_alpha()

barbrian_x_pos= 80
barbrian_y_pos= 850

barbrian2_x_pos= 585
barbrian2_y_pos= 210

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    # update everything

    screen.blit(BattleArena,(0,0)) # block image transfter (fancy word for saying that i want to put one surface on another)
    screen.blit(tower,(273,800))

    screen.blit(barbrian,(barbrian_x_pos,barbrian_y_pos))
    barbrian_y_pos -= 3
    
    screen.blit(barbrian,(barbrian2_x_pos,barbrian2_y_pos))
    barbrian2_y_pos +=3

    if barbrian_y_pos< 200:
        barbrian_y_pos= 850

    if barbrian2_y_pos> 810:
        barbrian2_y_pos= 210

    pygame.display.update()
    clock.tick(60)
    