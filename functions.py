






import pygame
from math import *
from random import random
import time



XMAX = X=900
YMAX = Y =800

YELLOW = (255,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

true = True
false = False
TRUE = True
FALSE = False



def randomColor():
    R = random() * 250
    G = random() * 250
    B = random() * 250
    return (R,G,B)


def aggressive(s):
        answer = random()
        if(answer < s.aggressiveness):
            return True
        return False

def fearful(s):
        answer = random()
        if(answer < s.fear):
            return True
        return False
def productive(s):
        answer = random()
        if(answer < s.productivity):
            return True
        return False
    

def minDof(me,lista):
    x = me.xpos
    y = me.ypos
    dist = 10000
    chosen = 0
    for i in lista:
        dx = x - i.xpos
        dy = y - i.ypos
        distance = sqrt(dx ** 2 + dy ** 2)
        if(distance < dist):
            chosen = i
            dist = distance
    return chosen


def oneOf(lista):
    if(len(lista)> 0):
        result = int(random() * len(lista))
        return lista[result]
    
    return 0




def showWords(words, size, x, y,screen, color = (255,255,0)):
    myfont = pygame.font.SysFont("monospace", size)

# render text
    label = myfont.render(words, 1, color)
    screen.blit(label, (x, y))

def detectActionT(length,teams):
        for event in pygame.event.get():
            
            if(event.type == pygame.KEYDOWN ):
                color = BLACK
                if (event.key == pygame.K_ESCAPE):
                    return 2
                if (event.key == pygame.K_r):
                    color = RED
                elif (event.key == pygame.K_g):
                    color = GREEN
                elif (event.key == pygame.K_b):
                    color = BLUE
                elif (event.key == pygame.K_y):
                    color = YELLOW
                for t in teams:
                    
                    if(color == t.color):
                        t.create(length,t.xpos,t.ypos,t.Nsupplies)
            
def detectAction():
    for event in pygame.event.get():
        
        if(event.type == pygame.KEYDOWN ):
            
            if (event.key == pygame.K_ESCAPE):
                return false
            if (event.key == pygame.K_r):
                return true
#                if(MUTE):
#                    MUTE = false
#                else:
#                    MUTE = true
#            elif (event.key == pygame.K_SPACE ):
#                ship.shoot(L)
#
#            elif (event.key == pygame.K_UP):
#                ship.shootMissile(L)
#            elif (event.key == pygame.K_LEFT):
#                ship.direction = -1
#                ship.moving = true
#                ship.move()
#            elif (event.key == pygame.K_RIGHT):
#                ship.direction = 1
#                ship.moving = true
#                ship.move()
#        elif(event.type == pygame.KEYUP ):
#                ship.moving = false
                
                
            
    return 2

def thoseWith(lista,attribute):
    result = [obj for obj in list if(hasattrobj,attribute)]
    
    return result

def thoseWithout(lista,attribute):
    result = []
    for i in lista:
        if(not hasattr(i,attribute)):
            result.append(i)

    return result

def thoseWithT(attribute,lista):
    result = []
    for i in lista:
        if(attribute(*i)):
            result.append(i)

    return result

def thoseWithF(lista,attribute):
    result = [obj for obj in list ]
    for i in lista:
        if(not attribute(i)):
            result.append(i)

    return result       




