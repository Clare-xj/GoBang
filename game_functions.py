import sys
import pygame
import end as end
import font as f
from chesspoint import Chesspoint

def check_gameover(ai_settings,chesspoints):
    line_direct=[(1,0),(0,1),(1,1),(1,-1)]
    for direct in line_direct:
        if judge_line(ai_settings,direct,chesspoints):
            return True
    return False


def judge_line(ai_settings,direct,chesspoints):
    dx,dy=direct
    last=chesspoints[-1]
    line=[]
    for cp in chesspoints:
        cx=cp.x-last.x
        cy=cp.y-last.y
        if dx*cy==dy*cx and last.color==cp.color:
           line.append(cp)

    if len(line)>=5:
        sorted_line=sorted(line,key=lambda chesspoint: chesspoint.x)
        print(sorted_line[4].x)
        if sorted_line[4].x==sorted_line[0].x and (sorted_line[4].y-sorted_line[0].y)==4 :
            return True
        elif sorted_line[4].x-sorted_line[0].x==4:
            return True
    return False


def check_pos(ai_settings,x,y,chesspoints,occupied): 
    num=int(ai_settings.num)
    if(x>0 and  x<num and y >0 and y<num  and occupied[x][y]==0):
        return True
    else :
        if x>num and y==5:
            Restart(ai_settings,chesspoints,occupied)
        elif x>num and y==8:
            Retract(ai_settings,chesspoints,occupied)
        elif x>num and y==11:
            Gameover(ai_settings)

        return False


def add_point(ai_settings,screen,posx,posy,chesspoints,occupied):
    x=int(round((posx-ai_settings.top)/ai_settings.space))
    y=int(round((posy-ai_settings.left)/ai_settings.space))
    judge=check_pos(ai_settings,x,y,chesspoints,occupied)
    if judge==True:
        chesspoint=Chesspoint(ai_settings,screen,x,y)
        occupied[x][y]=1
        chesspoints.append(chesspoint)
        if check_gameover(ai_settings,chesspoints):
            ai_settings.game_over=True
        else:
            ai_settings.is_black=  not ai_settings.is_black
    

def check_events(ai_settings,screen,chesspoints,occupied):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            (posx,posy)=pygame.mouse.get_pos()
            add_point(ai_settings,screen,posx,posy,chesspoints,occupied)

def Restart(ai_settings,chesspoints,occupied):
    chesspoints.clear()
    for i in range(ai_settings.num):
        for j in range(ai_settings.num):
            occupied[i][j]=0
    ai_settings.is_black=True
    ai_settings.game_over=False

def Retract(ai_settings,chesspoints,occupied):
    chess=chesspoints.pop()
    ai_settings.is_black = not ai_settings.is_black
    occupied[chess.x][chess.y]=0


def Gameover(ai_settings):
    ai_settings.game_over=True
    pygame.QUIT
    sys.exit()



def update_screen(ai_settings,screen,chessboard,chesspoints):
   # if ai_settings.game_over==False :
        chessboard.blitme()
        f.font(screen)
        for cp in chesspoints:
            cp.blitme()
        if ai_settings.is_black:
            pygame.draw.circle(screen,(0,0,0),(790,100), 30)
        else :
            pygame.draw.circle(screen,(255,255,255),(790,100), 30)
        if ai_settings.game_over==True:
            endings=end.end_interface(ai_settings,screen)
        pygame.display.flip()
        

