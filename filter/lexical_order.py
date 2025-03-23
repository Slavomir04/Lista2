import tools
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def isValid(word1,word2)->bool:
    if not word1.isalpha() or not word2.isalpha():
        return True
    for c1,c2 in zip(word1,word2):
        if ord(c1)<ord(c2):
            return True
        elif ord(c1)>ord(c2):
            return False
    return len(word1) == len(word2)


def getIfSorted(input:str)->str:
    """Funkcja wypisująca tylko te zdania, których wyrazy są w porządku leksykograficznym."""
    tools.checkText(input)
    tools.checkIsEmpty(input)


    result = ''
    current = ''
    last_word = ''
    word = ''
    isGood=True
    previous_char = ''
    for char in input:
        current +=char
        if tools.isItEnd(previous_char, char):#char == '\n':
            if last_word!='' and (not isValid(last_word,word)):
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

if __name__ == "__main__":
    book = sys.stdin.read()

    print(getIfSorted(book))

