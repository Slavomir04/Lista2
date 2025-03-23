
def getZdaniaPodrzedne(input:str,mincount=1)->str:
    """Funkcja wyszukująca pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne (na
podstawie przecinków)."""
    counter = 0
    current = ''
    for char in input:
        current = current + char
        if char == '\n':
            if counter >= mincount:
                return current
            current = ''
            counter = 0
        elif char == ',':
            counter += 1
    if counter >= mincount:
        return current
    return ""

#print(getZdaniaPodrzedne("zdanie nie podrzedne\nzdanie,Podrzedne,jest1\nzdanie,Podrzedne,jest2"))