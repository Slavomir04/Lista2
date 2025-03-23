import tools
def getZdaniaPodrzedne(input:str,mincount=1)->str:
    """Funkcja wyszukująca pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne (na
podstawie przecinków)."""
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

#print(getZdaniaPodrzedne("zdanie nie podrzedne. zdanie,Podrzedne,jest1. zdanie,Podrzedne,jest2."))