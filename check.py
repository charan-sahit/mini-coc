def move(self,idArray,wallsList):
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
                self.victim.health-=2
                if(self.victim.health<=0):
                    print(2)
                    self.occupied = False
                    self.victim = None 
            
            elif(self.victim.coordinates[0]==20 and self.victim.coordinates[1]==40 and abs(self.coordinates[0]-self.victim.coordinates[0])<=3 and abs(self.coordinates[1]-self.victim.coordinates[1])<=2):
                print('touch')
                self.victim.health-=1
                if(self.victim.health<=0):
                    print(3)
                    self.occupied = False
                    self.victim = None
                    self.death = True
            
        return idArray