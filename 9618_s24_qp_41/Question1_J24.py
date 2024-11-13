
# 1(a)
DataStored = [] # A global 2D array of 20 integers
NumberItems = 0 # Global varible which stores the quantity of items the array contains

# 1(b)
def Initialise():
    global DataStored, NumberItems

    # Prompt the user to input the quantity of numbers to enter
    NumberItems = int(input("Please enter the number of items to enter: "))

    # Validate the number no make sure it's within range
    while NumberItems > 20 or NumberItems < 1:
        NumberItems = int(input("Please enter the number of items to enter: "))
    
    # Input each number
    for i in range(NumberItems):
        input_no = int(input())
        DataStored.append(input_no)

# 1(c)(i)
NumberItems = 0 
Initialise()

print("Data stored:", DataStored)

# 1(d)(i)
def BubbleSort():
    global DataStored

    swapped = True

    while swapped:
        swapped = False

        for i in range(NumberItems-1):
            if DataStored[i] > DataStored[i+1]:
                temp = DataStored[i]
                DataStored[i] = DataStored[i+1]
                DataStored[i+1] = temp
                swapped = True

BubbleSort()
print("Data stored sorted:", DataStored)

def BinarySearch(DataToFind):
    global DataStored

    for i in range(NumberItems):
        if DataStored[i] == DataToFind:
            return i
    
    return -1
