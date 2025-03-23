import tools
import sys
import io

def getContainsWords(input:str,mincontains=2,words:list[str]=['i', 'oraz', 'ale', 'że' ,'lub'])->str:
    """j. Funkcja wypisująca tylko zdania, które zawierają co najmniej dwa wyrazy z następujących:
„i”, „oraz”, „ale”, „że”, „lub”."""
    tools.checkText(input)
    tools.checkIsEmpty(input)

    result = ''
    current = ''
    counter = 0
    word = ''
    prev_char = ''
    for char in input:
        current = current + char
        if tools.isItEnd(prev_char, char):#char == '\n':
            if word in words:
                counter += 1
            if counter >= mincontains:
                result += current
            current = ''
            word = ''
            counter = 0
        elif char.isalpha():
            word += char
        else:
            if word in words:
                counter += 1
            word = ''
        prev_char = char
    return result


if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


    book = sys.stdin.read()
    print(getContainsWords(book))