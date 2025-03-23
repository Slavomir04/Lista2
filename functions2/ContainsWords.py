from debugpy.common.timestamp import current
import tools

def getContainsWords(input:str,mincontains=2,words:list[str]=['i', 'oraz', 'ale', 'że' ,'lub'])->str:
    """j. Funkcja wypisująca tylko zdania, które zawierają co najmniej dwa wyrazy z następujących:
„i”, „oraz”, „ale”, „że”, „lub”."""
    result = ''
    current = ''
    counter = 0
    word = ''
    for char in input:
        current = current + char
        if char == '\n':
            if counter >= mincontains:
                result += current
            current = ''
            word = ''
            counter = 0
        elif tools.isWhiteChar(char):
            word += char
        else:
            if word in words:
                counter += 1
            word = ''
    if word in words:
        counter += 1
    if counter >= mincontains:
        result += current
    return result


#print(getContainsWords("kurwa ma c oraz i ale lub\njprdl na chuj to tak\noraz i"))