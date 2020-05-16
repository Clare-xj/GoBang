import pygame
def font(screen):
    font=pygame.font.SysFont('microsoft Yahei',60)
    surface1=font.render('Restart',False,(255,200,10))
    surface2=font.render('Retract',False,(255,200,10))
    surface3=font.render('End',False,(255,200,10))
    screen.blit(surface1,(720,200))
    screen.blit(surface2,(720,320))
    screen.blit(surface3,(720,440))
    

