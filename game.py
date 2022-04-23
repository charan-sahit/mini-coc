from array import array
from distutils.spawn import spawn
from operator import imod
from pickle import TRUE
import time
import colorama
from colorama import Fore, Back, Style
import time
from townhall import Townhall
colorama.init(autoreset=TRUE)
import numpy as np
from gameclass import Game
from kingclass import King
from input import input_to, Get
from os import system
from building import Townhall
from building import Canon
from building import Hut
from building import Wall
from barbarians import Barbarians
from building import Building
import os
from archers import Archers
from archerQueen import ArcherQueen
from wizardTower   import WizardTower
from input import input_to, Get
from balloon import Balloons
""" arrays = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        arrays[i][j] = Back.BLUE+Fore.RED+"  "+Style.RESET_ALL

print("\n".join(["".join(row) for row in arrays])) """
fileNum=1
if not os.path.exists('./replay'):
    os.makedirs('./replay')
    
file="./replay/game"
Check = True
while(Check):
    if(os.path.exists(file+str(fileNum)+".txt")):
        fileNum+=1
        Check = True
    else:
        Check = False
num=str(fileNum)
file=file+num+".txt"
rageTime = -1
healTime = time.time()
rows = 40
columns = 80
COC=Game(rows,columns)
king = King()
archerQueen = ArcherQueen()
#COC.render()
townhall = Townhall()
victory = ['v','i','c','t','o','r','y','!']
defeat = ['d','e','f','e','a','t',':','(']

hutsCoordinates = [[8,2],[13,60],[35,73],[7,15],[37,72]]
hutsList = []

for i in range(5):
    hut = Hut(hutsCoordinates[i][0],hutsCoordinates[i][1])
    
    COC.colorArray = hut.render(COC.colorArray)
    hutsList.append(hut)

canonPositions = [[20,60],[35,20],[35,40],[20,49]]
canonsList = []
for i in range(len(canonPositions)):
    canon = Canon(canonPositions[i][0],canonPositions[i][1])
    COC.colorArray = canon.render(COC.colorArray)
    canonsList.append(canon)
wallsList = []
for i in (18,23):
    for j in range(6):
        wall = Wall(i,int(columns/2)-2+j)
        ##COC.colorArray = wall.render(COC.colorArray)
        wallsList.append(wall)

for i in range(3):
    for j in (38,43):
        wall = Wall(int(rows/2)-1+i,j)
        ##COC.colorArray = wall.render(COC.colorArray)
        wallsList.append(wall)

towerList = []
towerPositions = [[20,70],[37,75],[20,75],[14,40]]
for i in range(len(towerPositions)):
    tower = WizardTower(towerPositions[i][0],towerPositions[i][1])
    COC.colorArray = tower.render(COC.colorArray)
    COC.idArray = tower.idUpdate(COC.idArray)
    towerList.append(tower)


barbariansList = []
Hut.hutsList = hutsList
Canon.canonsList = canonsList
Wall.wallsList = wallsList
Barbarians.barbariansList = barbariansList
WizardTower.towersList = towerList
""" getch = Get()
for i in range(100):
    print(input_to(getch)) """
def renderHuts():
    for i in range(Hut.limit[COC.level]):
        COC.colorArray=Hut.hutsList[i].render(COC.colorArray)
        COC.idArray = Hut.hutsList[i].idUpdate(COC.idArray)

def renderTowers():
    for i in range((WizardTower.limit[COC.level])):
        COC.colorArray=WizardTower.towersList[i].render(COC.colorArray)
        COC.idArray = WizardTower.towersList[i].idUpdate(COC.idArray)


def renderCanons():
    for i in range(Canon.limit[COC.level]):
        COC.colorArray=canonsList[i].render(COC.colorArray)
        COC.idArray = canonsList[i].idUpdate(COC.idArray)

def renderWalls():
    for i in range(len(Wall.wallsList)):
        COC.colorArray=Wall.wallsList[i].render(COC.colorArray)
        COC.idArray = Wall.wallsList[i].idUpdate(COC.idArray)

