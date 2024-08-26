
# Question 1 | (a) | (i)
DataArray = [] # Array of 25 elements Interger

# Question 1 | (a) | (ii)
try:
    file = open("Data.txt", 'r') # Open file Data.txt
    data = file.read().split("\n") # Read data from the file in array of elements
    file.close() # Close file

    for num in data:
        DataArray.append(int(num)) # Converting each element to an integer
except IOError: # Raise error if Data.txt doesn't exist
    print("File not found") # Print and exception if file doesn't exist

# Question 1 | (b) | (i)
def PrintArray(interger_array):
    for number in interger_array: # Loop over each element
        print(number, end=" ")  # Print the element without \n at the end
    print()

# Question 1 | (b) | (ii)
PrintArray(DataArray)

# Question 1 | (b) | (iii)
# Take a screenshot

# Question 1 | (c) 
def LinearSearch(integer_array, search_value):
    count = 0

    for i in range(len(integer_array)):
        if integer_array[i] == search_value:
            count = count + 1
    
    return count

# Question 1 | (d) | (i)
user_value = int(input("Input a value between 0 and 100 inclusive to search: ")) # Ask user to input value

while user_value < 0 or user_value > 100: # Check if value is out of range
    print("Invalid value") # Print error 
    user_value = int(input("Input a value between 0 and 100 inclusive to search: ")) # Ask user to input value

search_result = LinearSearch(DataArray, user_value) # Call the LinearSearch Array with user values
print("The number", user_value, "is found", search_result, "times.") # Output the result

# Question 1 | (d) | (ii)
