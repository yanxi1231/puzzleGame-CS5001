

from turtle import Screen, Turtle

from puzzle import Puzzle
from record import Record

class Gameboard():
    """
        Gameboard control the whole game.
    attributes:
        3 columns position, puzzle, menu, record objects,
        player name, maxmove, screen
    methods:
        square-- draw square.(None)
        drawBoard-- draw 3 boards.(None)
        click-- perform different tasks according to click.(None)
        initialize-- initialize the new game.(None)
    """

    # gameboard positon 4 corner
    PUZZLE_POS = [(-325,300),(125,300),(125,-150),(-325,-150)]
    LEAD_POS = [(145,300),(325,300),(325,-150),(145,-150)]
    MENU_POS = [(-325,-200),(325,-200),(325,-320),(-325,-320)]


    def __init__(self, puzzle, menu, record, moves, player, screen) -> None:

        self.puzzle = puzzle
        self.menu = menu
        self.record = record

        self.maxmove = moves
        self.player = player      
        self.screen = screen  

    def square(self, pos: tuple, color: str):
        """
        Function:
            draw square
        Parameters: 
            pos(tuple)-- position of left upper corner of the square
            color(str)-- color of square
        Return: 
            None  
        """        
        # set pen
        tBoard = Turtle(visible=False)  
        tBoard.speed(0)
        tBoard.pensize(5)
        tBoard.pencolor(color)

        # draw
        tBoard.penup()    
        tBoard.goto(pos[0])     # left upper corner
        tBoard.pendown()  

        # draw square according to the 4 corner coordinate  
        for i in range(1,4):
            tBoard.goto(pos[i])
        tBoard.goto(pos[0])

    def drawBoard(self):
        """
        Function:
            draw 3 squre on the gameboard
        Parameters: 
            none
        Return: 
            None  
        """        
        # column 1 puzzle
        self.square(self.PUZZLE_POS, "black")

        # column 2 menu
        self.square(self.MENU_POS, "black")

        # column 3 lead
        self.square(self.LEAD_POS, "blue")

    def click(self, x, y):  
        """
        Function:
            perform different tasks according to click.
        Parameters: 
            x(int)-- x coordinate of the click
            y(int)-- y coordinate of the click
        Return: 
            None  
        """                 
        # puzzle area
        if x > self.puzzle.X[0] and x < self.puzzle.X[1] and y > self.puzzle.Y[0] and y < self.puzzle.Y[1]:
            self.puzzle.click(x, y, self.record)
        
        # menu area 
        elif x > self.menu.X[0] and x < self.menu.X[1] and y > self.menu.Y[0] and y < self.menu.Y[1]:
            
            # load
            if x > self.menu.R_L_Q[1][0] - 40 and x < self.menu.R_L_Q[1][0] + 40:

                # user input puz
                puz = self.menu.load()                                

                if puz != None:
                    self.puzzle.t_puzzle.clear()    # puzzle area
                    self.puzzle.tMoves.clear()      # moves area
                    self.record.t_record.clear()    # record area                

                    # load new game
                    dicPuz = self.menu.readPuz(puz)
                    self.puzzle = Puzzle(dicPuz, self.maxmove, self.screen)
                    self.record = Record(self.player, dicPuz)
                    self.initialize()
 
            # reset & quit
            else:
                self.menu.click(x, self.puzzle)

    def initialize(self):   
        """
        Function:
            initialize the game
        Parameters: 
            None
        Return: 
            None  
        """     
        # puzzle area
        self.puzzle.shuffle()
        while self.puzzle.solve == False:
            self.puzzle.shuffle()
        self.puzzle.startDisplay()
        self.puzzle.badge()  

        # record area
        self.record.readRecord()
        self.record.display()

        # register click
        self.screen.onscreenclick(self.click)