def renderBarbarians():
    for i in range(len(Barbarians.barbariansList)):
        COC.colorArray=Barbarians.barbariansList[i].render(COC.colorArray)
        COC.idArray = Barbarians.barbariansList[i].idUpdate(COC.idArray)

def renderArchers():
    for i in range(len(Archers.archersList)):
        if(Archers.archersList[i].death==False):
            COC.colorArray=Archers.archersList[i].render(COC.colorArray)
            COC.idArray = Archers.archersList[i].idUpdate(COC.idArray)

def renderBalloons():
    for i in range(len(Balloons.balloonsList)):
        COC.colorArray=Balloons.balloonsList[i].render(COC.colorArray)
        COC.idArray = Balloons.balloonsList[i].idUpdate(COC.idArray)

def canonShoot():
    for i in range(len(canonsList)):
        canonsList[i].shoot(king,Barbarians,Archers)

def qcanonShoot():
    for i in range(len(canonsList)):
        canonsList[i].shoot(archerQueen,Barbarians,Archers)

def towerShoot():
    for i in range(len(towerList)):
        if(towerList[i].death==False):
            towerList[i].shoot(king,Barbarians,Archers,Balloons)

def qtowerShoot():
    for i in range(len(towerList)):
        if(towerList[i].death==False):
            towerList[i].shoot(archerQueen,Barbarians,Archers,Balloons)
def spawn(key):
    if(key == 'z'):
        if(len(Barbarians.barbariansList)<Barbarians.limit[COC.level]):
            barbarian = Barbarians(38,22)
            COC.colorArray = barbarian.render(COC.colorArray)
            COC.idArray = barbarian.idUpdate(COC.idArray)
            Barbarians.barbariansList.append(barbarian)
    if(key == 'c'):
        if(len(Barbarians.barbariansList)<Barbarians.limit[COC.level]):
            barbarian = Barbarians(17,65)
            COC.colorArray = barbarian.render(COC.colorArray)
            COC.idArray = barbarian.idUpdate(COC.idArray)
            Barbarians.barbariansList.append(barbarian)
    if(key == 'v'):
        if(len(Barbarians.barbariansList)<Barbarians.limit[COC.level]):
            barbarian = Barbarians(35,65)
            COC.colorArray = barbarian.render(COC.colorArray)
            COC.idArray = barbarian.idUpdate(COC.idArray)
            Barbarians.barbariansList.append(barbarian)
    if(key == 'b'):
        if(len(Archers.archersList)<Archers.limit[COC.level]):
            archer = Archers(25,65)
            COC.colorArray = archer.render(COC.colorArray)
            COC.idArray = archer.idUpdate(COC.idArray)
            Archers.archersList.append(archer)
    if(key == 'n'):
        if(len(Archers.archersList)<Archers.limit[COC.level]):
            archer = Archers(35,25)
            COC.colorArray = archer.render(COC.colorArray)
            COC.idArray = archer.idUpdate(COC.idArray)
            Archers.archersList.append(archer)
    if(key == 'm'):
        if(len(Archers.archersList)<Archers.limit[COC.level]):
            archer = Archers(15,49)
            COC.colorArray = archer.render(COC.colorArray)
            COC.idArray = archer.idUpdate(COC.idArray)
            Archers.archersList.append(archer)
    if(key == 'j'):
        if(len(Balloons.balloonsList)<Balloons.limit[COC.level]):
            balloon = Balloons(25,40)
            COC.colorArray = balloon.render(COC.colorArray)
            COC.idArray = balloon.idUpdate(COC.idArray)
            Balloons.balloonsList.append(balloon)
    if(key == 'k'):
        if(len(Balloons.balloonsList)<Balloons.limit[COC.level]):
            balloon = Balloons(35,40)
            COC.colorArray = balloon.render(COC.colorArray)
            COC.idArray = balloon.idUpdate(COC.idArray)
            Balloons.balloonsList.append(balloon)
    if(key == 'l'):
        if(len(Balloons.balloonsList)<Balloons.limit[COC.level]):
            balloon = Balloons(12,40)
            COC.colorArray = balloon.render(COC.colorArray)
            COC.idArray = balloon.idUpdate(COC.idArray)
            Balloons.balloonsList.append(balloon)

