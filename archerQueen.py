from colorama import Back, Fore, Style

from input import input_to, Get

class ArcherQueen:
    def __init__(self):
        getch = Get()
        self.coordinates = [25,55]
        self.rows = 2
        self.columns = 2
        self.color = Back.CYAN + " " + Style.RESET_ALL 
        self.key = 'h'
        self.prev = 'p'
        self.health = 100
        self.death = False
        self.velocity = 1
        self.site = [10,0]
        self.copy = [0,0]
        self.coords = [0,0]

    def input(self):
        getch = Get()
        print(self.coordinates[0],self.coordinates[1])
        print("site",self.site[0],self.site[1])
        if(self.key != ' '):
            self.prev = self.key
        self.key = input_to(getch)
        
        return self.key
    
    def move(self,idArray):

        if(self.key =='w'):
            ##print(idArray[self.coordinates[0]-1][self.coordinates[1]-2],idArray[self.coordinates[0]][self.coordinates[1]-2])
            print(idArray[self.coordinates[0]-2][self.coordinates[1]-1], idArray[self.coordinates[0]-2][self.coordinates[1]])
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                if(idArray[self.coordinates[0]-2][self.coordinates[1]-1]==0 and idArray[self.coordinates[0]-2][self.coordinates[1]]==0):
                
                    self.coordinates[0]-= self.velocity
        elif(self.key=='s'):
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                if(idArray[self.coordinates[0]+1][self.coordinates[1]-1]==0 and idArray[self.coordinates[0]+1][self.coordinates[1]]==0):
                
                    self.coordinates[0]+=self.velocity
        elif(self.key=='a'):
            ##print(idArray[self.coordinates[0]-2][self.coordinates[1]-1])
            if(self.coordinates[1]>1 and self.coordinates[1]<79):
                if(idArray[self.coordinates[0]-1][self.coordinates[1]-2]==0 and idArray[self.coordinates[0]][self.coordinates[1]-2]==0):
                
                    
                    self.coordinates[1]-=self.velocity
            
        elif(self.key=='d'):
            if(self.coordinates[1]>1 and self.coordinates[1]<79):
                if(idArray[self.coordinates[0]-1][self.coordinates[1]+1]==0 and idArray[self.coordinates[0]][self.coordinates[1]+1]==0):
                
                    self.coordinates[1]+=self.velocity
        elif(self.key == ' '):
            if(self.coordinates[1]>1 and self.coordinates[1]<79 and self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                pass

    def attack(self,COC,Townhall,hut,canon,wall):
        hutsList = hut.hutsList
        canonsList = canon.canonsList
        wallsList = wall.wallsList
        print(len(wallsList))
        ##print(wall.wallsList)
        if(self.coordinates[1]>1 and self.coordinates[1]<79 and self.coordinates[0]> 1 and  self.coordinates[0] < 39):
            if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]!=0 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]!=0):
                
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==7 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==7):
                   length = len(wallsList)
                   for i in range(length):
                        Wall = wallsList[i]
                        
                        
                        if(Wall.coordinates[0]==self.coordinates[0]-2 and Wall.coordinates[1]==self.coordinates[1]-1 and Wall.health!=0):
                            
                            Wall.health -= 1 
                            if(Wall.health==0):
                                
                                COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                        if(Wall.coordinates[0]==self.coordinates[0]-2 and Wall.coordinates[1] == self.coordinates[1] and Wall.health!=0):
                            
                            Wall.health -= 1 
                            if(Wall.health==0):
                                    
                                COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                        
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==2 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==2):
                    length = len(hutsList)
                    for i in range(length):
                        Hut = hutsList[i]
                        if(Hut.coordinates[0]==self.coordinates[0]-2 and Hut.coordinates[1]==self.coordinates[1]-1 and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.coordinates[0]==self.coordinates[0]-2 and Hut.coordinates[1] == self.coordinates[1] and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.health == 0):
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==3 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==3):
                    length = len(canonsList)
                    for i in range(length):
                        Canon = canonsList[i]
                        if(Canon.coordinates[0]==self.coordinates[0]-2 and Canon.coordinates[1]==self.coordinates[1]-1 and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.coordinates[0]==self.coordinates[0]-2 and Canon.coordinates[1] == self.coordinates[1] and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.health == 0):
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==4 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==4):
                    
                    
                    Townhall.health -= 1 
                    if(Townhall.health == 0):
                        COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                        COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0 
            
            if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]!=0 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]!=0):
                    print(1)
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==7 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]+1 and Wall.coordinates[1]==self.coordinates[1]-1 and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                            if(Wall.coordinates[0]==self.coordinates[0]+1 and Wall.coordinates[1] == self.coordinates[1] and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==2 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==2):
                        length = len(hutsList)
                        print(1)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]+1 and Hut.coordinates[1]==self.coordinates[1]-1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0]+1 and Hut.coordinates[1] == self.coordinates[1] and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==3 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]+1 and Canon.coordinates[1]==self.coordinates[1]-1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0]+1 and Canon.coordinates[1] == self.coordinates[1] and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==4 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
              
            if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]!=0 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]!=0):
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==7 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]-1 and Wall.coordinates[1]==self.coordinates[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1] == self.coordinates[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==2 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]-1 and Hut.coordinates[1]==self.coordinates[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0] and Hut.coordinates[1] == self.coordinates[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==3 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]-1 and Canon.coordinates[1]==self.coordinates[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0] and Canon.coordinates[1] == self.coordinates[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==4 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                            COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
            if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]!=0 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]!=0):
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==7 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]-1 and Wall.coordinates[1]==self.coordinates[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1] == self.coordinates[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==2 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]-1 and Hut.coordinates[1]==self.coordinates[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0] and Hut.coordinates[1] == self.coordinates[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==3 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]-1 and Canon.coordinates[1]==self.coordinates[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0] and Canon.coordinates[1] == self.coordinates[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==4 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                            COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0


    def attacck(self,COC,Townhall,hut,canon,wall):
        hutsList = hut.hutsList
        canonsList = canon.canonsList
        wallsList = wall.wallsList
        print(len(wallsList))
        ##print(wall.wallsList)
        if(self.coords[1]>1 and self.coords[1]<79 and self.coords[0]> 1 and  self.coords[0] < 39):
            if(COC.idArray[self.coords[0]-2][self.coords[1]-1]!=0 or COC.idArray[self.coords[0]-2][self.coords[1]]!=0):
                
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==7 or COC.idArray[self.coords[0]-2][self.coords[1]]==7):
                   length = len(wallsList)
                   for i in range(length):
                        Wall = wallsList[i]
                        
                        
                        if(Wall.coords[0]==self.coords[0]-2 and Wall.coords[1]==self.coords[1]-1 and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                
                                COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                        if(Wall.coords[0]==self.coords[0]-2 and Wall.coords[1] == self.coords[1] and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                    
                                COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                        
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==2 or COC.idArray[self.coords[0]-2][self.coords[1]]==2):
                    length = len(hutsList)
                    for i in range(length):
                        Hut = hutsList[i]
                        if(Hut.coords[0]==self.coords[0]-2 and Hut.coords[1]==self.coords[1]-1 and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.coords[0]==self.coords[0]-2 and Hut.coords[1] == self.coords[1] and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.health == 0):
                            COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==3 or COC.idArray[self.coords[0]-2][self.coords[1]]==3):
                    length = len(canonsList)
                    for i in range(length):
                        Canon = canonsList[i]
                        if(Canon.coords[0]==self.coords[0]-2 and Canon.coords[1]==self.coords[1]-1 and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.coords[0]==self.coords[0]-2 and Canon.coords[1] == self.coords[1] and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.health == 0):
                            COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==4 or COC.idArray[self.coords[0]-2][self.coords[1]]==4):
                    
                    
                    Townhall.health -= 1 
                    if(Townhall.health == 0):
                        COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                        COC.idArray[self.coords[0]-2][self.coords[1]] = 0 
            
            if(COC.idArray[self.coords[0]+1][self.coords[1]-1]!=0 or COC.idArray[self.coords[0]+1][self.coords[1]]!=0):
                    print(1)
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==7 or COC.idArray[self.coords[0]+1][self.coords[1]]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coords[0]==self.coords[0]+1 and Wall.coords[1]==self.coords[1]-1 and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                            if(Wall.coords[0]==self.coords[0]+1 and Wall.coords[1] == self.coords[1] and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==2 or COC.idArray[self.coords[0]+1][self.coords[1]]==2):
                        length = len(hutsList)
                        print(1)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coords[0]==self.coords[0]+1 and Hut.coords[1]==self.coords[1]-1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coords[0]==self.coords[0]+1 and Hut.coords[1] == self.coords[1] and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                                COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==3 or COC.idArray[self.coords[0]+1][self.coords[1]]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coords[0]==self.coords[0]+1 and Canon.coords[1]==self.coords[1]-1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coords[0]==self.coords[0]+1 and Canon.coords[1] == self.coords[1] and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                                COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==4 or COC.idArray[self.coords[0]+1][self.coords[1]]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]+1][self.coords[1]] = 0
              
            if(COC.idArray[self.coords[0]-1][self.coords[1]-2]!=0 or COC.idArray[self.coords[0]][self.coords[1]-2]!=0):
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==7 or COC.idArray[self.coords[0]][self.coords[1]-2]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coords[0]==self.coords[0]-1 and Wall.coords[1]==self.coords[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                            if(Wall.coords[0]==self.coords[0] and Wall.coords[1] == self.coords[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==2 or COC.idArray[self.coords[0]][self.coords[1]-2]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coords[0]==self.coords[0]-1 and Hut.coords[1]==self.coords[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coords[0]==self.coords[0] and Hut.coords[1] == self.coords[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                                COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==3 or COC.idArray[self.coords[0]][self.coords[1]-2]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coords[0]==self.coords[0]-1 and Canon.coords[1]==self.coords[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coords[0]==self.coords[0] and Canon.coords[1] == self.coords[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                                COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==4 or COC.idArray[self.coords[0]][self.coords[1]-2]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                            COC.idArray[self.coords[0]][self.coords[1]-2] = 0
            if(COC.idArray[self.coords[0]-1][self.coords[1]+1]!=0 or COC.idArray[self.coords[0]][self.coords[1]+1]!=0):
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==7 or COC.idArray[self.coords[0]][self.coords[1]+1]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coords[0]==self.coords[0]-1 and Wall.coords[1]==self.coords[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                            if(Wall.coords[0]==self.coords[0] and Wall.coords[1] == self.coords[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==2 or COC.idArray[self.coords[0]][self.coords[1]+1]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coords[0]==self.coords[0]-1 and Hut.coords[1]==self.coords[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coords[0]==self.coords[0] and Hut.coords[1] == self.coords[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                                COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==3 or COC.idArray[self.coords[0]][self.coords[1]+1]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coords[0]==self.coords[0]-1 and Canon.coords[1]==self.coords[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coords[0]==self.coords[0] and Canon.coords[1] == self.coords[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                                COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==4 or COC.idArray[self.coords[0]][self.coords[1]+1]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                            COC.idArray[self.coords[0]][self.coords[1]+1] = 0

    def attaacck(self,COC,Townhall,hut,canon,wall):
        hutsList = hut.hutsList
        canonsList = canon.canonsList
        wallsList = wall.wallsList
        
        ##print(wall.wallsList)
        if(self.coords[1]>1 and self.coords[1]<79 and self.coords[0]> 1 and  self.coords[0] < 39):
            if(COC.idArray[self.coords[0]-2][self.coords[1]-1]!=0 or COC.idArray[self.coords[0]-2][self.coords[1]]!=0):
                
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==7 or COC.idArray[self.coords[0]-2][self.coords[1]]==7):
                   length = len(wallsList)
                   for i in range(length):
                        Wall = wallsList[i]
                        
                        
                        if(Wall.coordinates[0]==self.coords[0]-2 and Wall.coordinates[1]==self.coords[1]-1 and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                
                                COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                        if(Wall.coordinates[0]==self.coords[0]-2 and Wall.coordinates[1] == self.coords[1] and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                    
                                COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                        
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==2 or COC.idArray[self.coords[0]-2][self.coords[1]]==2):
                    length = len(hutsList)
                    for i in range(length):
                        Hut = hutsList[i]
                        if(Hut.coordinates[0]==self.coords[0]-2 and Hut.coordinates[1]==self.coords[1]-1 and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.coordinates[0]==self.coords[0]-2 and Hut.coordinates[1] == self.coords[1] and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.health == 0):
                            COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==3 or COC.idArray[self.coords[0]-2][self.coords[1]]==3):
                    length = len(canonsList)
                    for i in range(length):
                        Canon = canonsList[i]
                        if(Canon.coordinates[0]==self.coords[0]-2 and Canon.coordinates[1]==self.coords[1]-1 and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.coordinates[0]==self.coords[0]-2 and Canon.coordinates[1] == self.coords[1] and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.health == 0):
                            COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]-2][self.coords[1]] = 0
                if(COC.idArray[self.coords[0]-2][self.coords[1]-1]==4 or COC.idArray[self.coords[0]-2][self.coords[1]]==4):
                    
                    
                    Townhall.health -= 1 
                    if(Townhall.health == 0):
                        COC.idArray[self.coords[0]-2][self.coords[1]-1] = 0
                        COC.idArray[self.coords[0]-2][self.coords[1]] = 0 
            
            if(COC.idArray[self.coords[0]+1][self.coords[1]-1]!=0 or COC.idArray[self.coords[0]+1][self.coords[1]]!=0):
                    print(1)
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==7 or COC.idArray[self.coords[0]+1][self.coords[1]]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coords[0]+1 and Wall.coordinates[1]==self.coords[1]-1 and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                            if(Wall.coordinates[0]==self.coords[0]+1 and Wall.coordinates[1] == self.coords[1] and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==2 or COC.idArray[self.coords[0]+1][self.coords[1]]==2):
                        length = len(hutsList)
                        print(1)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coords[0]+1 and Hut.coordinates[1]==self.coords[1]-1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coords[0]+1 and Hut.coordinates[1] == self.coords[1] and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                                COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==3 or COC.idArray[self.coords[0]+1][self.coords[1]]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coords[0]+1 and Canon.coordinates[1]==self.coords[1]-1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coords[0]+1 and Canon.coordinates[1] == self.coords[1] and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                                COC.idArray[self.coords[0]+1][self.coords[1]] = 0
                    if(COC.idArray[self.coords[0]+1][self.coords[1]-1]==4 or COC.idArray[self.coords[0]+1][self.coords[1]]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]+1][self.coords[1]-1] = 0
                            COC.idArray[self.coords[0]+1][self.coords[1]] = 0
              
            if(COC.idArray[self.coords[0]-1][self.coords[1]-2]!=0 or COC.idArray[self.coords[0]][self.coords[1]-2]!=0):
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==7 or COC.idArray[self.coords[0]][self.coords[1]-2]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coords[0]-1 and Wall.coordinates[1]==self.coords[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                            if(Wall.coordinates[0]==self.coords[0] and Wall.coordinates[1] == self.coords[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==2 or COC.idArray[self.coords[0]][self.coords[1]-2]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coords[0]-1 and Hut.coordinates[1]==self.coords[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coords[0] and Hut.coordinates[1] == self.coords[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                                COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==3 or COC.idArray[self.coords[0]][self.coords[1]-2]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coords[0]-1 and Canon.coordinates[1]==self.coords[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coords[0] and Canon.coordinates[1] == self.coords[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                                COC.idArray[self.coords[0]][self.coords[1]-2] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]-2]==4 or COC.idArray[self.coords[0]][self.coords[1]-2]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]-1][self.coords[1]-2] = 0
                            COC.idArray[self.coords[0]][self.coords[1]-2] = 0
            if(COC.idArray[self.coords[0]-1][self.coords[1]+1]!=0 or COC.idArray[self.coords[0]][self.coords[1]+1]!=0):
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==7 or COC.idArray[self.coords[0]][self.coords[1]+1]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coords[0]-1 and Wall.coordinates[1]==self.coords[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                            if(Wall.coordinates[0]==self.coords[0] and Wall.coordinates[1] == self.coords[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==2 or COC.idArray[self.coords[0]][self.coords[1]+1]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coords[0]-1 and Hut.coordinates[1]==self.coords[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coords[0] and Hut.coordinates[1] == self.coords[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                                COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==3 or COC.idArray[self.coords[0]][self.coords[1]+1]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coords[0]-1 and Canon.coordinates[1]==self.coords[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coords[0] and Canon.coordinates[1] == self.coords[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                                COC.idArray[self.coords[0]][self.coords[1]+1] = 0
                    if(COC.idArray[self.coords[0]-1][self.coords[1]+1]==4 or COC.idArray[self.coords[0]][self.coords[1]+1]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coords[0]-1][self.coords[1]+1] = 0
                            COC.idArray[self.coords[0]][self.coords[1]+1] = 0


    def attackk(self,COC,Townhall,hut,canon,wall):
        self.copy = self.coordinates
        
        if(self.key=='w'):
            if(self.coordinates[0]> 9 and  self.coordinates[0] < 38):
                self.site = [self.coordinates[0]-8,self.coordinates[1]]
        elif(self.key=='s'):
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 30):
                self.site = [self.coordinates[0]+8,self.coordinates[1]]
        elif(self.key=='a'):
            if(self.coordinates[1]>9 and self.coordinates[1]<78):
                self.site = [self.coordinates[0],self.coordinates[1]-8]
        elif(self.key=='d'):
            if(self.coordinates[1]>1 and self.coordinates[1]<70):
                self.site = [self.coordinates[0],self.coordinates[1]+8]
        
        for i in range(8):
            for j in range(8):
                print("coo",self.copy[0],self.coordinates[0])
                self.coords[0] = self.site[0]-i+4
                self.coords[1] = self.site[1]-j+4
                self.attaacck(COC,Townhall,hut,canon,wall)
        self.coords[0] = self.copy[0]
        self.coords[1] = self.copy[1]
        
    def chooseAttack(self,Building):
        print(1000000000000000000000000)
        if(self.prev=='w'):
            if(self.coordinates[0]> 9 and  self.coordinates[0] < 38):
                self.site = [self.coordinates[0]-8,self.coordinates[1]]
        elif(self.prev=='s'):
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 30):
                self.site = [self.coordinates[0]+8,self.coordinates[1]]
        elif(self.prev=='a'):
            if(self.coordinates[1]>9 and self.coordinates[1]<78):
                self.site = [self.coordinates[0],self.coordinates[1]-8]
        elif(self.prev=='d'):
            if(self.coordinates[1]>1 and self.coordinates[1]<70):
                self.site = [self.coordinates[0],self.coordinates[1]+8]
        else:
            self.site = self.coordinates
        check = False
        #print("Target",self.target)
        #if(self.target != None):
            #print('Distance',abs(self.coordinates[0]-self.target.coordinates[0]),abs(self.coordinates[1]-self.target.coordinates[1]))
        #    pass
        #if(self.occupied == False):
        #if(self.target == None):
            #print('barbPeek')
        min_distance = 1000
        for building in Building.buildingList:
            
            if(abs(building.coordinates[0]-self.site[0])<5 and abs(building.coordinates[1]-self.site[1])<5):
                

                
                if(building.death==False):
                    building.health-=2
                    if(building.health<=0):
                        building.death=True
                    #self.target = building
                    #check = True
                    #min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
                
            """ if(check == True):
                self.occupied = True
        if(self.target != None): 
               
            if(self.target.health<=0):
                
                print(1789)
                self.target = None
                self.occupied = False """
        

    def healthDisplay(self,colorArray):
        health = ['H','e','a','l','t','h','=',]
        fraction = self.health/100
        for i in range(len(health)):
            colorArray[1][60 - 7 + i] = Back.LIGHTGREEN_EX + health[i] + Style.RESET_ALL
        toColor = int(fraction*10)
        for i in range(toColor):
            colorArray[1][60 + i] = Back.GREEN + ' ' + Style.RESET_ALL
        for i in range(10-toColor):
            colorArray[1][60 + toColor + i] = Back.RED + ' ' + Style.RESET_ALL
        return colorArray

    def update(self,colorArray):
        self.color = Back.LIGHTCYAN_EX+ str(self.health) + Style.RESET_ALL
        if(self.health>0):
            self.color = Back.LIGHTCYAN_EX + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL
            self.death = True
        for i in range(self.rows):
            for j in range(self.columns):
                colorArray[self.coordinates[0] - 1 + j][self.coordinates[1] - 1 + i] = self.color

                
        return colorArray

    def idUpdate(self,idArray):
        for i in range(self.rows):
            for j in range(self.columns):
                idArray[self.coordinates[0] - 1 + j][self.coordinates[1] - 1 + i] = 1
        return idArray

                            