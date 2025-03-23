
import tools

def isValid(word1,word2)->bool:
    if not word1.isalpha() or not word2.isalpha() :
        return True
    for c1,c2 in zip(word1,word2):
        if ord(c1)<ord(c2):
            return True
        elif ord(c1)>ord(c2):
            return False
    return len(word1)==len(word2)
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
            if last_word!='' and (not isValid(last_word,word)):
                isGood = False
            if len(word)>0:
                last_word = word
            word = ''
        else:
            word += char
        previous_char = char
    return result

print(getIfSorted('a b c 12. aa ab ac. b a c! ab a.'))

