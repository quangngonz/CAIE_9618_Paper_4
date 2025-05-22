arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] # Array [0: 10] of INTEGER

def linearSearch(target: int):
    global arrayData

    for i in range(10):
        if arrayData[i] == target:
            return True
        
    return False

searchValue = int(input("Input target value: "))

found = linearSearch(searchValue)

if found == True:
    print("Value found in list")
else:
    print("Value not found in list")

def bubbleSort():
    global arrayData

    temp = 0

    for x in range(10):
        for y in range(9):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp


