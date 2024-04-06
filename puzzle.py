
from turtle import Screen, Turtle
import math
import random
import os.path
import time


directory_path = os.path.dirname(__file__)   
resource_path = os.path.join(directory_path, "Resources")
image_path = os.path.join(directory_path, "Images")


class Puzzle:
    """
        the puzzle game board where players play
    attributes:
        GRID_POS. GRID_SIZE, BADGE_POS, turtle
        screen, disPuz, maxmove, initial order, initial move

    methods:

    """
    # position of the game column
    GRID_POS = [(-300,275),(100,275),(100,-125),(-300,-125)]   # 4 corner of the grids
    X = [GRID_POS[0][0], GRID_POS[1][0]]
    Y = [GRID_POS[2][1], GRID_POS[0][1]]

    GRID_SIZE = 100
    BADGE_POS = (300, 280)  # middle pos

    t_puzzle = Turtle(visible=False)
    t_puzzle.speed(0)
    tMoves = Turtle(visible=False)   # turtle that records moves 

    def __init__(self, dicPuz: dict, maxmove: int, screen):      
        ### documents for init???

        self.screen = screen
        self.dic = dicPuz
        self.max = maxmove        

        self.game = dicPuz["name"]
        self.picSize = int(dicPuz["size"])     # pic size int
        self.total = int(dicPuz["number"])     # total number of pics
        self.width = int(math.sqrt(self.total))      # how many rows & columns

        # initialize ascending order & move
        self.order = [i for i in range(1, self.total + 1)]  
        self.solve = False
        self.move = 0        
        
        # a list to record the position of each grids (left, up)
        self.posLst = self.pos_list()               

    def pos_list(self):
        """
        Function:
            return a list of positions(left, up) of each grids in order
        Parameters: 
            None
        Return: 
            lst(list)-- list of position tuples
        """
        lst = []
        first = list(self.GRID_POS[0])    # left upper corner coordinate

        for y in range(self.width):     # row
            for x in range(self.width):     # column
                lst.append(tuple(first))
                first[0] += self.GRID_SIZE

            first[0] -= self.width * self.GRID_SIZE     # back to first cloumn
            first[1] -= self.GRID_SIZE      # next row

        return lst      # [(),(),()...]
   
    def shuffle(self):
        """
        Function:
            shuffle the order list.        
        Returns:
            None      
        """ 
        random.shuffle(self.order)
        self.solvable()

    def solvable(self):
        """
        Function:
            determine whether the puzzle is solvable,
            and change the solve attribute      
        Returns:
            Non3   
        """ 
        # inversion number
        inverse = 0
        
        for i in range(self.total):
            for n in range(i + 1, self.total):
                if self.order[i] > self.order[n] and self.order[i] != self.total and self.order[n] != self.total:
                    inverse += 1

        # count is odd 
        if self.width % 2 == 1:

            # odd width is solvable with even inversion
            self.solve = (inverse % 2 == 0)

            if self.solve:
                print("solvable")
            else:
                print("unsolvable")

        # count is even
        if self.width % 2 == 0:
            i = self.order.index(self.total)
            blank = i // self.width

            # even width is solvable with odd sum
            sum_even = inverse + blank
            self.solve = (sum_even % 2 == 1)   

            if self.solve:
                print("solvable")
            else:
                print("unsolvable") 

    def badge(self):
        """
        Function:
            display the badge of the selected puz
        Parameters: 
            none
        Return: 
            None  
        """        
        self.t_puzzle.penup()
        self.t_puzzle.goto(self.BADGE_POS)
        badge_path = os.path.join(directory_path, self.dic["thumbnail"])
        self.screen.register_shape(badge_path)
        self.t_puzzle.shape(badge_path)
        self.t_puzzle.stamp()
        self.t_puzzle.hideturtle()
    
    def checkOrder(self, record):
        """
        Function:
            check the game win or lose or continue
        Parameters: 
            record(object)-- pass the record to win()
        Return: 
            none
        """

        if self.move >= self.max:
            self.lose()

        else:
            for i in range(self.total):
                
                if i + 1 != self.order[i]:
                    return      ### ????
                
            self.win(record)
    
    def popMsg(self, file):  
        """
        Function:
            pop a prompt for 2 seconds
        Parameters: 
            filr(str)-- the name of the file that poped
        Return: 
            None  
        """    
        msg = Turtle()

        loadMsg_path = os.path.join(resource_path, file)
        self.screen.register_shape(loadMsg_path)
        msg.penup()
        msg.home()
        msg.shape(loadMsg_path)
        time.sleep(2)
        msg.hideturtle()

    def lose(self):
        """
        Function:
            pop the lose window and exit
        Parameters: 
            none
        Return: 
            None  
        """
        # pop lose msg
        self.popMsg("Lose.gif")

        # pop end msg & exit
        self.end()

    def win(self, record):
        """
        Function:
            pop the win window, register the record and exit
        Parameters: 
            none
        Return: 
            None  
        """ 
        # check if beats the current record
        record.check(self.move)
        record.writeRecord()
        record.display()

        # pop win msg
        self.popMsg("winner.gif")   

        # pop end msg & exit
        self.end()

    def end(self):

        self.popMsg("credits.gif")
        self.screen.bye()  

    def square(self, index: int):
        """
        Function:
            draw square around the puzzle pic from left, up
        Parameters: 
            index(int)-- the index of the grid
        Return: 
            None  
        """
        self.t_puzzle.penup()
        self.t_puzzle.pensize(1)
        self.t_puzzle.pencolor("black")

        x = self.posLst[index][0] + (100 - (self.picSize + 2)) // 2
        y = self.posLst[index][1] - (100 - (self.picSize + 2)) // 2

        self.t_puzzle.goto(tuple([x,y]))

        self.t_puzzle.pendown()

        for _ in range(4):
            self.t_puzzle.fd(self.picSize + 2)
            self.t_puzzle.right(90)

    def display(self, index: int): 
        """
        Function:
            display the pic at the given grid index
        Parameters: 
            index(int)-- the index of the grid
        Return: 
            None  
        """

        pic_index = self.order[index]   # the index of pic path
        pic = self.dic[pic_index]    # string of pic path relatively

        pic_path = os.path.join(directory_path, pic)    # string of pic path
        self.screen.register_shape(pic_path)
        self.t_puzzle.penup()
        
        # stamp pic
        self.t_puzzle.penup()
        self.t_puzzle.goto(tuple([self.posLst[index][0] + 50, self.posLst[index][1] - 50]))   # go to position
        self.t_puzzle.shape(pic_path)      
        self.t_puzzle.stamp()   # add pic

    def startDisplay(self):
        """
        Function:
            display the pic and square of each grid at start
        Parameters: 
            none
        Return: 
            None  
        """
        for i in range(self.total):
            self.square(i)
            self.display(i)

    def neighbor(self, index: int):
        """
        Function:
            return the neighbour position of the given grid index
        Parameters: 
            index(int)-- the index of the grid
        Return: 
            neighbor(list)-- the list of the neighbor grids position
        """
        neighbor = [index - self.width, index - 1, index + 1, index + self.width] 
        
        if index % self.width == 0:
            neighbor.remove(index - 1)

        if (index + 1) % self.width == 0:
            neighbor.remove(index + 1)

        for i in neighbor:
            if i < 0 or i >= self.total:
                neighbor.remove(i)

        return neighbor     # list
    
    def click(self, x, y, record):  ### ????
 
        for i in range(self.total):
            if x > self.posLst[i][0] and x < self.posLst[i][0] + self.GRID_SIZE:
                if y > self.posLst[i][1] - self.GRID_SIZE and y < self.posLst[i][1]:
                    self.swap(i, record)    # pos
   
    def swap(self, index, record):
        neighbor = self.neighbor(index)  # list

        for i in neighbor:
            if self.order[i] == self.total:
                self.order[i], self.order[index] = self.order[index], self.total

                # update moves
                self.move += 1
                self.moveDisplay()

                self.display(index)
                self.display(i)
                self.checkOrder(record)

    def moveDisplay(self):        
        
        self.tMoves.penup()
        self.tMoves.goto(-300, -275)
        self.tMoves.clear()
        self.tMoves.write(f"Player Moves: {self.move}", font=("Arial", 20, "normal"))

    def reset(self):

        self.order = [i for i in range(1, self.total + 1)]  # initialize ascending order
        self.move = 0
        self.moveDisplay()

        for i in range(self.total):
            self.display(i)

