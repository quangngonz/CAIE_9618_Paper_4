
#1(a)
StackData = [] # 1D Array of 10 integer elements
StackPointer = 0 

#1(b)
def PrintStack():
    global StackData, StackPointer

    print("Stack values: ", end="")
    for i in range(StackPointer): # Loop over the Stack
        print(StackData[i], end=" ") # Print value
    
    print("\nPointer Value:", StackPointer) # Print pointer value

#1(c)
def PushToStack(value):
    global StackData, StackPointer
    if StackPointer == 10: # Check if stack is full
        return False
    else:
        StackData.append(value) # Push the value to the stack
        StackPointer += 1 # Move the pointer to the next free space
        return True

#1(d)(i)
for i in range(11): # run 11 times
    InputValue = int(input("Enter the number to push to stack: "))

    PushResponse = PushToStack(InputValue)

    if PushResponse == True: # Check if value is pushed to stack 
        print("Successfully pushed value", InputValue, "to Stack") # Output sucessful message
    else:
        print("Stack is full, cannot push value", InputValue, "to stack") # Output failed message
    
PrintStack()

#1(e)(i)
def Pop():
    global StackData, StackPointer

    if StackPointer == 0: # Check if stack is empty
        return -1
    
    TopValue = StackData[StackPointer-1] # Get the top value
    StackData.pop() # Remove the value from list
    StackPointer = StackPointer - 1 # Move the pointer to the previous free space
    return TopValue

#1(e)(ii)
# Remove two elements
TopValue = Pop()
print("removed", TopValue)
TopValue = Pop()
print("removed", TopValue)

PrintStack() # Print updated stack

