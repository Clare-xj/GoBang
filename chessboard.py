import pygame
import sys
import os
class Chessboard():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.color=ai_settings.YELLOW
        self.rect=pygame.Rect(0,0,ai_settings.chessboard_width,ai_settings.chessboard_height)

    def blitme(self):
       
        pygame.draw.rect(self.screen,self.color,self.rect)
        dist=40
        line=17
        top=20
        left=20

        pygame.draw.line(self.screen,(0,0,0),(0,0),(dist*line,0),2)
        pygame.draw.line(self.screen,(0,0,0),(0,0),(0,dist*line),2)
        pygame.draw.line(self.screen,(0,0,0),(dist*line,0),(dist*line,dist*line),2)
        pygame.draw.line(self.screen,(0,0,0),(0,dist*line),(dist*line,dist*line),2)

        pygame.draw.circle(self.screen,(0,0,0),[top+dist*5,left+dist*5],5)
        pygame.draw.circle(self.screen,(0,0,0),[top+dist*11,left+dist*5],5)
        pygame.draw.circle(self.screen,(0,0,0),[top+dist*5,left+dist*11],5)
        pygame.draw.circle(self.screen,(0,0,0),[top+dist*11,left+dist*11],5)
        
        for x in range(0,line+1):
            pygame.draw.line(self.screen,(0,0,0),(-top+dist*x,-left+dist),(-top+dist*x,-left+dist*line),2)
            pygame.draw.line(self.screen,(0,0,0),(-top+dist,-left+dist*x),(-top+dist*line,-left+dist*x),2)
        