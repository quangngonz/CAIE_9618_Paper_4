
from threading import ThreadError


class Queue:
    def __init__(self, queue, headPointer, tailPointer):
        self.QueueArray = queue         # Array up to 100 INTEGER values
        self.Headpointer = headPointer  # Index first data Item
        self.Tailpointer = tailPointer  # Index next free location

    def Enqueue(self, theData: int):
        if self.Headpointer == -1:
            self.QueueArray[self.Tailpointer] = theData
            self.Headpointer = 0
            self.Tailpointer = self.Tailpointer + 1
            return 1
        else:
            if self.Tailpointer > 100:
                return -1
            else:
                self.QueueArray[self.Tailpointer] = theData
                self.Tailpointer = self.Tailpointer + 1
                return 1
    
    def Dequeue(self):
        if self.Tailpointer == 0:
            return -1 
        else:
            nextItem = self.QueueArray[self.Headpointer]
            self.Headpointer = self.Headpointer + 1

            return nextItem
            


emptyQueue = []
for i in range(100):
    emptyQueue.append(-1)

TheQueue = Queue(emptyQueue, -1, 0)

def ReturnAllData():
    global TheQueue

    OutputString = ""

    for i in range(TheQueue.Headpointer, TheQueue.Tailpointer):
        OutputString = OutputString + str(TheQueue.QueueArray[i]) + " "

    return OutputString

for i in range(10):
    InputValue = -1

    while InputValue < 0:
        InputValue = int(input("Input next value: "))
    
    ReturnValue = TheQueue.Enqueue(InputValue)

    if ReturnValue == -1:
        print("Queue is full")

outputString = ReturnAllData()

print(outputString)

for i in range(2):
    NextValue = TheQueue.Dequeue()

    if NextValue == -1:
        print("Queue is empty")
    else:
        print(NextValue)
    
    
