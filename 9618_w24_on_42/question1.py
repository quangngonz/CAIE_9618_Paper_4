
class EventItem:
    def __init__(self, EventName, Type, Difficulty):
        self.__EventName = EventName    # Name of Event
        self.__Type = Type              # Type of Event [jump, swim, run, drive]
        self.__Difficulty = Difficulty  # Difficulty of Event [1 .. 5]

    
    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__Type

Group : list[EventItem] = [] # ARRAY [0:5] OF EventItem

Group.append(EventItem('Bridge', 'jump', 3))
Group.append(EventItem('Water wade', 'swim', 4))
Group.append(EventItem('100 mile run', 'run', 5))
Group.append(EventItem('Gridlock', 'drive', 2))
Group.append(EventItem('Wall on wall', 'jump', 4))

class Character:
    def __init__(self, Name, Jump, Swim, Run, Drive):
        self.__Name = Name      # Character Name
        self.__Jump = Jump      # Skill level at Event type of Jump
        self.__Swim = Swim      # Skill level at Event type of Swim
        self.__Run = Run        # Skill level at Event type of Run
        self.__Drive = Drive    # Skill level at Event type of Drive

    def GetName(self):
        return self.__Name
    
    def CalculateScore(self, typeOfEvent, eventDifficulty):
        CharacterSkill = -1     # Declare character skill varible

        # Get Character Skill level
        if typeOfEvent == 'jump':
            CharacterSkill = self.__Jump
        elif typeOfEvent == 'swim':
            CharacterSkill = self.__Swim
        elif typeOfEvent == 'run':
            CharacterSkill = self.__Run
        elif typeOfEvent == 'drive':
            CharacterSkill = self.__Drive
        
        # Calculate the score
        if CharacterSkill >= eventDifficulty:
            return 100
        else:
            difference = eventDifficulty - CharacterSkill

            if difference == 1:
                return 80
            if difference == 2:
                return 60
            if difference == 3:
                return 40
            if difference == 4:
                return 20
            else:
                return 0



TarzCharacter = Character('Tarz', 5, 3, 5, 1)
GeniCharacter = Character('Geni', 2, 2, 3, 4)

TarzScore = 0
GeniScore = 0

for i in range(5):
    eventType = Group[i].GetEventType()
    eventDifficulty = Group[i].GetDifficulty()

    TarzChance = TarzCharacter.CalculateScore(eventType, eventDifficulty)
    GeniChance = GeniCharacter.CalculateScore(eventType, eventDifficulty)
    
    if TarzChance > GeniChance: # type: ignore
        print("Tarz won event number " + str(i+1))
        TarzScore = TarzScore + 1
    elif GeniChance > TarzChance: # type: ignore
        print("Geni won event number " + str(i+1))
        GeniScore = GeniScore + 1
    else:
        print("Event number " + str(i+1) + " is a draw")
    
if TarzScore > GeniScore:
    print("Tarz has the most points in the Group")
elif GeniScore > TarzScore:
    print("Geni has the most points in the Group")
else:
    print("Group is a draw")
