import tools
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def getFirstSentences(input:str,number:int=20)->str:
    tools.checkText(input)
    tools.checkIsEmpty(input)

    result = ''
    previous_char = ''
    for char in input:
        if number<=0:
            break
        else:
            result = result + char
            if tools.isItEnd(previous_char, char):
                number-=1
        previous_char = char
    return result

if __name__ == "__main__":
    book = sys.stdin.read()

    print(getFirstSentences(book))
