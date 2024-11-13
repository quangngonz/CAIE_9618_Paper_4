#2(a)
import random

ArrayData = [] # 2D Array of 10 by 10 integer elements

for i in range(10):
    InsideArray = [] # Blank array for 10 integer elements
    for j in range(10):
        RandomNumber = random.randint(1,100) # Generate a random number between 1 and 100
        InsideArray.append(RandomNumber) # Add to the subarray
    
    ArrayData.append(InsideArray) # Append to main array

def printArrayData():
    global ArrayData
    for i in range(10): # Loop over first dimension
        for j in range(10): # Loop over second dimension
            print(f"{ArrayData[i][j]:<{4}}", end="") # Output value [row][column]
        print("\n") # Create new line (new row)
    print("\n")

print("Values before sorting")
printArrayData()

#2(b)(i)
ArrayLength = 10

for X in range(ArrayLength):
    for Y in range(ArrayLength-1):
        for Z in range(ArrayLength-Y-1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

print("Values after sorting")
printArrayData()

def BinarySearch(SearchArray, Lower, Upper, SearchValue) -> int:
    global ArrayData
    if Upper > Lower:
        Mid = (Lower + (Upper -1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, 0, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    
    return -1

number = ArrayData[0][9]

print("Finding number", number)
print(BinarySearch(ArrayData, 0, 10, number))

print("Finding number", 102)
print(BinarySearch(ArrayData, 0, 10, 102))
