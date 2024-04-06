import os
from turtle import Turtle

                               
class Record():
    
    directory_path = os.path.dirname(__file__)  

    def __init__(self, player, puzDic):

        self.name = puzDic["name"]    # game name
        self.player = player        # player's name
        self.file = os.path.join(self.directory_path, "Records.txt")

        self.t_record = Turtle(visible=False)
        
        self.leadPos = (160, 200)
        self.allRecord = []       # ["mario: 1,nyx,11 2,yanxi,48 3,Na,66", "yoshi: 1,oo,356"] or []
        self.theRecord = []     # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []

    def check(self, move):
        """
        Function:
            check if the new one beats the current record,
            and keep top 5(at most) records
        Parameters: 
            move(int)-- the player's move
        Return: 
            record(list)-- 
        """        
        record = self.theRecord          

        if not self.theRecord:
            record.append([1, self.player, move])   
            new = record         

        else:
            length = len(record)
            for i in range(length):

                # same moves already in the old list
                if record[i][2] == move and record[i + 1][2] > move:
                    record.insert(i + 1, [record[i][0], self.player, move])
                    for k in range(i + 1, length + 1):
                        record[k][0] += 1
                    new = record[0:5]  

                # no same moves in the old list
                elif record[i][2] > move:
                    record.insert(i, [record[i][0], self.player, move])
                    for k in range(i + 1, length + 1):
                        record[k][0] += 1
                    new = record[0:5]  # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []
            
            # not beats any current record
            record.append([length + 1, self.player, move])
            new = record[0:5]
        
        add = ""
        for p in new:
            for i in range(3):
                p[i] = str(p[i])
            add = add + ",".join(p) + " "

        self.allRecord.append(f"{self.name}: {add}")


    def readRecord(self):
        """
        Function:
            read the old record of all games
            current playing game's old record-- self.oldrecord
            append all the other records to-- self.new
        Parameters: 
            None            
        Return: 
            theRecord(list)-- the list of the current game's record
        """
        
        with open(self.file, "r", encoding='utf-8') as file:
            all = file.readlines()
            theRecord = []

            for line in all:
                note = line.split()
                game = note[0].strip(":")           ####  ?????

                if game == self.name:                    
                    for top in note[1:]:

                        record = top.split(",")
                        record[0] = int(record[0])
                        record[2] = int(record[2])
                        theRecord.append(record)

                else:
                    self.allRecord.append(line)       # apend other game's record (str) needn't change

            self.theRecord = theRecord    # [[1,"name", 55], [1,"name2", 55], [3,"", 356]] or []


    def writeRecord(self):
        """
        Function:
            check if the new one beats the current record,
            and keep top 5(at most) records
        Parameters: 
            move(int)-- the player's move
        Return: 
            None
        """ 
        
        with open(self.file, "w", encoding='utf-8') as file:
            for line in self.allRecord:
                file.write(line)


    def display(self):
        """
        Function:
            display the current record
        Parameters: 
            recordLst(list)-- the list of the current top players
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

