

def isWhiteChar(char):
    return char in (' ', '\t', '\n', '\r', '\v', '\f')
def isSpecialChar(char:str):
    char.isalpha()

def isItEnd(previousChar:str, currentChar:str)->bool:
    return ['.','?','!'].__contains__(currentChar) or (previousChar == currentChar and previousChar =='\n')