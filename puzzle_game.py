'''
   CS5001
   Spring 2024
   Yanxi Na
   Project: puzzle game
'''

from turtle import Screen, Turtle
import os.path
import time

from puzzle import Puzzle
from record import Record
from menu import Menu
from gameboard import Gameboard

"""
# Show the Splash Screen before gameplay starts. The splash screen should "linger" for 3-4 seconds before you erase it, so your user can bask in the glow of your game's awesomeness. We're big-time game designers now and every big-time game has a splash screen.
# The player should be able to input their name to your game through a pop-up window rather than in the terminal.
# The player should be allowed to select the number of "moves" they can have to unscramble the puzzle. The lower limit is 5, the upper limit is 200. If the player unscrambles the puzzle in less than (or equal to) the number of moves they've chosen, they win the game. If they do not unscramble the puzzle within the number of allowed moves specified, they lose the game.
NOTE: Some 15-puzzles (about 50%) are unsolvable. Using a simplistic tile swap or Python's shuffle() will often result in unsolvable puzzles. For this project, you do NOT need to guarantee a solvable puzzle. However, you may earn extra credit for identifying a non-solvable puzzle and/or for presenting your user with a guaranteed solvable puzzle (you'll need to do a bit of research on how to do this).
Moves are completed when the player clicks on a piece (I call them Tiles in my game) that is adjacent to a blank square (empty Tile). Logical description (you can implement this any way you wish): The Tile that is clicked shifts to the place where the blank was, and the blank shifts to where the clicked Tile was. Legal shifts are ONLY horizontal or vertical (no diagonal shifts are allowed). A status area on the playing surface updates and displays the number of moves a player has completed.
If the player clicks on a Tile that is NOT adjacent to a blank, nothing happens. No shifts occur and the click does NOT count as a move. Only actual shifts of the Tiles count as a move.
A status line in the game is updated when each move is completed by the player. If the player uses more moves than the "max moves" they've selected in rule #3 above, they "lose" the game. A message indicating that should be shown, and the program should end. If the player unscrambles the puzzle in less moves than selected in rule #3 above, they "win" the game. A message indicating that victory should be shown, and the program should end.
A player must be allowed to use the "Reset" button to auto-unscramble the puzzle. The game does NOT end if they press Reset, but the puzzle is displayed in its completed form (think of the reset as a "cheat code" for those of us who get frustrated with puzzles).
A player must be allowed to load a different puzzle from the file system using the Load button. Do not hardcode the "starter pack" puzzle names - your code should be able to read any puzzle file from the file system - including new puzzles created by your users (or the instruction team during our testing).
Puzzle files are multi-faceted. The description/meta-data is contained in a .puz file, and the actual resources are contained in directories within the Images directory given to you (more information on this follows below). If the user loads a different puzzle, the move count resets to zero (0) and the current puzzle to solve is updated with the user selection. 
If the user attempts to load a non-existent file, OR a puzzle (.puz) file that has malformed data, your program should display an error message and continue processing. Missing files are recoverable errors that should NOT crash your system.
??? Your program should also log any errors to an error file called 5001_puzzle.err. This is a text file which your support team will use to help investigate issues as you work on version 2 (because we know version 1 will be a blockbuster!). An example of my error file is given below
# A player can quit and exit the game at any time using the Quit button.
# OPTIONAL: When the program exits show a Credits screen before the program terminates. You can use the Credits resource I've provided, or create your own

"""

#### tkinter while running the program?
  
# the resources path
directory_path = os.path.dirname(__file__)   
resource_path = os.path.join(directory_path, "Resources")
image_path = os.path.join(directory_path, "Images")

def main():

    # initialize screen
    screen = Screen()
    screen.setup(width = 800, height = 700)  
    screen.title("CS5001 Sliding Puzzle Game")

    # Show the Splash Screen for 3 seconds
    splash(screen)
    # player input name through a pop-up window, str
    player_name = screen.textinput("CS5001 Puzzle Slide", "Your name:") 
    # input the number of "moves" [5, 200], int or None(canceled)
    moves = int(screen.numinput("CS5001 Puzzle Slide - Moves", 
                            "Enter the number of moves (chances) you want? (5-200)", 
                            default=None, minval=5, maxval=200))      

    # create menu
    menu = Menu(screen)
    # read .puz file, begin with "mario" -> {" ":" ", int:"path.gif"} 
    dic_puz = menu.readPuz("mario.puz")

    # create puzzle
    puzzle = Puzzle(dic_puz, moves, screen)

    # create reord 
    record = Record(player_name, dic_puz)
    
    # create game board    
    gameBoard = Gameboard(puzzle, menu, record, moves, player_name, screen)

    # initialize the game
    gameBoard.drawBoard()   # draw 3 square column  
    gameBoard.menu.display_botton()     # set botton in menu
    gameBoard.initialize()  # initialize the game
    
    screen.mainloop()       #### ????????
       

def splash(screen): 
    """
    Function:
        Show the Splash Screen before gameplay starts.
        The splash screen should "linger" for 3 seconds.
    Parameters: 
        screen-- the screen that the splash shown on 
    Return: 
        None  
    """    
    splash_path = os.path.join(resource_path, "splash_screen.gif")  
    screen.register_shape(splash_path)

    # set turtle
    t_splash = Turtle(visible = False)
    t_splash.penup()
    t_splash.home() 
    t_splash.shape(splash_path)
    t_splash.showturtle()

    time.sleep(3)   # linger 3 seconds
    t_splash.hideturtle()   # hide splash

if __name__ == "__main__":
    main()


# earn extra credit for identifying a non-solvable puzzle 
# and/or presenting your user with a guaranteed solvable puzzle
    

# moves are completed when the player clicks on a piece

# status area on the playing surface updates and displays the number of moves a player has completed

# clicks on a Tile that is NOT adjacent to a blank, nothing happens. No shifts no counts. 

# lose, message shown, program ends.
# win,  message shown, program ends.

# reset, auto-unscramble the puzzle, game does NOT end, puzzle displayed in completed form

# load button, load a different puzzle

# load a non-existent, or malformed data file. display an error message and continue processing. Missing files are recoverable errors that should NOT crash your system.

# log any errors to an error file called 5001_puzzle.err

# quit button: exit the game at any time

# When the program exits show a Credits screen before the program terminates



#### bonus: 
# (a) determines if the current puzzle is solvable or unsolvable.
# (b) Design Description clearly state that you have implemented this feature. and how we can view the status of "solvable-ness"
# (c) PyUnit test
# (d) guarantee the puzzle you supply to the player is solvable.
# provide a PyUnit test that validates your "puzzle scrambler" such that we can verify it is "solvable"
####


    

