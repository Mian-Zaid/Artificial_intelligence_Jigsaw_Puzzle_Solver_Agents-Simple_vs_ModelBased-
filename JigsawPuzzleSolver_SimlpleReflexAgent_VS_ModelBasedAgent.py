import random
import time

# Environmnet Class

class Environment:

    def __init__(self,n,moves):
        # print("I am Environment counstructor")
        self.moves=moves
        self.N=n
        self.list=[]
        self.InitialGrid=[]   #my starting grid
        self.StartGrid=[]     #grid solved by simple reflex agent
        self.StartGrid_2=[]   #grid solved by Model based reflex agent
        self.SolutionGrid=[]  #my solutioin grid
        ag=None

        for i in range(self.N):
            temp = []
            for j in range(self.N):
                temp.append(random.randint(1, 4))
            self.InitialGrid.append(temp)

        for i in range(self.N):
            temp=[]
            for j in range(self.N):
               temp.append(self.InitialGrid[i][j])
            self.StartGrid.append(temp)

        for i in range(self.N):
            temp=[]
            for j in range(self.N):
               temp.append(self.InitialGrid[i][j])
            self.StartGrid_2.append(temp)

        for i in range(self.N):
            temp=[]
            for j in range(self.N):
               temp.append(random.randint(1,4))
            self.SolutionGrid.append(temp)

        self.x_cordinate = random.randint(0, self.N - 1)
        self.y_cordinate = random.randint(0, self.N - 1)

    def printGrids(self):
        print("value of N : ")
        print(self.N)
        print("value of moves : ")
        print(self.moves)

        print("initial  : ",self.StartGrid)
        print("initial_2: ", self.StartGrid_2)
        print("solution : ",self.SolutionGrid)

    def getState(self,StartGrid):
        if StartGrid[self.x_cordinate][self.y_cordinate] == self.SolutionGrid[self.x_cordinate][self.y_cordinate]:
            return 1
        return 0

    def getCordinates(self):
        print("x : ",self.x_cordinate)
        print("y : ",self.y_cordinate)

    def clockWise(self,ag):
        if self.StartGrid[ag.x_cordinate][ag.y_cordinate] + 1 > 4:
            self.StartGrid[ag.x_cordinate][ag.y_cordinate] = 1
        else:
            self.StartGrid[ag.x_cordinate][ag.y_cordinate] += 1
        ag.consumedMoves += 1

    def antiClockWise(self,ag):
        if self.StartGrid[ag.x_cordinate][ag.y_cordinate] - 1 < 1:
            self.StartGrid[ag.x_cordinate][ag.y_cordinate] = 4
        else:
            self.StartGrid[ag.x_cordinate][ag.y_cordinate] -= 1
        ag.consumedMoves += 1

    def clockWise_2(self, ag):
        if self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] + 1 > 4:
            self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] = 1
        else:
            self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] += 1
        ag.consumedMoves += 1

    def antiClockWise_2(self, ag):
        if self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] - 1 < 1:
            self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] = 4
        else:
            self.StartGrid_2[ag.x_cordinate][ag.y_cordinate] -= 1
        ag.consumedMoves += 1

    def moveUp(self):
        if self.x_cordinate - 1 == -1:
            return 0
        else:
            self.x_cordinate-=1
            # print("move up")
            return 1

    def moveDown(self):
        if self.x_cordinate + 1 == self.N:
            return 0
        else:
            self.x_cordinate+=1
            # print("move down")
            return 1

    def moveRight(self):
        if self.y_cordinate + 1 == self.N:
            return 0
        else:
            self.y_cordinate+=1
            # print("move right")
            return 1

    def moveLeft(self):
        if self.y_cordinate - 1 == -1:
            return 0
        else:
            self.y_cordinate-=1
            # print("move left")
            return 1

    def gridSolved(self,StartGrid):
        solve=0
        for i in range(self.N):
            for j in range(self.N):
                if StartGrid[i][j]==self.SolutionGrid[i][j]:
                    solve+=1


        if solve==self.N*self.N:
            return 1
        else:
            return 0

    def createAgent(self):
        ag = SimpleAgent(self.moves,self.N)
        ag.percept(self.x_cordinate,self.y_cordinate,self.getState(self.StartGrid))
        # ag.currentLoc()
        # print("Moves consumed : ", ag.consumedMoves)
        # print("moves remianing : ", ag.totalMoves - ag.consumedMoves)
        while self.gridSolved(self.StartGrid)==0: # run until grid is solved or not
            if ag.consumedMoves<ag.totalMoves:  #chek for moves end or not

                # do rotation while reaming in same box
                while ag.state!=1 and ag.consumedMoves<ag.totalMoves:
                    if ag.rotation()==1:
                        self.clockWise(ag)
                    elif ag.rotation()==2:
                        self.antiClockWise(ag)
                    # print("\nafter some moves  : ", self.StartGrid)
                    ag.percept(self.x_cordinate,self.y_cordinate,self.getState(self.StartGrid))
                    if self.getState(self.StartGrid)==1:
                        ag.correctPiece += 1
                    # ag.currentLoc()
                    # print("Moves consumed : ",ag.consumedMoves)
                    # print("moves remianing : ",ag.totalMoves-ag.consumedMoves)

                # change box by moving up down left right
                if ag.state==1 and ag.consumedMoves<ag.totalMoves:
                    # time.sleep(3)
                    # print("\n\nplaced correctly now ready to move")
                    # print("\ntowrads soloution: ",self.StartGrid)
                    # print("solution         : ",self.SolutionGrid,"\n")

                    goo=1
                    while goo==1:
                        if ag.movement(self.getState(self.StartGrid))==0:
                            if self.moveUp()==0:
                                goo=1
                                # print("movew up failed")
                            else:
                                goo=0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid))
                                # ag.currentLoc()
                                # print("move up passed")
                                break
                        elif ag.movement(self.getState(self.StartGrid))==1:
                            if self.moveDown()==0:
                                goo=1
                                # print("movew down failed")
                            else:
                                goo=0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid))
                                # ag.currentLoc()
                                # print("move down passed")
                                break
                        elif ag.movement(self.getState(self.StartGrid))==2:
                            if self.moveRight()==0:
                                goo=1
                                # print("movew right failed")
                            else:
                                goo=0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid))
                                # ag.currentLoc()
                                # print("move right passed")
                                break
                        elif ag.movement(self.getState(self.StartGrid))==3:
                            if self.moveLeft()==0:
                                goo=1
                                # print("movew left failed")
                            else:
                                goo=0
                                ag.consumedMoves+=1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid))
                                # ag.currentLoc()
                                # print("move left passed")
                                break

            else:
                print("\nAll moves consumed but grid not solved by SIMPLE REFLEX AGENT")
                break

        # print("\nInitial   Grid : ",self.InitialGrid,"\n")
        # print("My Solved Grid : ",self.StartGrid,"\n")
        # print("Expected  Grid : ", self.SolutionGrid,"\n")
        print("Simple: No of Correct Pieces = ", ag.correctPiece, " No of Moves Utilized = ", ag.consumedMoves)


    def validateSides(self,x,y):
        self.list.clear()
        if x-1>-1:
            self.list.append(1)
            # return "UP"
        else:
            self.list.append(0)
        if x+1<self.N:
            self.list.append(1)
            # return "DOWN"
        else:
            self.list.append(0)
        if y-1>-1:
            self.list.append(1)
            # return "LEFT"
        else:
            self.list.append(0)
        if y+1<self.N:
            self.list.append(1)
            # return "RIGHT"
        else:
            self.list.append(0)

    def randomDirection(self):
        return random.randint(1,4)


    def createModelBasedAgent(self):
        ag = ModelBasedAgent(self.moves, self.N,self.StartGrid_2)
        ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
        # ag.currentLoc()
        # print("Moves consumed : ", ag.consumedMoves)
        # print("moves remianing : ", ag.totalMoves - ag.consumedMoves)
        while self.gridSolved(self.StartGrid_2) == 0:  # run until grid is solved or not
            if ag.consumedMoves < ag.totalMoves:  # chek for moves end or not

                # do rotation while reaming in same box
                tempx=self.x_cordinate
                tempy=self.y_cordinate
                move=0
                lastRotation=0
                while ag.state != 1 and ag.consumedMoves < ag.totalMoves:
                    if move==0:
                        if ag.rotation() == 1:
                            lastRotation = 1
                        elif ag.rotation() == 2:
                            lastRotation = 2

                    # chek last rotation and go in that direction
                    if lastRotation == 1:
                        self.clockWise_2(ag)
                        move+=1
                    elif lastRotation == 2:
                        self.antiClockWise_2(ag)
                        move+=1

                    # print("\nafter some moves  : ", self.StartGrid_2)
                    ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                    if self.getState(self.StartGrid_2) == 1:
                        ag.correctPiece += 1
                    # ag.currentLoc()
                    # print("Moves consumed : ", ag.consumedMoves)
                    # print("moves remianing : ", ag.totalMoves - ag.consumedMoves)

                # change box by moving up down left right
                if ag.state == 1 and ag.consumedMoves < ag.totalMoves:
                    # time.sleep(3)
                    # print("\n\nplaced correctly now ready to move")
                    # print("\ntowrads soloution: ", self.StartGrid_2)
                    # print("solution         : ", self.SolutionGrid, "\n")


                    ag.maintainState[self.x_cordinate][self.y_cordinate]=ag.state
                    # print(ag.maintainState)

                    goo = 1
                    while goo == 1:
                        # time.sleep(0.5)
                        # print("i am loop")
                        self.validateSides(self.x_cordinate,self.y_cordinate)

                        if ag.checkMiantainedStates(self.list)=="UP":
                            if self.moveUp() == 0:
                                goo = 1
                                # print("movew up failed")
                            else:
                                goo = 0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))

                                # ag.currentLoc()
                                # print("move up passed")
                                break
                        elif ag.checkMiantainedStates(self.list)=="DOWN":
                            if self.moveDown() == 0:
                                goo = 1
                                # print("movew down failed")
                            else:
                                goo = 0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                # ag.currentLoc()
                                # print("move down passed")
                                break

                        elif ag.checkMiantainedStates(self.list)=="LEFT":
                            if self.moveLeft() == 0:
                                goo = 1
                                # print("movew left failed")
                            else:
                                goo = 0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                # ag.currentLoc()
                                # print("move left passed")
                                break

                        elif ag.checkMiantainedStates(self.list)=="RIGHT":
                            if self.moveRight() == 0:
                                goo = 1
                                # print("movew right failed")
                            else:
                                goo = 0
                                ag.consumedMoves += 1
                                ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                # ag.currentLoc()
                                # print("move right passed")
                                break

                        elif ag.checkMiantainedStates(self.list)=="RANDOM":
                            # print("i am random")
                            if self.randomDirection()==1: #up
                                if self.moveUp() == 0:
                                    goo = 1
                                    # print("movew up failed")
                                else:
                                    goo = 0
                                    ag.consumedMoves += 1
                                    ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))

                                    # ag.currentLoc()
                                    # print("move up passed")
                                    break

                            elif self.randomDirection()==2: #down
                                if self.moveDown() == 0:
                                    goo = 1
                                    # print("movew down failed")
                                else:
                                    goo = 0
                                    ag.consumedMoves += 1
                                    ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                    # ag.currentLoc()
                                    # print("move down passed")
                                    break

                            elif self.randomDirection()==3: #left
                                if self.moveLeft() == 0:
                                    goo = 1
                                    # print("movew left failed")
                                else:
                                    goo = 0
                                    ag.consumedMoves += 1
                                    ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                    # ag.currentLoc()
                                    # print("move left passed")
                                    break

                            elif self.randomDirection()==4: #right
                                if self.moveRight() == 0:
                                    goo = 1
                                    # print("movew right failed")
                                else:
                                    goo = 0
                                    ag.consumedMoves += 1
                                    ag.percept(self.x_cordinate, self.y_cordinate, self.getState(self.StartGrid_2))
                                    # ag.currentLoc()
                                    # print("move right passed")
                                    break
            else:
                print("\nAll moves consumed but grid not solved by MODEL BASED AGENT")
                break

        # print("\nInitial   Grid : ", self.InitialGrid, "\n")
        # print("My Solved Grid : ", self.StartGrid_2, "\n")
        # print("Expected  Grid : ", self.SolutionGrid, "\n")
        print("Model: No of Correct Pieces = ", ag.correctPiece, " No of Moves Utilized = ", ag.consumedMoves)



