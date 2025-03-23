

def paragraphCounter(input:str)->str:
    """Funkcja zliczająca akapity w tekście (akapit jest oddzielony pustą linią)."""
    counter = 0
    previous_char = ''
    for char in input:
        if previous_char == char and char == '\n':
            counter += 1
        previous_char = char
    return counter

#print(paragraphCounter('dupa\n\nchujci\nw\ndupe'))