
import tools

def isValid(word1,word2)->bool:
    for c1,c2 in zip(word1,word2):
        if ord(c1)<ord(c2):
            return True
        elif ord(c1)>ord(c2):
            return False
    return True
def getIfSorted(input:str)->str:
    """Funkcja wypisująca tylko te zdania, których wyrazy są w porządku leksykograficznym."""
    result = ''
    current = ''
    last_word = ''
    word = ''
    isGood=True
    previous_char = ''
    for char in input:
        current +=char
        if tools.isItEnd(previous_char,char):#char == '\n':
            if not isValid(last_word,word):
                isGood = False
            if isGood:
                result += current
            current = ''
            last_word = ''
            word = ''
            isGood = True
        elif not char.isalpha():#tools.isWhiteChar(char):
            if not isValid(last_word,word):
                isGood = False
            if len(word)>0:
                last_word = word
            word = ''
        else:
            word += char
        previous_char = char
    return result

#print(getIfSorted('a b c.ba bb. cb cd'))