# Agent Class

class SimpleAgent:

    def __init__(self,totalmoves,gridSize):
        # print("I am simple agent counstructor")
        self.totalMoves=totalmoves
        self.gridSize=gridSize
        self.x_cordinate=None
        self.y_cordinate=None
        self.consumedMoves=0
        self.state=None
        self.move=None
        self.correctPiece=0

    def percept(self,x,y,state):
        self.x_cordinate=x
        self.y_cordinate=y
        self.state=state


    def currentLoc(self):
        print("my x cordinate : ",self.x_cordinate)
        print("my y cordinate : ",self.y_cordinate)
        print("my current state : ",self.state)

    def rotation(self):
        rotateSide=random.randint(1,2)

        if rotateSide==1: #goo cockwise
            # print("\nMoving clock wise")
            return 1
        elif rotateSide==2:  #goo anti clockwise
            # print("\nMoving anti clock wise")
            return 2

    def movement(self,st):
        self.percept(self.x_cordinate,self.y_cordinate,st)
        if st==1:
            goo=1
            while(goo==1):
                randomSide=random.randint(0,3)
                # print("Random move : ", randomSide)
                if randomSide==0: #move up x,y--
                    return 0
                elif randomSide==1: #move down x,y++
                    return 1
                elif randomSide==2: #move right x++,y
                    return 2
                elif randomSide==3: #move left x--,y
                    return 3

