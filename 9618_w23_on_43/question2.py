
from numbers import Number


Queue = ['' for i in range(50)] # Array of STRING, 50 spaces
HeadPointer = -1
TailPointer = 0

def Enqueue(value: str):
    global Queue, HeadPointer, TailPointer

    if HeadPointer == -1:
        Queue[TailPointer] = value
        HeadPointer = 0
        TailPointer = TailPointer + 1
        print("Added element")
    else:
        if TailPointer > 49:
            print("Queue is full")
        else:
            Queue[TailPointer] = value
            TailPointer = TailPointer + 1
            print("Added Element")

def Dequeue():
    global Queue, HeadPointer, TailPointer

    if HeadPointer == -1 or TailPointer == 0 or HeadPointer == TailPointer:
        return 'Empty'
    else:
        nextItem = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        return nextItem

def ReadData():

    try:
        file = open("QueueData.txt", 'r')

        NextLine = file.readline().strip()

        while NextLine != "" :
            Enqueue(NextLine)
            NextLine = file.readline().strip()

        file.close()
    except IOError:
        print("File not found")

class RecordData:
    def __init__(self):
        self.ID : str = ""   # Record ID: STRING
        self.Total = 0  # Total times ID appears: INTEGER

Records = [RecordData() for i in range(50)]        # Array of RecordData, 50 spaces
NumberRecords = 0   # Number of Records : INTEGER

def TotalData():
    global Records, NumberRecords

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed 
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for x in range(NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total = Records[x].Total + 1
                Flag = True
    
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords = NumberRecords + 1

def OutputRecords():
    global Records, NumberRecords

    for i in range(NumberRecords):
        print("ID " + str(Records[i].ID) + " Total " + str(Records[i].Total))

ReadData()

for i in range(HeadPointer, TailPointer):
    TotalData()

OutputRecords()

