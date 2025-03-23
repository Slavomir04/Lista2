def isWhiteChar(char):
    return char in (' ', '\t', '\n', '\r', '\v', '\f')
def isSpecialChar(char:str):
    char.isalpha()

def isItEnd(previousChar:str, currentChar:str)->bool:
    return ['.','?','!'].__contains__(currentChar) or (previousChar == currentChar and previousChar =='\n')

def checkText(arg):
    if (isinstance(arg, str)):
        return True
    else: raise TypeError("Your type is not string")

def checkIsEmpty(arg:str):
    if (len(arg) == 0):
        raise ValueError("String can't be empty")