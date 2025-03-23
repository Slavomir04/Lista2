import tools
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def getAskYellSentence(input:str)->str:
    """Funkcja, która wypisuje na wyjściu tylko zdania, które są pytaniami lub wykrzyknieniami."""
    tools.checkText(input)
    tools.checkIsEmpty(input)
    result = ""
    prev_char = ''
    current = ''

    for char in input:
        current = current + char
        if tools.isItEnd(prev_char, char):
            if char == '!' or char == '?':
                result = result + current
            current = ""
        prev_char = char
    if len(current)>1 and (current[-1]=='!' or current[-1]=='?'):
        result = result + current
    return result

if __name__ == "__main__":
    book = sys.stdin.read()

    print(getAskYellSentence(book))