

def paragraphCounter(input:str)->str:
    """Funkcja zliczająca akapity w tekście (akapit jest oddzielony pustą linią)."""
    counter = 0
    previous_char = ''
    for char in input:
        if previous_char == char and char == '\n':
            counter += 1
        previous_char = char
    if previous_char == '\n':
        counter = max(0, counter - 1)
    return counter

#print(paragraphCounter('dupa\n\nchujci\nw\ndupe'))