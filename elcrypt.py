#-------ELCRYPT-------
# Made by: ELChris414
# Version: 0.0.1
from sys import *

import math

def combineCharacters(character1, character2):
    result = character1 + character2
    if (result > 94):
        result -= 94
    return result

def hash(input, desiredLength):
    desiredLength = int(desiredLength)
    result = []
    finalResult = ""
    allowedCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_`~,.<>/?\|[]{}=+;: \"\'") # 95 characters
    acceptedCharacters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_`~,.<>/?\|[]{}=+;:\"\'") # 94 characters
    characters = list(input)
    length = len(input)
    for char in characters:
        if char not in allowedCharacters:
            return "errored"
    current = 0
    for x in range(0, desiredLength):
        char = input[current]
        result.insert(x,acceptedCharacters.index(char) + 1)
        current += 1
        if current == len(input):
            current = 0
        if x == (desiredLength - 1) and current != 0:
            x = -1
            while current != len(input):
                x += 1
                result.insert(x, combineCharacters(result[x], acceptedCharacters.index(characters[current]) + 1))
                current += 1
                if x == (desiredLength - 1):
                    x = 0
    for x in range(0, desiredLength):
        if (len(result) < x+2 or len(result) < x+3):
            num = result[x]
        else:
            num = math.floor((result[x] + result[x+1] + result[x+2] + 3) / 3)
        result.insert(x, combineCharacters(result[x], num))
        result.insert(x + 1, combineCharacters(result[x + 1], num))
        result.insert(x + 2, combineCharacters(result[x + 2], num))
        x += 2
    for x in range(0, desiredLength):
        finalResult += acceptedCharacters[int(result[x]) - 1]
    return finalResult

print(hash(argv[1],argv[2]))
