LinkedList = [] # Global array 
FirstNode = - 1
FirstEmpty = 0

for i in range(20):
    LinkedList.append([-1, i + 1])

LinkedList[19][1] = -1

def InsertData():
    global FirstNode
    global FirstEmpty
    global LinkedList

    for i in range(5):
        if FirstEmpty != -1:
            NewNode = FirstEmpty
            FirstEmpty = LinkedList[FirstEmpty][1]
            LinkedList[NewNode][0] = int(input("Enter a number: "))
            LinkedList[NewNode][1] = FirstNode
            FirstNode = NewNode

def OutputLinkedList():
    global FirstNode
    global LinkedList

    CurrentNode = FirstNode

    while CurrentNode != -1:
        print(LinkedList[CurrentNode][0])
        CurrentNode = LinkedList[CurrentNode][1]

def RemoveData(dataItem):
    global FirstNode
    global FirstEmpty
    global LinkedList

    CurrentNode = FirstNode
    PreviousNode = -1

    while CurrentNode != -1:
        if LinkedList[CurrentNode][0] == dataItem:
            if PreviousNode == -1:
                FirstNode = LinkedList[CurrentNode][1]
            else:
                LinkedList[PreviousNode][1] = LinkedList[CurrentNode][1]
            LinkedList[CurrentNode][1] = FirstEmpty
            FirstEmpty = CurrentNode
            return
        PreviousNode = CurrentNode
        CurrentNode = LinkedList[CurrentNode][1]

InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
