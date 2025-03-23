


def longestSentence(array:list[str])->str:
    """Funkcja wypisująca najdłuższe zdanie w książce (kryterium – liczba znaków)."""
    return max(array,key= lambda x: len(x))


def longestSentence_non_same_char(array:list[str])->str:
    """Funkcja wyszukująca najdłuższe zdanie, w którym żadne dwa sąsiadujące słowa niezaczynają się na tę samą literę"""
    result = ""
    for sentence in array:
        s = sentence.split(' ')
        good = True
        for i in range(1,len(s)):
            if s[i][0]==s[i - 1][0]:
                good = False
                break
        if good and len(sentence)>len(result):
            result = sentence
    return result



def getZdaniaPodrzedne(array:[str],mincount=4):
    """Funkcja wyszukująca pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne (na
podstawie przecinków)."""
    result = []
    for sentence in array:
        c=0
        for char in sentence:
            if char == ',':
                c+=1
        if c>=mincount:
            result.append(sentence)
    return result