def rageStart():
    COC.color = Back.LIGHTMAGENTA_EX + "  " + Style.RESET_ALL
    king.velocity = 2
    Barbarians.velocity = 2
    townhall.health = 10 - 2*(10 - townhall.health)
    for hut in Hut.hutsList:
        hut.health = 10 - 2*(10 - hut.health)
    for canon in Canon.canonsList:
        canon.health = 10 - 2*(10 - canon.health)

def rageEnd():
    COC.color = Back.LIGHTGREEN_EX + "  " + Style.RESET_ALL
    king.velocity = 1
    Barbarians.velocity = 1

def healStart():
    COC.color = Back.LIGHTYELLOW_EX + "  " + Style.RESET_ALL
    
    townhall.health = (3/2)*townhall.health
    for hut in Hut.hutsList:
        hut.health = (3/2)*hut.health
        if(hut.health>10):
            hut.health = 10
    for canon in Canon.canonsList:
        canon.health = (3/2)*canon.health
        if(canon.health>10):
            canon.health = 10

def healEnd():
    COC.color = Back.LIGHTGREEN_EX + "  " + Style.RESET_ALL
    
def checkVictory():
    check = False
    if(townhall.death == True):
        check = True
    else:
        return False
    for hut in Hut.hutsList:
        if(hut.death == True):
            check = True
        else:
            return False
    for canon in Canon.canonsList:
        if(canon.death == True):
            check = True
        else:
            return False
    return check

def checkDefeat():
    check = False
    for barbarian in Barbarians.barbariansList:
        if(barbarian.death == True):
            check = True
        else:
            return False
    for archer in Archers.archersList:
        if(archer.death == True):
            check = True
        else:
            return False
    for balloon in Balloons.balloonsList:
        if(balloon.death == True):
            check = True
        else:
            return False
    if(king.death == True):
        check = True
    else:
        return False
    return check

def qcheckDefeat():
    check = False
    for barbarian in Barbarians.barbariansList:
        if(barbarian.death == True):
            check = True
        else:
            return False
    for archer in Archers.archersList:
        if(archer.death == True):
            check = True
        else:
            return False
    for balloon in Balloons.balloonsList:
        if(balloon.death == True):
            check = True
        else:
            return False
    if(archerQueen.death == True):
        check = True
    else:
        return False
    return check

def narikey():
    for building in Building.buildingList:
        if(abs(building.coordinates[0]-king.coordinates[0])< 5 and abs(building.coordinates[1]-king.coordinates[1]) < 5):
            building.health = building.health - 5
 
def moveBarbarians(hutsList):
    for barbarian in Barbarians.barbariansList:
        barbarian.choose(Building)
        barbarian.move(COC.idArray, hutsList)

def moveArchers(wallsList):
    for archer in Archers.archersList:
        archer.choose(Building)
        archer.move(COC.idArray, wallsList)
def moveBalloons():
    for balloon in Balloons.balloonsList:
        balloon.choose(Building,WizardTower)
        balloon.move(COC.idArray, wallsList)
def levelInit():
    king.health = 100
    king.death = False
    
    for building in Building.buildingList:
        building.health = 10
        building.death = False
    for tower in WizardTower.towersList:
        tower.health = 10
        tower.death = False
    Barbarians.barbariansList = []
    Archers.archersList = []
    Balloons.balloonsList = []

    king.coordinates = [25,55]


    


print("If you want to play with king press K else press Q")

