
class Horse:
    
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name # Private attribute
        self.__MaxFenceHeight = MaxFenceHeight # Private attribute
        self.__PercentageSuccess = PercentageSuccess # Private attribute

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self, FenceHeight, RiskModifier):
        if FenceHeight > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        else:
            if RiskModifier == 1:
                return self.__PercentageSuccess * 1
            elif RiskModifier == 2:
                return self.__PercentageSuccess * 0.9
            elif RiskModifier == 3:
                return self.__PercentageSuccess * 0.8
            elif RiskModifier == 4:
                return self.__PercentageSuccess * 0.7
            elif RiskModifier == 5:
                return self.__PercentageSuccess * 0.6
            else:
                return 0 # Invalid risk modifier
    
Horses = [] # Array of 2 horses object
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))

# Output the name of both horses from the array
print(Horses[0].GetName())
print(Horses[1].GetName())

class Fence:

    def __init__(self, Height, Risk):
        # Private attribute integer between 70 and 180 
        self.__Height = Height 
        # Private attribute integer between 1 and 5 
        self.__Risk = Risk

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

Courses = [] # Array of 4 fence object

for i in range(4):
    valid_input = False

    while not valid_input:
        # Read the height and risk of the fence
        height = int(input("Enter the height of the fence: ")) 
        risk = int(input("Enter the risk of the fence: "))

        if height < 70 or height > 180 or risk < 1 or risk > 5:
            print("Invalid input. Please enter a height between 70 and 180 and a risk between 1 and 5.")
        else:
            Courses.append(Fence(height, risk))
            print("Fence added. \n")
            valid_input = True
        
average_success = [] # Array of average success rate for each horse

for i in range(2):
    total_success = 0
    for j in range(4):
        print("The horse " + Horses[i].GetName() + " at fence " + str(j + 1) + " has a " + str(Horses[i].Success(Courses[j].GetHeight(), Courses[j].GetRisk())) + "% chance of success.")
        total_success += Horses[i].Success(Courses[j].GetHeight(), Courses[j].GetRisk())
    
    print("The horse " + Horses[i].GetName() + " has an average " + str(total_success/4) + "%. chance of jumping over all four fences. \n")

    average_success.append(total_success/4)

if average_success[0] > average_success[1]:
    print("The horse " + Horses[0].GetName() + " has the highest average chance of success ")
elif average_success[0] < average_success[1]:
    print("The horse " + Horses[1].GetName() + " has the highest average chance of success ")
