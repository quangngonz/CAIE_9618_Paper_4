
def ReadData():
    try:
        # Open the file in read mode
        DataFile = open("Source files/Data.txt", "r") 
        
        # Local array consist of 45 items
        DataItems = [] 

        # Read the data from the file and store it in the array
        for i in range(45):
            DataItems.append(DataFile.readline().strip())

        DataFile.close() # Close the file

        return DataItems
    except IOError:
        print("Error reading from file")

# Function to format the array takes in an array of strings
def FormatArray(DataArray):
    OutputString = ""

    # Loop through the array
    for i in range(len(DataArray)):
        # Add the item to the output string with a space between each item
        OutputString = OutputString + DataArray[i] + " " 

    return OutputString

def CompareStrings(String1, String2):
    maxLen = len(String1) if len(String1) > len(String2) else len(String2)

    for i in range(maxLen):
        if ord(String1[i]) < ord(String2[i]):
            return 1
        elif ord(String1[i]) > ord(String2[i]):
            return 2
        else:
            continue

    return -1

def Bubble(DataArray):
    data = DataArray[:]
    n = len(data)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if CompareStrings(data[j], data[j + 1]) == 2:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

    return data

FileData = ReadData() # Read the data from the file
FormattedArray = FormatArray(FileData) # Print the formatted data

# print(FormattedArray) # Print the formatted data

SortedData = Bubble(FileData) # Sort the data
FormattedSortedData = FormatArray(SortedData) # Print the formatted data
print(FormattedSortedData) # Print the formatted data
