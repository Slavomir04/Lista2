import tools
def nonWhiteCharCount(input:str)->str:
    """Funkcja zliczająca wszystkie znaki w tekście, z pominięciem białych znaków."""
    counter = 0
    previous_char = ''
    for char in input:
        if tools.isItEnd(previous_char, char):
            continue
        elif char.isalpha():
            counter+=1
        previous_char = char
    return counter

#print(nonWhiteCharCount('abc    de f asd.asd bccvb asad'))