class ModelBasedAgent:

    def __init__(self,totalmoves,gridSize,StartGrid):
        # print("I am simple agent counstructor")
        self.totalMoves=totalmoves
        self.gridSize=gridSize
        self.x_cordinate=None
        self.y_cordinate=None
        self.consumedMoves=0
        self.state=None
        self.move=None
        self.correctPiece=0
        self.StartGrid=StartGrid
        self.maintainState=[]

        for i in range(self.gridSize):
            temp = []
            for j in range(self.gridSize):
                temp.append(0)
            self.maintainState.append(temp)

    def percept(self,x,y,state):
        self.x_cordinate=x
        self.y_cordinate=y
        self.state=state


    def currentLoc(self):
        print("my x cordinate : ",self.x_cordinate)
        print("my y cordinate : ",self.y_cordinate)
        print("my current state : ",self.state)

    def rotation(self):

        rotateSide=random.randint(1,2)

        if rotateSide==1: #goo cockwise
            # print("\nMoving clock wise")
            return 1
        elif rotateSide==2:  #goo anti clockwise
            # print("\nMoving anti clock wise")
            return 2

    def checkMiantainedStates(self,list):
        if list[0]==1: #chek up
            if self.maintainState[self.x_cordinate-1][self.y_cordinate]==0: #not placed corecctly
                return "UP"
            else:
                pass
        if list[1]==1:
            if self.maintainState[self.x_cordinate+1][self.y_cordinate]==0:
                return "DOWN"
            else:
                pass
        if list[2]==1:
            if self.maintainState[self.x_cordinate][self.y_cordinate-1]==0:
                return "LEFT"
            else:
                pass
        if list[3]==1:
            if self.maintainState[self.x_cordinate][self.y_cordinate+1]==0:
                return "RIGHT"
            else:
                pass
        return "RANDOM"




    def movement(self,st):
        self.percept(self.x_cordinate,self.y_cordinate,st)
        if st==1:
            goo=1
            while(goo==1):
                randomSide=random.randint(0,3)
                # print("Random move : ", randomSide)
                if randomSide==0: #move up x,y--
                    return 0
                elif randomSide==1: #move down x,y++
                    return 1
                elif randomSide==2: #move right x++,y
                    return 2
                elif randomSide==3: #move left x--,y
                    return 3
# Mian fucntion


def main():
    N=int(input("Enter value of N to create Grid : "))
    moves=int(input("Enter Number of Moves : "))
    env=Environment(N , moves)
    print("\nPlease WAIT Agnet's are Soling the Puzzle . . .\n")
    env.createAgent()
    env.createModelBasedAgent()
    print("\nWait Over Puzzle is Solved\n")
    time.sleep(5)

if __name__== "__main__" :
    main()


