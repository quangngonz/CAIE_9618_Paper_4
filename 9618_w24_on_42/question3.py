
HighScores = [] # ARRAY [0:10] OF ARRAY [STRING, INTEGER, INTEGER]

for i in range(7):
    emptyScore = ["", "", ""]
    HighScores.append(emptyScore)

def ReadData():
    scoreData = []

    try:
        file = open('HighScoreTable.txt', 'r')

        for i in range(7):
            playerID = file.readline().strip()
            gameLevel = int(file.readline().strip())
            score = int(file.readline().strip())

            scoreData.append([playerID, gameLevel, score])

        file.close()

        return scoreData
    except IOError:
        print("File not found")

def OutputHighScores(scores):
    for i in range(len(scores)):
        print(str(scores[i][0])+ " reached level " + str(scores[i][1]) + " with a score of " + str(scores[i][2]))

def SortScores(scores):
    sortedScores = scores

    swapped = True

    while swapped == True:
        swapped = False

        for i in range(len(sortedScores) - 1):
            temp1 = sortedScores[i]

            if sortedScores[i][1] < sortedScores[i+1][1]:
                sortedScores[i] = sortedScores[i+1]
                sortedScores[i+1] = temp1
                swapped = True
            elif sortedScores[i][1] == sortedScores[i+1][1]:
                if sortedScores[i][2] < sortedScores[i+1][2]:
                    sortedScores[i] = sortedScores[i+1]
                    sortedScores[i+1] = temp1
                    swapped = True
    
    return sortedScores

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)

