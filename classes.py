from functions import *
import time

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
#        image.set_alpha(0)
        image.blit(self.sheet, (0, 0), rect)
        #if colorkey == None:
            
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


class Supplies:
    def __init__(self,xpos,ypos,size = X / 20,color = BLACK):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color = color
        self.rect = pygame.Rect(xpos,ypos,size,size)
    def show(self,s):
        pygame.draw.rect(s,self.color,self.rect)
    def supply(self,l):
        for i in l:
            if(abs(self.xpos - i.xpos)+ abs(self.ypos - i.ypos)< self.size ):
                    if(i.resources < i.max_resources):
                        i.resources = i.resources + 1
                        i.ammo = 0
                        i.dx = - i.dx
                        i.dy = - i.dy
                        i.angle = i.angle + pi
    def act(self,s,l):
        for i in l:
            if(abs(self.xpos - i.xpos)+ abs(self.ypos - i.ypos)< self.size and self.color == i.color):
                if(i.ammo < i.max_ammo):
                    i.ammo = i.ammo + 1
    def invest(self,team):
        for i in team.list:
            if(abs(self.xpos - i.xpos)+ abs(self.ypos - i.ypos)< self.size and self.color == i.color):
                if(i.resources > 0 and team.points > 0):
                    i.resources = i.resources - 1
                    team.points = team.points - 1
                    i.invest(team)
            
        
        
    
class shots:
    def __init__(self, x= 0,y = 0,dx = 0,dy = 0,angle = 0,color =BLACK):
        self.xpos = int(x)
        self.ypos = int(y)
        self.radius = 2
        self.dead = false
        self.start_time = time.time()
    #    self.image = pygame.image.load()
        self.speed = 5
        self.dx = dx
        self.dy = dy
        self.angle = angle
        self.color = color
    def move(self,s):
        if (time.time() - self.start_time > 1):
           self.dead =TRUE 
        self.xpos += int(self.speed * self.dx)
        self.ypos += int(self.speed * self.dy)
        pygame.draw.circle(s,self.color,(self.xpos,self.ypos),self.radius)
        if(self.xpos > XMAX or self.xpos < 0 or self.ypos > YMAX or self.ypos < 0):
            self.dead = TRUE
    def die(self,enemy):
        if(abs(self.xpos - enemy.xpos)+ abs(self.ypos - enemy.ypos)< enemy.size and self.color != enemy.color):
            self.dead = TRUE
            enemy.life = enemy.life - 1
            if(enemy.life <=0):
                enemy.dead = TRUE
                return true
        return false

class team:
    def __init__(self,color,name ):
        self.color = color
        self.points = 0
        self.name = name
        self.xpos = 0
        self.ypos = 0
        self.winner = false
        self.list = []
        self.enemies = []
        self.supplies = []
        self.Nsupplies = []
        self.shotList = []
    def create(self,length,x,y,nsupplies):
        for i in range(length):
            p1 = villager(self.color,random() * 800,random() * 800,10,10)
            self.list.append(p1)
        s1 = Supplies(x,y,40,self.color)
        self.supplies.append(s1)
        self.xpos = s1.xpos
        self.ypos = s1.ypos
        if(type(nsupplies)!= list):
            self.Nsupplies.append(nsupplies)
        else:
            self.Nsupplies = self.Nsupplies + nsupplies

    
                    
    def challenge(self,screen):
        for s in self.supplies:
            s.act(screen,self.list)
            s.invest(self)
            s.show(screen)
        for n in self.Nsupplies:
            n.supply(self.list)
            n.show(screen)
        for i in self.list:
            i.challenge(self,screen)
            
        for j in self.shotList:
            j.move(screen)
            for i in self.enemies:
                
                if(j.die(i)):
                    self.points= self.points + 2
            if(j.dead):
                self.shotList.remove(j)
    def play(self,enemies,screen):
        for s in self.supplies:
            s.act(screen,self.list)
            s.show(screen)
        for i in self.list:
            if(random() < 0.1 and i.ammo > 0):
                i.shoot(oneOf(enemies),self.shotList)
            
            minSup = minDof(i,self.supplies)
            if(minSup != 0):
                
                i.findSupply(minDof(i,self.supplies))
            
            
            
            if( i.fearful()):
                
                minimo = minDof(i,enemies)
                if(minimo != 0 ):
                    i.runaway(minimo)
                
            if(random()< 0.01):
                i.facePos(int(random() * X),int(random() * Y))
            i.move()
            i.show(screen)
            if(i.dead):
                self.list.remove(i)
        for j in self.shotList:
            j.move(screen)
            for i in enemies:
                
                if(j.die(i)):
                    self.points= self.points + 1
            if(j.dead):
                self.shotList.remove(j)

