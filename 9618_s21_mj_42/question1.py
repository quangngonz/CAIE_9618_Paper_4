from ctypes import pointer


class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
emptyList = 5

def outputNodes(nodeArray : list[node], startPointer):
    currentPointer = startPointer

    while currentPointer != -1:
        print(str(nodeArray[currentPointer].data)) 
        currentPointer = nodeArray[currentPointer].nextNode

def addNode(linkedList : list[node], currentPointer, emptyList):
    dataToAdd = int(input("Enter number to add: "))

    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newNode = node(dataToAdd, -1)
        linkedList[emptyList] = newNode

        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode

        return True
    

outputNodes(linkedList, startPointer)

result = addNode(linkedList, startPointer, emptyList)

if result == True:
    print("Item successfully added")
else:
    print("Failed to add item")

outputNodes(linkedList, startPointer)
