
def nonWhiteCharCount(input:str)->str:
    """Funkcja zliczająca wszystkie znaki w tekście, z pominięciem białych znaków."""
    counter = 0
    for char in input:
        if char=='\n' or char==' ':
            continue
        elif not char.isalpha():
            counter+=1
    return counter

#print(nonWhiteCharCount('ab[,cd.. .\n..'))