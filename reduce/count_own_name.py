import set_encoding
import sys
from checkTypes import checkText

def countSentences(title:str)->int:
    checkText(title)

    counter = 0
    separators = ["?", ".", "!"]
    for i in range(0, len(title), 1):
        if (title[i] in separators):
            counter+=1
    return counter

def countOwnNamePercent(title:str)->float:
    checkText(title)

    counter = 0
    isOwnNameFinded = False
    separators_combination = ["— ", "\n\n", "! ", ". ", "? "]
    separators = ["?", ".", "!"]
    for i in range(2, len(title), 1):
        if (title[i].isupper() and title[i-2:i] not in separators_combination and title[i-1] == " "):
            isOwnNameFinded = True
        elif (title[i] in separators and isOwnNameFinded):
            counter+=1
            isOwnNameFinded = False

    return counter / countSentences(title) * 100

if __name__ == "__main__":
    name = sys.stdin.read()

    print(countOwnNamePercent(1))