
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)

    for x in range(0, LengthString):
        FirstCharacter = Value[0:1]

        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1

        Value = Value[1: len(Value)]

    return Total

def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    elif Value[0] == 'a' or Value[0] == 'e' or Value[0] == 'i' or Value[0] == 'o' or Value[0] == 'u':
        return 1 + RecursiveVowels(Value[1: len(Value)])
    else:
        return RecursiveVowels(Value[1: len(Value)])

print(RecursiveVowels("imagine"))


