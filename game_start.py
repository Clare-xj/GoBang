from settings import Settings
from chessboard import Chessboard
from chesspoint import Chesspoint
import  game_functions as gf
import pygame
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Chess made by xujing")
    #对象
    chessboard=Chessboard(ai_settings,screen)
    chesspoints=[]
    occupied=[[0]*ai_settings.num for i in range(ai_settings.num)]
   

    while True:    
        screen.fill(ai_settings.bk_color)        
        gf.check_events(ai_settings,screen,chesspoints,occupied)
        gf.update_screen(ai_settings,screen,chessboard,chesspoints)
        pygame.display.flip()
        
run_game()