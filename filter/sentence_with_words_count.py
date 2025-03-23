import tools
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def getSentenceWithWordsCount(input:str,sep=' ',min=4)->str:
    """Funkcja wypisująca tylko zdania zawierające co najwyżej 4 wyrazy."""
    tools.checkText(input)
    tools.checkIsEmpty(input)


    result = ""
    current_sentence = ""
    count = 0
    word = ''
    previous_char = ''
    for char in input:
        current_sentence += char
        if char.isalpha():#tools.isWhiteChar(char):
            word = word + char
        else:
            if(len(word)>0):
                 count +=1
                 word = ''
            if tools.isItEnd(previous_char, char):#char == '\n':
                if (len(current_sentence) > 0 and count >= min):
                    result += current_sentence + sep
                current_sentence = ""
                count = 0
                word = ''
        previous_char = char
    return result


if __name__ == "__main__":
    book = sys.stdin.read()

    print(getSentenceWithWordsCount(book))


