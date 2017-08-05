#-------ELCRYPT-------
# Made by: ELChris414
# Version: 0.0.1
from sys import *

import math

def combineCharacters(character1, character2):
    result = character1 + character2
    if (result > 95):
        result -= 95
    return result

def hash(input, desiredLength):
    desiredLength = int(desiredLength)
    result = []
    finalResult = ""
    acceptedCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_`~,.<>/?\|[]{}=+;: \"\'") # 95 characters
    characters = list(input)
    length = len(input)
    for char in characters:
        if char not in acceptedCharacters:
            return "errored"
    current = 0
    for x in range(0, desiredLength):
        char = input[current]
        result.insert(x,acceptedCharacters.index(char) + 1)
        current += 1
        if current == len(input):
            current = 0
        if x == (desiredLength - 1) and current != 0:
            y = -1
            while current != len(input):
                y += 1
                result[y] = combineCharacters(result[y], acceptedCharacters.index(characters[current]) + 1)
                current += 1
                if y == (desiredLength - 1):
                    y = 0
    for x in range(0, desiredLength):
        if (len(result) < x+2):
            num = result[x]
            result[x] = combineCharacters(result[x], num)
        elif (len(result) < x+3):
            num = math.floor((result[x] + result[x+1] + 2) / 2)
            result[x] = combineCharacters(result[x], num)
            result[x + 1] = combineCharacters(result[x + 1], num)
        else:
            num = math.floor((result[x] + result[x+1] + result[x+2] + 3) / 3)
            result[x] = combineCharacters(result[x], num)
            result[x + 1] = combineCharacters(result[x + 1], num)
            result[x + 2] = combineCharacters(result[x + 2], num)
    for x in range(0, desiredLength):
        finalResult += acceptedCharacters[int(result[x]) - 1]
    return finalResult

if (len(argv) == 3):
    print(hash(argv[1],argv[2]))
