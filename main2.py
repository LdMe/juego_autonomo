from classes import *


def main():
    

    game = pygame.init()
    fondo = pygame.image.load("ground.png")
    fondo = pygame.transform.scale(fondo,(900,800))
    screen = pygame.display.set_mode((900,800))
    length = 20
    lista = []
    teams = []
    red = team(RED,"red")
    blue = team(BLUE,"blue")
    green = team(GREEN,"green")
    yellow = team(YELLOW,"yellow")
    
    s5= Supplies(400,400,40,BLACK)
    
    red.create(length,random() * 100,random() * 100,s5)
    blue.create(length,random() * 100 + 700,random() * 100,s5)
    green.create(length,random() * 100 + 700,random() * 100 + 700,s5)
    yellow.create(length,random() * 100,random() * 100 + 700,s5)

    teams.append(red)
    teams.append(green)
    teams.append(blue)
    teams.append(yellow)         
    
 #   pygame.mouse.set_visible(0)
    i = 0
    while(1):
 #       red.enemies = blue.list + green.list + yellow.list
#        green.enemies = red.list + blue.list + yellow.list
#        blue.enemies = green.list + red.list + yellow.list
#        yellow.enemies = blue.list + red.list + green.list
        screen.blit(fondo ,(0,0))
        for t in teams:
            t.enemies = []
            for e in teams:
                if(e.name != t.name):
                    t.enemies= t.enemies + e.list
            t.challenge(screen)
 #           a = thoseWithT(aggressive,t.list)
#            print "agressiveness" , len(a)
        if(detectActionT(length,teams)):
            return
 #       red.challenge(screen)
#        green.challenge(screen)
#        blue.challenge(screen)
#        yellow.challenge(screen)

        
        showWords("red",Y / 30,X * 0.78, Y * 0.80, screen, RED)
        showWords(str(red.points),Y / 30,X * 0.87, Y * 0.80, screen, RED)
        showWords("/",Y / 30,X * 0.92, Y * 0.80, screen, RED)
        showWords(str(len(red.list)),Y / 30,X * 0.94, Y * 0.80, screen, RED)
        showWords("green",Y / 30,X * 0.77, Y * 0.85, screen, GREEN)
        showWords(str(green.points),Y / 30,X * 0.87, Y * 0.85, screen, GREEN)
        showWords("/",Y / 30,X * 0.92, Y * 0.85, screen, GREEN)
        showWords(str(len(green.list)),Y / 30,X * 0.94, Y * 0.85, screen, GREEN)
        showWords("blue",Y / 30,X * 0.78, Y * 0.90, screen, BLUE)
        showWords(str(blue.points),Y / 30,X * 0.87, Y * 0.90, screen, BLUE)
        showWords("/",Y / 30,X * 0.92, Y * 0.90, screen, BLUE)
        showWords(str(len(blue.list)),Y / 30,X * 0.94, Y * 0.90, screen, BLUE)

        showWords("yellow",Y / 30,X * 0.76, Y * 0.94, screen, YELLOW)
        showWords(str(yellow.points),Y / 30,X * 0.87, Y * 0.94, screen, YELLOW)
        showWords("/",Y / 30,X * 0.92, Y * 0.94, screen, YELLOW)
        showWords(str(len(yellow.list)),Y / 30,X * 0.94, Y * 0.94, screen, YELLOW)
        pygame.display.update()
        if(detectAction()):
            return
        for i in teams:
            if(i.points >= 100 *length and not i.winner):
                i.winner = true
                print i.name,"team wins" 

        for j in teams:
            if(j.winner):                              
                time.sleep(3)
                return
        
 #       i= i + 1
    
        

def main2():
    

    game = pygame.init()
    fondo = pygame.image.load("ground.png")
    fondo = pygame.transform.scale(fondo,(900,800))
    screen = pygame.display.set_mode((900,800))
    length = 10
    team_qty = 10
    
    supply_qty = 5
    lista = []
    teams = []
    supplies = []
    
    for i in range(supply_qty):
        
        s5= Supplies(random() * 800,random() * 800,20,BLACK)
        supplies.append(s5)
    for i in range(team_qty):
        color = randomColor()
        t = team(color,str(color))
        t.create(length,random() * 800,random() * 800,supplies)
        teams.append(t)
          
    
 #   pygame.mouse.set_visible(0)
    i = 0
    while(1):
 #       red.enemies = blue.list + green.list + yellow.list
#        green.enemies = red.list + blue.list + yellow.list
#        blue.enemies = green.list + red.list + yellow.list
#        yellow.enemies = blue.list + red.list + green.list
        screen.blit(fondo ,(0,0))
        for t in teams:
            t.enemies = []
            for e in teams:
                if(e.name != t.name):
                    t.enemies= t.enemies + e.list
            t.challenge(screen)
 #           a = thoseWithT(aggressive,t.list)
#            print "agressiveness" , len(a)
 #       if(detectActionT(length,teams)):
#            return
 #       red.challenge(screen)
#        green.challenge(screen)
#        blue.challenge(screen)
#        yellow.challenge(screen)

        
 #       showWords("red",Y / 30,X * 0.78, Y * 0.80, screen, RED)
#        showWords(str(red.points),Y / 30,X * 0.87, Y * 0.80, screen, RED)
 #       showWords("/",Y / 30,X * 0.92, Y * 0.80, screen, RED)
#        showWords(str(len(red.list)),Y / 30,X * 0.94, Y * 0.80, screen, RED)
#        showWords("green",Y / 30,X * 0.77, Y * 0.85, screen, GREEN)
#        showWords(str(green.points),Y / 30,X * 0.87, Y * 0.85, screen, GREEN)
#        showWords("/",Y / 30,X * 0.92, Y * 0.85, screen, GREEN)
#        showWords(str(len(green.list)),Y / 30,X * 0.94, Y * 0.85, screen, GREEN)
#        showWords("blue",Y / 30,X * 0.78, Y * 0.90, screen, BLUE)
#        showWords(str(blue.points),Y / 30,X * 0.87, Y * 0.90, screen, BLUE)
#        showWords("/",Y / 30,X * 0.92, Y * 0.90, screen, BLUE)
#        showWords(str(len(blue.list)),Y / 30,X * 0.94, Y * 0.90, screen, BLUE)

#        showWords("yellow",Y / 30,X * 0.76, Y * 0.94, screen, YELLOW)
#        showWords(str(yellow.points),Y / 30,X * 0.87, Y * 0.94, screen, YELLOW)
#        showWords("/",Y / 30,X * 0.92, Y * 0.94, screen, YELLOW)
#        showWords(str(len(yellow.list)),Y / 30,X * 0.94, Y * 0.94, screen, YELLOW)
        pygame.display.update()
        detect = detectAction()
        if(detect != 2):
            return detect
        for i in teams:
            if(i.points >= 100 *length and not i.winner):
                i.winner = true
                print i.name,"team wins" 

        for j in teams:
            if(j.winner):                              
                time.sleep(3)
                return true
        
 #       i= i + 1
    
  
restart = true
while(restart):
     restart = main2()




