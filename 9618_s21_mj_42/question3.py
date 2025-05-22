

class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question    # Stores the question
        self.__answer = answer        # Stores the answer
        self.__points = points        # Points availible

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, userAnswer):
        if int(userAnswer) == int(self.__answer):
            return True
        else:
            return False
    
    def getPoints(self, numberAttempts):
        if numberAttempts == 1:
            return int(self.__points)
        elif numberAttempts == 2:
            return int(self.__points) // 2
        elif numberAttempts == 3:
            return int(self.__points) // 4
        else:
            return 0
        

arrayTreasure : list[TreasureChest] = [] # Array [0:4] OF TreasureChest

def readData():
    filename = "TreasureChestData.txt"

    try:
        file = open(filename, 'r')

        dataFetched = file.readline().strip()

        while dataFetched != "":
            question = dataFetched
            answer = file.readline().strip()
            points = file.readline().strip()

            newTreasure = TreasureChest(question, answer, points)
            arrayTreasure.append(newTreasure)

            dataFetched = file.readline().strip()
    
    except IOError:
        print("File not found")


readData()

questionNumber = int(input("Enter question number [1-5]: "))

if questionNumber > 0 and questionNumber < 6:

    print(arrayTreasure[questionNumber - 1].getQuestion())

    attemps = 0
    returnedValue = False

    while returnedValue == False:
        answerInput = int(input("Answer: "))
        returnedValue = arrayTreasure[questionNumber - 1].checkAnswer(answerInput)
        
        attemps = attemps + 1

    pointsAwarded = arrayTreasure[questionNumber - 1].getPoints(attemps)

    print("Points awarded: " + str(pointsAwarded))

