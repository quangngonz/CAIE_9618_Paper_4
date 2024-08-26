
class Vehicle():
    # self.__ID                 String
    # self.__MaxSpeed           Integer
    # self.__CurrentSpeed       Integer
    # self.__IncreaseAmount     Integer
    # self.__HorizontalPosition Integer

    def __init__(self, id, maxSpeed, increaseAmount):
        self.__ID = id
        self.__MaxSpeed = maxSpeed
        self.__IncreaseAmount = increaseAmount

        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed
    
    def SetHorizontalPosition(self, position):
        self.__HorizontalPosition = position

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
    
    def OutputCurrentPosition(self):
        print("Current Position:", self.__HorizontalPosition)
        print("Current Speed:", self.__CurrentSpeed)

class Helicopter(Vehicle):
    # self.__VerticlePosition   Integer
    # self.__VerticleChange     Integer
    # self.__MaxHeight          Integer

    def __init__(self, id, maxSpeed, increaseAmount, verticleChange, maxHeight):
        super().__init__(id, maxSpeed, increaseAmount)
        self.__VerticlePosition = 0
        self.__VerticleChange = verticleChange
        self.__MaxHeight = maxHeight
    
    def IncreaseSpeed(self):
        self.__VerticlePosition = self.__VerticlePosition + self.__VerticleChange
        if self.__VerticlePosition > self.__MaxHeight:
            self.__VerticlePosition = self.__MaxHeight
        
        super().IncreaseSpeed()

    def OutputCurrentPosition(self):
        super().OutputCurrentPosition()
        print("Current verticle position:", self.__VerticlePosition)

car_1 = Vehicle("Tiger", 100, 20)
helicopter_1 = Helicopter("Lion", 350, 40, 3, 100)

car_1.IncreaseSpeed()
car_1.IncreaseSpeed()
car_1.OutputCurrentPosition()

print()

helicopter_1.IncreaseSpeed()
helicopter_1.IncreaseSpeed()
helicopter_1.OutputCurrentPosition()
