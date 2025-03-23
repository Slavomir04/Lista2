from debugpy.common.timestamp import current
import tools

def getContainsWords(input:str,mincontains=2,words:list[str]=['i', 'oraz', 'ale', 'że' ,'lub'])->str:
    """j. Funkcja wypisująca tylko zdania, które zawierają co najmniej dwa wyrazy z następujących:
„i”, „oraz”, „ale”, „że”, „lub”."""
    result = ''
    current = ''
    counter = 0
    word = ''
    prev_char = ''
    for char in input:
        current = current + char
        if tools.isItEnd(prev_char,char):#char == '\n':
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


#print(getContainsWords("zdanie i oraz koniec. zdanie bez niczego! zdanie z ale że."))