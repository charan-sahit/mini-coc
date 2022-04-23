        

import colorama
from colorama import Back, Fore, Style
import time

class WizardTower:
    towersList = []
    limit = [2,3,4]
    def __init__(self,xCoordinate,yCoordinate):
        self.coordinates = [xCoordinate,yCoordinate]
        self.health = 10
        self.occupied = False
        self.victim = None
        self.target = None
        self.init = time.time()
        self.death = False
        self.area = [0,0]
        self.fly = True
        
    def render(self,colorArray,):
         
        ## canons
        
        if(self.health>0):
            
            self.color = Back.WHITE+ " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL
            self.death = True
        
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self, idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 14
        return idArray

    def shoot(self,king,Barbarians, Archers, Balloons):
        min_distance = 10
        #print(self.occupied)
        self.target = None
        if(self.victim!=None):
            if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                            
                #print('yess')
                pass
            else:
                #print('nooo')
                self.victim = None
                self.occupied = False
        if(abs(king.coordinates[0]-self.coordinates[0])<5 and abs(king.coordinates[1]-self.coordinates[1])<5 and king.death == False):
            distance = abs(king.coordinates[0]-self.coordinates[0]) + abs(king.coordinates[1]-self.coordinates[1])
            if(distance<min_distance):
                min_distance = distance
                self.target = king
        for barbarian in Barbarians.barbariansList:
            if(abs(barbarian.coordinates[0]-self.coordinates[0])<5 and abs(barbarian.coordinates[1]-self.coordinates[1])<5):
                distance = abs(barbarian.coordinates[0]-self.coordinates[0]) + abs(barbarian.coordinates[1]-self.coordinates[1])
                if(barbarian.death == False):
                    if(distance<min_distance):
                        min_distance = distance
                        self.target = barbarian
        for archer in Archers.archersList:
            if(abs(archer.coordinates[0]-self.coordinates[0])<5 and abs(archer.coordinates[1]-self.coordinates[1])<5):
                distance = abs(archer.coordinates[0]-self.coordinates[0]) + abs(archer.coordinates[1]-self.coordinates[1])
                if(archer.death == False):
                    if(distance<min_distance):
                        min_distance = distance
                        self.target = archer
        for balloon in Balloons.balloonsList:
            distance = abs(balloon.coordinates[0]-self.coordinates[0]) + abs(balloon.coordinates[1]-self.coordinates[1])
            
            if(abs(balloon.coordinates[0]-self.coordinates[0])<5 and abs(balloon.coordinates[1]-self.coordinates[1])<5):
                
                if(balloon.death == False):
                    
                    if(distance<min_distance):
                        print('hi')
                        min_distance = distance
                        self.target = balloon
        
        if(self.target!=None):
            if(self.occupied==False):
                self.victim = self.target
                self.occupied = True
            
                
                if(min_distance<10):
                    self.victim.health -= 1
                    self.occupied = True
                    if(self.victim.health <=0):
                        self.victim = None
                        self.occupied = False

                    

                    
            else:
                #print(self.coordinates, self.victim.coordinates)
                #print(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[0]-self.coordinates[0])<5)
                if(self.target != self.victim):
                    if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                        
                        pass
                        #print('yes')
                    else:
                        self.victim = self.target
                #print(self.victim)
                if(time.time()-self.init > 1):
                    self.init = time.time()
                    self.victim.health -= 1
                if(self.victim.health <=0):
                    self.victim = None
                    self.occupied = False
            if(self.victim != None):
                self.area = [self.victim.coordinates[0],self.victim.coordinates[1]]
                #print(self.area[0],self.area[1])
                for i in range(6):
                    for j in range(6):
                        
                        x = self.area[0] + i - 3
                        y = self.area[1] + j - 3
                        for barbarian in Barbarians.barbariansList:
                            
                            #print('diff',barbarian.coordinates[0]-x,barbarian.coordinates[1]-y)
                            if(barbarian.coordinates[0]==x and barbarian.coordinates[1]==y):
                                
                                barbarian.health -= 1
                                if(barbarian.health <=0):
                                    barbarian.death = True
                                    self.occupied = False
                                    self.victim = None
                                    self.area = [0,0]
                        
                        for archer in Archers.archersList:
                            if(archer.coordinates[0]==x and archer.coordinates[1]==y):
                                archer.health -= 1
                                if(archer.health <=0):
                                    archer.death = True
                                    self.occupied = False
                                    self.victim = None
                                    self.area = [0,0]
                        
                        if(king.coordinates[0]==x and king.coordinates[1]==y):
                            king.health -= 1
                            if(king.health <=0):
                                king.death = True
                                self.occupied = False
                                self.victim = None
                                self.area = [0,0]

        