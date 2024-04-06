import os.path
from turtle import Screen, Turtle
import time

directory_path = os.path.dirname(__file__)   
resource_path = os.path.join(directory_path, "Resources")
image_path = os.path.join(directory_path, "Images")

class Menu:
    """
        the menu column on the bottom of the window.
    attributes:
        button position
    methods:
        puzLst-- return all .puz file with its name in a (list).
        readPuz-- read .puz file and return an info (dict).  
        checkMalformed-- check if the dict info is malformed. (Boolean)    
        display_botton-- display 3 button on the menu.(None)
        click-- choose a task to perform by the click.(None)
        reset-- shuffle the current puzzle game
        quit-- quit the game
        load-- user select a puz game.(str)
        popMsg-- pop a prompt for 2 seconds.(None)
    """
    ###  here or init ????

    # center coordinate of the button
    R_L_Q = [(50, -260), (150, -260), (250, -260)]  
    X = [10, 290]       # x range
    Y = [-300, -220]    # y range
    BUTTON_SIZE = 80

    def __init__(self, screen) -> None:        
        self.screen = screen

    def puzLst(self):
        """
        Function:
            return all .puz file with its name in a list.        
        Input: 
            None
        Returns:
            puz_lst(list)-- ["mario.puz", "yoshi.puz"...]
        """ 
        # read all files in current directory
        dir_lst = os.listdir(directory_path)    

        puz_lst = []
        for i in dir_lst:
            if i.endswith(".puz"):
                puz_lst.append(i)
        
        return puz_lst

    def readPuz(self, puz):
        """
        Function:
            read .puz file and return an info dict.        
        Input: 
            puz(str)-- the current game's puz file 
        Returns:
            dict-- {" ":" ", int:"path"}        
        """ 
        puzPath = os.path.join(directory_path, puz)

        try:
            # read the puz file
            with open(puzPath, "r") as file:
                lines = file.readlines()
                puzInfo = {}  

                for line in lines:
                    words = line.split()  # ["1:", "path.gif"]

                    try:        # if the .gif index info
                        index = int(words[0].strip(":"))  
                        puzInfo[index] = words[1]

                    except ValueError:      # if the other info
                        puzInfo[words[0].strip(":")] = words[1] 

                return puzInfo
            
        except FileNotFoundError:            ### other error???
            self.popMsg("file_error.gif")

    def checkMalformed(self, puz: dict): 
        """
        Function:
            check if the dict info is malformed.
        Parameters: 
            none
        Return: 
            Boolean
        """
        # types of malformed??? 1.number 2. size.... ????
        # pop a malform message of not show on load menu at all????

    def display_botton(self):
        """
        Function:
            display 3 button on the menu
        Parameters: 
            none
        Return: 
            None  
        """
        button = ["resetbutton.gif", "loadbutton.gif", "quitbutton.gif"]
        t_botton = Turtle(visible = False)
        t_botton.speed(0)

        for i in range(3):
            path = os.path.join(resource_path, button[i])
            self.screen.register_shape(path)
            
            t_botton.shape(path)
            t_botton.penup()
            t_botton.goto(self.R_L_Q[i])
            t_botton.stamp()

    def click(self, x, puzzle):
        """
        Function:
            reset or quit by the click's x coordinate
        Parameters: 
            puzzle(object)
            x(int) -- the x coordinate of the click
        Return: 
            None  
        """
        # reset   
        if x > self.R_L_Q[0][0] - 40 and x < self.R_L_Q[0][0] + 40:
            self.reset(puzzle)
        
        # quit
        elif x > self.R_L_Q[2][0] - 40 and x < self.R_L_Q[2][0] + 40:
            self.quit()    

    def reset(self, puzzle):
        """
        Function:
            shuffle the current puzzle game
        Parameters: 
            puzzle(object)
        Return: 
            None  
        """
        puzzle.reset()

    def quit(self):
        """
        Function:
            quit the game
        Parameters: 
            none
        Return: 
            None  
        """
        # pop Msg
        self.popMsg("quitmsg.gif")
        self.popMsg("credits.gif")

        # log out screen
        self.screen.bye() 

    def load(self):
        """
        Function:
            user select a puz game
        Parameters: 
            None
        Return: 
            puzzle(str) or None--  .puz str
        """
        content = "Enter the name of the puzzle you wish to load. Choices are:"

        puzLst = self.puzLst()
        # if more than 10 .puz, return first 10
        if len(puzLst) > 10:
            self.popMsg("file_warning.gif")
            puzLst = puzLst[:10]

        for p in puzLst:
            content = content + "\n" + p

        puzzle = self.screen.textinput("Load Puzzle", content)

        # valid input
        if puzzle in puzLst:
            return puzzle   # .puz str
        
        # invalid input
        else:
            self.popMsg("file_error.gif")  # invalid input

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