class villager:
    def __init__(self, color,x= 0,y = 0,size = 40,life = 10):
        self.xpos = x
        self.ypos = y
        self.life = life
        self.maxlife = life
        self.shots = []
        self.ammo = 0
        self.productivity = random() * 0.5
        self.fear = random() * 0.1
        self.accuracy = random()
        self.aggressiveness = random()
        self.fear = random() * 0.3
        self.resources = 0
        self.max_resources = 2
        self.max_ammo = 3
        self.num_shots =1
        self.generation = 0
        self.size = size
        self.rect = pygame.Rect(x,y,size,size)
    #    self.image = pygame.image.load()
        self.speed = 4
        self.dx = 0.00
        self.dead = false
        self.dy = 0.00
        self.angle = 0.00
        self.color = color

    def invest(self,team):
        if(self.resources > 0):
            son = villager(self.color,self.xpos,self.ypos ,self.size ,self.maxlife)
            son.born(self)
            team.list.append(son)
    def born (self,father):
        self.generation = father.generation + 1
        print self.generation, int (100 * self.productivity),int (100 * self.aggressiveness),int (100 * self.accuracy), int(100* self.fear)
        self.fear = father.fear + random() * 0.2 - 0.1
        self.productivity = father.productivity + random() * 0.2 - 0.1
        self.accuracy = father.accuracy + random() * 0.2 - 0.1
        self.aggressiveness = father.aggressiveness + random() * 0.2 - 0.1
    def challenge(self,team,screen):
        enemies = team.enemies
        if(aggressive(self) and self.ammo > 0):
            self.shoot(oneOf(enemies),team.shotList)
        minSup = minDof(self,team.supplies)
        if(minSup != 0):
                
                self.findSupply(minSup,"ammo")
        else:
            print("error_ammo")
        if(productive(self)):           
            minSup =minDof(self,team.Nsupplies)
            if(minSup != 0):
                self.findSupply(minSup,"resources")
            else:
                print("error_resources")
        
        if( fearful(self)):
                
                minimo = minDof(self,team.enemies)
                if(minimo != 0 and self.Distance(minimo)< 100):
                    self.runaway(minimo)
        if(random() < 0.01):
                self.facePos(int(random() * X),int(random() * Y))
        self.move()
        self.show(screen)
        if(self.dead):
                team.list.remove(self)
       
    def facePos(self, xpos,ypos):
        x = xpos - self.xpos
        y = ypos - self.ypos
        if(x == 0):
            if(y < 0):
                self.angle = -pi / 2
            else:
                
                self.angle = pi / 2
        if( y == 0):
            if(x > 0):
                self.angle = pi
            else:
                self.angle = 0
        if(x != 0 and  y != 0):
            self.angle = atan(y / x)
        if( x < 0):
            self.angle = self.angle + pi
        
        self.dx = cos(self.angle)
        self.dy = sin(self.angle)
        return
    def face(self,someone):
        x = someone.xpos - self.xpos
        y = someone.ypos - self.ypos
        if(x == 0):
            if(y < 0):
                self.angle = -pi / 2
            else:
                
                self.angle = pi / 2
        if( y == 0):
            if(x > 0):
                self.angle = pi
            else:
                self.angle = 0
        if(x != 0 and  y != 0):
            self.angle = atan(y / x)
        if( x < 0):
            self.angle = self.angle + pi
        
        self.dx = cos(self.angle)
        self.dy = sin(self.angle)
        
        
        
        return
    def findSupply(self,supply,kind = "ammo"):
        if(kind == "ammo"):
            if(self.ammo == 0):
                self.face(supply)
        else:
             if(self.resources == 0):
                self.face(supply)
    def Distance(self,someone):
        x= someone.xpos - self.xpos
        y = someone.ypos - self.ypos
        d = sqrt(x**2 + y **2)
        return d
    def shoot(self,someone,l):
        
            
        if(someone != 0 and self.ammo > 0):
            self.face(someone)  
            x = someone.xpos - self.xpos
            y = someone.ypos - self.ypos
            if(abs(x + y)< 100 and len(self.shots) < self.num_shots):
                coord = self.miss()
                dx = coord[0]
                dy = coord[1]
                shot1 = shots(self.xpos,self.ypos,dx,dy,self.angle,self.color)
                self.shots.append(shot1)
                l.append(shot1)
                self.ammo = self.ammo - 1
        
    def runaway(self,someone):
        self.face(someone)
        self.angle = self.angle + pi
        self.dx = -self.dx
        self.dy = -self.dy
    def miss(self):
        angle = self.angle + (random() * 2 - 1) * (1 - self.accuracy)
        x = cos(angle)
        y = sin(angle)
        return(x,y)
    def move(self):
        
        self.xpos += self.speed * self.dx
        self.ypos += self.speed * self.dy
        if(self.xpos > XMAX):
            self.xpos = XMAX
            self.dx = -self.dx
        elif(self.xpos < 0):
            self.xpos = 0
            self.dx = -self.dx
        if(self.ypos > YMAX):
            self.ypos = YMAX
            self.dy = -self.dy
        elif(self.ypos < 0):
            self.ypos = 0
            self.dy = -self.dy
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        
        
    def show(self,s):
        pygame.draw.rect(s,self.color,self.rect)
        for i in self.shots:
            
            if(i.dead):
                self.shots.remove(i)
    


