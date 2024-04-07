import os
from turtle import Turtle
import time

directory_path = os.path.dirname(__file__)   
resource_path = os.path.join(directory_path, "Resources")
image_path = os.path.join(directory_path, "Images")
                               
class Record():
    """
        the record column on the right of the window.
    attributes:
        player name, current game, records file
        allRecord, the Record, record position
    methods:
        readRecord-- read the old record of all games
        check-- check if the new one beats the record, keep top 5 records.(none)

    """

    def __init__(self, player, puzDic):
        """
        Function:
            
        Parameters: 
            player(str)-- the player's name
            puzDic(dict)-- the current game info dict
        Return: 
            None
        """      
        self.name = puzDic["name"]    # game name
        self.player = player        # player's name
        self.file = os.path.join(directory_path, "Records.txt")

        self.t_record = Turtle(visible=False)
        
        self.leadPos = (160, 200)
        self.allRecord = []       # ["mario: 1,nyx,11 2,yanxi,48 3,Na,66", "yoshi: 1,oo,356"] or []
        self.theRecord = []     # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []

    def readRecord(self):
        """
        Function:
            read the old record of all games
            current playing game's old record-- self.theRecord
            append all the other records to-- self.allRecord
        Parameters: 
            None            
        Return: 
            None
        """
        try:
            with open(self.file, "r", encoding='utf-8') as file:
                all = file.readlines()

                for line in all:
                    if line.strip():
                        note = line.split()
                        game = note[0].strip(":")           # "mario"

                        if game == self.name:       # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []

                            for top in note[1:]:
                                record = top.split(",")
                                record[0] = int(record[0])
                                record[2] = int(record[2])
                                self.theRecord.append(record)

                        else:
                            self.allRecord.append(line)       # apend other game's record (str) needn't change

        except FileNotFoundError:
            self.popMsg("leaderboard_error.gif")

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

    def check(self, move):
        """
        Function:
            check if the new one beats the current record,
            and keep top 5(at most) records
        Parameters: 
            move(int)-- the player's move
        Return: 
            None
        """        
        # no previous record
        if not self.theRecord:
            self.theRecord.append([1, self.player, move])    

        # have previous record
        else:
            length = len(self.theRecord)
            for i in range(length):

                # same moves already in the old list
                if self.theRecord[i][2] == move and self.theRecord[i + 1][2] > move:
                    self.theRecord.insert(i + 1, [self.theRecord[i][0], self.player, move])
                    for k in range(i + 2, length + 1):
                        self.theRecord[k][0] += 1
                    
                    new = self.theRecord[0:5] 
                    self.theRecord = new
                    return 

                # no same moves in the old list
                elif self.theRecord[i][2] > move:
                    self.theRecord.insert(i, [self.theRecord[i][0], self.player, move])
                    for k in range(i + 1, length + 1):
                        self.theRecord[k][0] += 1
                    new = self.theRecord[0:5]  # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []
                    self.theRecord = new
                    return

            # not beats any current record            
            self.theRecord.append([length + 1, self.player, move])
            new = self.theRecord[0:5]
            self.theRecord = new     

    def writeRecord(self):
        """
        Function:
            write the record to the record file
        Parameters: 
            none
        Return: 
            None
        """ 
        # add theRecord to allRecord
        add = ""
        for p in self.theRecord:
            for i in range(3):
                p[i] = str(p[i])
            add = add + " " + ",".join(p)

        self.allRecord.append(f"{self.name}:{add}")

        # write records                
        with open(self.file, "w", encoding='utf-8') as file:
            for line in self.allRecord:
                file.write(line)    
                file.write("\n")    # new line???

    def display(self):
        """
        Function:
            display the current record
        Parameters: 
            None
        Return: 
            None
        """
        recordLst = self.theRecord   

        # leaders
        self.t_record.penup()        
        self.t_record.goto(self.leadPos)
        self.t_record.write(f"{self.name} Leaders:", font=("Arial", 15, "normal"))

        # top players         
        pos = [self.leadPos[0], self.leadPos[1] - 80]  
        
        for p in recordLst:
            self.t_record.penup()
            self.t_record.goto(tuple(pos))
            self.t_record.write(f"{p[0]}: {p[1]}  ({p[2]}moves) \n", font=("Arial", 12, "normal"))   
            pos[1] -= 30  

