import tools
import sys
import io



def findMax(s:str)->int:
    max_out = 0
    count = 0
    previous_char = ''
    for char in s:
        if tools.isItEnd(previous_char, char):
            count = 0
        else:
            count += 1
        if max_out<count:
            max_out = count
        previous_char = char
    return max_out



def getKwartyl(input:str)->str:
    """Funkcja, która wypisuje na wyjściu tylko zdania w czwartym kwartylu pod względem
długości zdania (kryterium – liczba znaków)."""
    tools.checkText(input)
    tools.checkIsEmpty(input)

    max_len = findMax(input)
    quart_len = int(max_len//4) +(1 if max_len % 4 != 0 else 0)
    result = ''
    current = ''
    previous_char = ''
    for char in input:
        current = current + char
        if tools.isItEnd(previous_char, char):
            if len(current) - (1 if previous_char == '\n' and char == '\n' else 0) <= quart_len + 1:
                result = result + current
            current = ''
        previous_char = char
    if len(current) <= quart_len+1:
        result = result + current
    return result


if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


    book = sys.stdin.read()

    print(getKwartyl(book))