choice = input()
if(choice == 'K' or choice == 'k'):

    while(1):
        

        COC.board(rows,columns)
        COC.idArray = townhall.idUpdate(COC.idArray)
        COC.colorArray =  townhall.render(COC.colorArray, COC.idArray)
        
        renderHuts()
        renderCanons()
        renderTowers()
        renderWalls()
        canonShoot()
        towerShoot()
        moveBarbarians(wallsList)
        moveArchers(wallsList)
        moveBalloons()
        
        renderBarbarians()
        renderArchers()
        renderBalloons()

        key = king.input()
        king.move(COC.idArray)
        
        spawn(key)
        if(key == 'r'):
            rageTime = time.time()
            rageStart()
        if(time.time()-rageTime>=5):
            rageEnd()
            rageTime = time.time()

        if(key == 'h'):
            healTime = time.time()
            healStart()
        if(time.time()-healTime>=5):
            healEnd()
        if(key == 'x'):
            narikey()
        if(key == ' '):
            king.attack(COC,townhall,Hut,Canon,Wall)


        COC.colorArray = king.update(COC.colorArray)
        COC.idArray = king.idUpdate(COC.idArray)
        king.healthDisplay(COC.colorArray)
        if(checkVictory()==True):
            COC.colorArray= [[Back.LIGHTGREEN_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
            for i in range(8):
                COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.GREEN + victory[i] + Style.RESET_ALL
            
            
            levelInit()
            COC.level+=1
            if(COC.level ==3):
                system('clear')
                COC.render()
                file_name=open(file,"a")
                file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
                file_name.write("\n")
                file_name.close()
                break

        if(checkDefeat()==True):
            COC.colorArray= [[Back.LIGHTRED_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
            for i in range(8):
                COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.LIGHTRED_EX + defeat[i] + Style.RESET_ALL
            system('clear')
            COC.render()
            file_name=open(file,"a")
            file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
            file_name.write("\n")
            file_name.close()
            break
        system('clear')
        COC.render()
        file_name=open(file,"a")
        file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
        file_name.write("\n")
        file_name.close()
    
elif(choice == 'Q' or choice == 'q'):
    while(1):
        
        
        COC.board(rows,columns)
        COC.idArray = townhall.idUpdate(COC.idArray)
        COC.colorArray =  townhall.render(COC.colorArray, COC.idArray)
        
        renderHuts()
        renderCanons()
        renderTowers()
        renderWalls()
        qcanonShoot()
        qtowerShoot()
        moveBarbarians(wallsList)
        moveArchers(wallsList)
        moveBalloons()
        renderBarbarians()
        renderArchers()
        renderBalloons()
        if(archerQueen.death==False):
            key = archerQueen.input()
            archerQueen.move(COC.idArray)
        
        spawn(key)
        if(key == 'r'):
            rageTime = time.time()
            rageStart()
        if(time.time()-rageTime>=5):
            rageEnd()
            rageTime = time.time()

        if(key == 'h'):
            healTime = time.time()
            healStart()
        if(time.time()-healTime>=5):
            healEnd()
        if(key == 'x'):
            narikey()
        if(key == ' '):
            #archerQueen.attackk(COC,townhall,Hut,Canon,Wall)
            archerQueen.chooseAttack(Building)

        COC.colorArray = archerQueen.update(COC.colorArray)
        COC.idArray = archerQueen.idUpdate(COC.idArray)
        archerQueen.healthDisplay(COC.colorArray)
        if(checkVictory()==True):
            COC.colorArray= [[Back.LIGHTGREEN_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
            for i in range(8):
                COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.GREEN + victory[i] + Style.RESET_ALL
            levelInit()
            COC.level+=1
            if(COC.level ==3):
                system('clear')
                COC.render()
                file_name=open(file,"a")
                file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
                file_name.write("\n")
                file_name.close()
                break
            
        if(qcheckDefeat()==True):
            COC.colorArray= [[Back.LIGHTRED_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
            for i in range(8):
                COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.LIGHTRED_EX + defeat[i] + Style.RESET_ALL
        
        system('clear')
        COC.render()
        file_name=open(file,"a")
        file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
        file_name.write("\n")
        file_name.close()
    
        
        


    