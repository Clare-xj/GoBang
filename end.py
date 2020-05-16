import pygame
def end_interface(ai_settings,screen):
    font=pygame.font.SysFont(None,60)
    if ai_settings.is_black:
        text=font.render("BLACK WIN",True,(255,200,10))
        screen.blit(text, (250,300))
    else:
        text=font.render("WHITE WIN",True,(255,200,10))
        screen.blit(text, (250,300))


	
	