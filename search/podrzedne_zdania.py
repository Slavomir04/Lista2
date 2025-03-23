import tools
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def getZdaniaPodrzedne(input:str,mincount=1)->str:
    """Funkcja wyszukująca pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne (na
podstawie przecinków)."""
    tools.checkText(input)
    tools.checkIsEmpty(input)


    counter = 0
    current = ''
    previous_char = ''
    for char in input:
        current = current + char
        if tools.isItEnd(previous_char,char):#char == '\n':
            if counter >= mincount:
                return current
            current = ''
            counter = 0
        elif char == ',':
            counter += 1
        previous_char = char
    if counter >= mincount:
        return current
    return ""

if __name__ == "__main__":
    book = sys.stdin.read()

    print(getZdaniaPodrzedne(book))