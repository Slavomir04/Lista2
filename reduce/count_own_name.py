import tools
import sys
import io



def countSentences(title:str)->int:
    tools.checkText(title)
    tools.checkIsEmpty(title)

    counter = 0
    separators = ["?", ".", "!"]
    for i in range(0, len(title), 1):
        if (title[i] in separators):
            counter+=1
    return counter

def countOwnNamePercent(title:str)->float:
    tools.checkText(title)
    tools.checkIsEmpty(title)

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
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    book = sys.stdin.read()

    print(countOwnNamePercent(book))