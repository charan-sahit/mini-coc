from tabnanny import check
from colorama import Fore, Back, Style
import math

from numpy import minimum

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

class Balloons:
    balloonsList = []
    velocity = 2
    limit= [5,8,10]
    def __init__(self,xCoordinate,yCoordinate):
        self.coordinates = [xCoordinate,yCoordinate]
        self.health = 10
        self.death = False
        self.target = None
        self.occupied = False
        self.available = False
        self.victim = None
    
    def render(self,colorArray):
        ## balloons
        if(self.health>0):
            self.color = Back.BLUE + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
            self.death = True
        
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray

    def idUpdate(self,idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 11
        return idArray

    def choose(self,Building, WizardTower):
        
        min_distance = 100
        
        if(self.occupied==False):
            for building in Building.buildingList:
                if(building.wall==False and building.fly == True):
                    if(building.death==False):
                        self.available = True
                    if(distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])<min_distance):
                        

                        
                        if(building.death==False):
                            self.target = building
                            self.occupied = True
                            check = True
                            min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
                            
          
            for tower in WizardTower.towersList:
                if(tower.death==False):
                    self.available = True
                if(distance(self.coordinates[0],self.coordinates[1],tower.coordinates[0],tower.coordinates[1])<min_distance):
                    if(tower.death == False):
                        self.target = tower
                        self.occupied = True
                        min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
            

            if(self.available == False):
                
                for building in Building.buildingList:
                    if(building.wall==False):
                        if(distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])<min_distance):
                            

                            
                            if(building.death==False):
                                self.target = building
                                self.occupied = True
                                
                                check = True
                                min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])

            
            if(self.target!=None):
                self.victim = self.target
                self.target = None
                
                

    """ def move(self):
        check = True
        print(check)
        if(self.victim!=None):

            print('vic',self.victim, self.victim.coordinates[0],self.victim.coordinates[1],self.coordinates[0],self.coordinates[1])
        if(self.occupied == True):
            print(1)
            if(self.victim.coordinates[0]>self.coordinates[0]):
                self.coordinates[0] += self.velocity
            elif(self.victim.coordinates[0]<self.coordinates[0]):
                self.coordinates[0] -= self.velocity
            elif(self.victim.coordinates[1]>self.coordinates[1]):
                self.coordinates[1] += self.velocity
            elif(self.victim.coordinates[1]<self.coordinates[1]):
                self.coordinates[1] -= self.velocity
            
            if(self.victim.coordinates[0]==self.coordinates[0] and self.victim.coordinates[1]==self.coordinates[1]):
                self.victim.health -= 1
            if(self.victim.health <= 0):
                check = False
                self.victim.death = True
                self.victim = False
                self.occupied = False
             """

    """ def choose(self,Building, WizardTower):
        check = False
        print("Target",self.target)
        if(self.target != None):
            print('Distance',abs(self.coordinates[0]-self.target.coordinates[0]),abs(self.coordinates[1]-self.target.coordinates[1]))
        #if(self.occupied == False):
        if(self.target == None):
            print('barbPeek')
            min_distance = 1000
            for building in Building.buildingList:
                if(building.wall==False):
                    if(distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])<min_distance):
                        

                        
                        if(building.death==False):
                            self.target = building
                            check = True
                            min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
                        
            if(check == True):
                self.occupied = True
        if(self.target != None): 
               
            if(self.target.health<=0):
                
                print(1789)
                self.target = None
                self.occupied = False
     """
    """ def move(self,idArray,wallsList):
        if(self.target!=None):
            print(self.target.health)
            print('th',self.target.coordinates[0],self.target.coordinates[1])
            if(abs(self.coordinates[0]-self.target.coordinates[0])==1 or abs(self.coordinates[1]-self.target.coordinates[1])==1):
                self.velocity = 1
            else:
                self.velocity = 2
            if(self.coordinates[0]<self.target.coordinates[0]):
                #if(idArray[self.coordinates[0]+1][self.coordinates[1]]==0 or idArray[self.coordinates[0]+1][self.coordinates[1]]==9):
                self.coordinates[0]+=self.velocity
                
            elif(self.coordinates[0]>self.target.coordinates[0]):
                #if(idArray[self.coordinates[0]-1][self.coordinates[1]]==0 or idArray[self.coordinates[0]-1][self.coordinates[1]]==9):
                self.coordinates[0]-=self.velocity
                
            elif(self.coordinates[1]<self.target.coordinates[1]):
                #if(idArray[self.coordinates[0]][self.coordinates[1]+1]==0 or idArray[self.coordinates[0]][self.coordinates[1]+1]==9):
                self.coordinates[1]+=self.velocity
                
            elif(self.coordinates[1]>self.target.coordinates[1]):
                #if(idArray[self.coordinates[0]][self.coordinates[1]-1]==0 or idArray[self.coordinates[0]][self.coordinates[1]-1]==9):
                self.coordinates[1]-=self.velocity
                
            if(abs(self.coordinates[0]-self.target.coordinates[0])<=3 and abs(self.coordinates[1]-self.target.coordinates[1])<=3):
                self.target.health-=2
                if(self.target.health<=0):
                    print(2)
                    self.occupied = False
                    self.target = None 
            
            elif(self.target.coordinates[0]==20 and self.target.coordinates[1]==40 and abs(self.coordinates[0]-self.target.coordinates[0])<=3 and abs(self.coordinates[1]-self.target.coordinates[1])<=2):
                print('touch')
                self.target.health-=1
                if(self.target.health<=0):
                    print(3)
                    self.occupied = False
                    self.target = None
                    self.death = True
            
        return idArray """

    def move(self,idArray,wallsList):
        if(self.victim==None):
            self.available = False
        if(self.victim!=None):
            print(self.victim.health)
            print('th',self.victim.coordinates[0],self.victim.coordinates[1])
            if(abs(self.coordinates[0]-self.victim.coordinates[0])==1 or abs(self.coordinates[1]-self.victim.coordinates[1])==1):
                self.velocity = 1
            else:
                self.velocity = 2
            if(self.coordinates[0]<self.victim.coordinates[0]):
                #if(idArray[self.coordinates[0]+1][self.coordinates[1]]==0 or idArray[self.coordinates[0]+1][self.coordinates[1]]==9):
                self.coordinates[0]+=self.velocity
                """ elif(idArray[self.coordinates[0]+1][self.coordinates[1]]==7):
                    #print(1000)    
                    length = len(wallsList)
                    for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]+1 and Wall.coordinates[1]==self.coordinates[1] and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    idArray[Wall.coordinates[0]][Wall.coordinates[1]] = 0 """
            elif(self.coordinates[0]>self.victim.coordinates[0]):
                #if(idArray[self.coordinates[0]-1][self.coordinates[1]]==0 or idArray[self.coordinates[0]-1][self.coordinates[1]]==9):
                self.coordinates[0]-=self.velocity
                """ elif(idArray[self.coordinates[0]-1][self.coordinates[1]]==7):
                    #print(1000)
                    length = len(wallsList)
                    for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]-1 and Wall.coordinates[1]==self.coordinates[1] and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    idArray[Wall.coordinates[0]][Wall.coordinates[1]] = 0 """
            elif(self.coordinates[1]<self.victim.coordinates[1]):
                #if(idArray[self.coordinates[0]][self.coordinates[1]+1]==0 or idArray[self.coordinates[0]][self.coordinates[1]+1]==9):
                self.coordinates[1]+=self.velocity
                """ elif(idArray[self.coordinates[0]][self.coordinates[1]+1]==7):
                    print(1000)
                    length = len(wallsList)
                    for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1]==self.coordinates[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    #idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                                    idArray[Wall.coordinates[0]][Wall.coordinates[1]] = 0

                            

                 """    #pass
            elif(self.coordinates[1]>self.victim.coordinates[1]):
                #if(idArray[self.coordinates[0]][self.coordinates[1]-1]==0 or idArray[self.coordinates[0]][self.coordinates[1]-1]==9):
                self.coordinates[1]-=self.velocity
                """ elif(idArray[self.coordinates[0]][self.coordinates[1]-1]==7):
                    #print(1000)
                    length = len(wallsList)
                    for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1]==self.coordinates[1]-1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    idArray[Wall.coordinates[0]][Wall.coordinates[1]] = 0 """
            if(abs(self.coordinates[0]-self.victim.coordinates[0])<=3 and abs(self.coordinates[1]-self.victim.coordinates[1])<=3):
                self.victim.health-=4
                print('health',self.victim.health)
                if(self.victim.health<=0):
                    print(2)
                    self.occupied = False
                    self.victim.death = True
                    self.victim = None
                    
                    self.available = False 
            
            elif(self.victim.coordinates[0]==20 and self.victim.coordinates[1]==40 and abs(self.coordinates[0]-self.victim.coordinates[0])<=3 and abs(self.coordinates[1]-self.victim.coordinates[1])<=2):
                print('touch')
                self.victim.health-=4
                if(self.victim.health<=0):
                    print(3)
                    self.occupied = False
                    self.victim.death = True
                    self.victim = None
                    
                    self.available = False
            
        return idArray