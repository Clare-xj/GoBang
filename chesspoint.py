import pygame
import sys
import os
class Chesspoint():
    def __init__(self,ai_settings,screen,x,y):
        self.screen=screen
        if ai_settings.is_black==True:
            self.color=ai_settings.BLACK
        else :
            self.color=ai_settings.WHITE
          
        #逻辑位置
        self.x=x
        self.y=y
       
        #屏幕显示位置
        self.posx=ai_settings.left+ai_settings.space*x
        self.posy=ai_settings.top+ai_settings.space*y
        self.R=ai_settings.r
        
    

    def blitme(self):
        pygame.draw.circle(self.screen, self.color,(self.posx,self.posy), self.R)
        