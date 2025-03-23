
def findMax(s:str)->int:
    max_out = 0
    count = 0
    for char in s:
        if char == '\n':
            count = 0
        else:
            count += 1
        if max_out<count:
            max_out = count
    return max_out



def getKwartyl(input:str)->str:
    """Funkcja, która wypisuje na wyjściu tylko zdania w czwartym kwartylu pod względem
długości zdania (kryterium – liczba znaków)."""

    max_len = findMax(input)
    quart_len = int(max_len//4) +(1 if max_len % 4 != 0 else 0)
    result = ''
    current = ''
    for char in input:
        current = current + char
        if char == '\n':
            if len(current) <= quart_len+1:
                result = result + current
            current = ''
    if len(current) <= quart_len+1:
        result = result + current
    return result


#print(getKwartyl('123456789\n123\n123456\n1'))




