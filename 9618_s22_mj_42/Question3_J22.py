
class Card:
    # private __number: INTEGER number of the card
    # private __colour: STRING colour of the card
    def __init__(self, number, colour):
        self.__number = number # Create a private attribute to store number
        self.__colour = colour # Create a private attribute to store colour

    def GetNumber(self):
        return self.__number

    def GetColour(self):
        return self.__colour

    # def __str__(self) -> str:
    #     return f"Card {self.__number}-{self.__colour}"
    
    # def __repr__(self) -> str:
    #     return f"{self.__number}-{self.__colour}"

#3(c)
CardArray = [] # Array of 30 elements with datatype Card

CardValuesFile = open('CardValues.txt', 'r') # Open CardValues.txt
CardValuesFileData = CardValuesFile.read().split("\n") # Read the data line by line
NumberOfLines = 60
CardValuesFile.close() # Close the file

for line in range(0, NumberOfLines, 2): # Loop through 2 lines at a time
    CardNumber = int(CardValuesFileData[line]) # Get card number
    CardColour = CardValuesFileData[line+1] # Get card colour

    CardArray.append(Card(CardNumber, CardColour)) # Add the Card to the array

#3(d)
ChosenCards = [] # Array of INTEGER to store chosen cards

def ChooseCard():
    global ChosenCards
    CardAvailible = False

    while CardAvailible == False:
        CardChoice = int(input("Select the card index you want: "))
        if CardChoice >= 1 and CardChoice <= 30: # Check if valid index
            if CardChoice not in ChosenCards: # Check if card is already chosen
                CardAvailible = True # Set valid varible to True
                ChosenCards.append(CardChoice) # Add choice to chosen cards
            else:
                print("Card already chosen, please choose again") # Display message asking user to choose again
        else:
            print("Not valid index, please choose from 1 to 30 (inclusive)") # Display message asking user to choose again
    
    return CardChoice # return index of chosen card
        

#3(e)(i)
Player1 = [] # Array for player 1 chosen cards of type Card

for i in range(4):
    Player1CardChoice = ChooseCard() # Ask player to choose card
    Player1.append(CardArray[Player1CardChoice-1]) # Add the chosen card to Player1's array minus 1 because index starts at 0

print("Player 1 chosen cards:")
for i in range(4): # Loop over Player1 chosen cards
    P1Card = Player1[i] 
    P1CardNumber = P1Card.GetNumber() # Get card number
    P1CardColour = P1Card.GetColour() # Get card colour
    print("Card:", P1CardNumber, "-", P1CardColour) # Output card number and colour
    # print("Card:", f"{P1CardNumber:>3}", "-", P1CardColour) # Output card number and colour

# print(CardArray)
# print(Player1)
# print(ChosenCards)
