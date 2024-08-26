
global Animal, Colour, AnimalTopPointer, ColourTopPointer
Animal = [] # Array of 20 elements Strings
Colour = [] # Array of 10 elements Strings

AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(dataToPush: str) -> bool:
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(dataToPush)
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal() -> str:
    global AnimalTopPointer
    returnData = ""

    if AnimalTopPointer == 0:
        return ""
    else:
        returnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return returnData

def PushColour(dataToPush: str) -> bool:
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour.append(dataToPush)
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour() -> str:
    global ColourTopPointer
    returnData = ""

    if ColourTopPointer == 0:
        return ""
    else:
        returnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return returnData

def ReadData():
    global AnimalTopPointer, ColourTopPointer

    try:
        file = open("AnimalData.txt", 'r')
        for line in file:
            PushAnimal(line.strip('\n'))
        file.close()
    except IOError:
        print("File does not exist")
    
    try:
        file = open("ColourData.txt")
        for line in file:
            PushColour(line.strip('\n'))
        file.close()
    except IOError:
        print("File does not exist")

def OutputItem():
    next_animal = PopAnimal()
    next_colour = PopColour()

    if next_colour == "":
        next_colour = "No colour"
        PushAnimal(next_animal)
    else:
        if next_animal == "":
            next_animal = "No animal"
            PushColour(next_colour)
        else:
            print(next_colour, next_animal)

ReadData()

OutputItem()
OutputItem()
OutputItem()
OutputItem()

