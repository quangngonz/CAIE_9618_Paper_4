
class Character:
    def __init__(self, pName, pXPos, pYPos):
        self.Name = pName       # Chracter Name: STRING
        self.XPosition = pXPos  # Chracter X-Position: INTEGER
        self.YPosition = pYPos  # Chracter Y-Position: INTEGER

    def GetXPosition(self):
        return self.XPosition
    
    def GetYPosition(self):
        return self.YPosition
    
    def SetXPosition(self, pXPos):
        if self.XPosition + pXPos > 10000:
            self.XPosition = 10000
        elif self.XPosition + pXPos < 0:
            self.XPosition = 0
        else:
            self.XPosition = self.XPosition + pXPos

    def SetYPosition(self, pYPos):
        if self.YPosition + pYPos > 10000:
            self.YPosition = 10000
        elif self.YPosition + pYPos < 0:
            self.YPosition = 0
        else:
            self.YPosition = self.YPosition + pYPos
    
    def Move(self, direction):
        if direction == 'up':
            self.SetYPosition(10)
        elif direction == 'down':
            self.SetYPosition(-10)
        elif direction == 'left':
            self.SetXPosition(-10)
        elif direction == 'right':
            self.SetXPosition(10)

class BikeCharacter(Character):
    def __init__(self, pName, pXPos, pYPos):
        super().__init__(pName, pXPos, pYPos)
    
    def Move(self, direction):
        if direction == 'up':
            self.SetYPosition(20)
        elif direction == 'down':
            self.SetYPosition(-20)
        elif direction == 'left':
            self.SetXPosition(-20)
        elif direction == 'right':
            self.SetXPosition(20)

Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)

TargetCharacter = str(input("Target Character: "))

while TargetCharacter != "jack" and TargetCharacter != "karla":
        print("Invalid Character")
        TargetCharacter = str(input("Target Character: "))

TargetDirection = str(input("Target Dircection: "))

while TargetDirection != 'up' and TargetDirection != 'down' and TargetDirection != 'left' and TargetDirection != 'right':
    print("Invalid Direction")
    TargetDirection = str(input("Target Dircection: "))

if TargetCharacter == 'jack':
    Jack.Move(TargetDirection)
    print("Jack's new poisition is X = " + str(Jack.GetXPosition()) + " Y = " + str(Jack.GetYPosition()))
elif TargetCharacter == "karla":
    Karla.Move(TargetDirection)
    print("Karla's new poisition is X = " + str(Karla.GetXPosition()) + " Y = " + str(Karla.GetYPosition()))
    

