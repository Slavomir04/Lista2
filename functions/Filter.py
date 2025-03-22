from markdown_it.common.utils import isValidEntityCode

import Reduce

def getZdaniaPodrzedne(array,mincount=4):
    result = []
    for sentence in array:
        s = Reduce.splitFromChars(sentence,ignore=Reduce.nonWhiteValues())
        if len(s)>=mincount:
            result.append(s)
    return result



def getAskYellSentence(array:list[str])->list[str]:
    result = []
    for sentence in array:
        if sentence.endswith('?'):
            result.append(sentence)
        elif sentence.endswith('!'):
            result.append(sentence)
    return result

def getContainsWords(array:list[str],words:list[str]=['i', 'oraz', 'ale', 'że' ,'lub'],mincontains=2)->list[str]:
    """j. Funkcja wypisująca tylko zdania, które zawierają co najmniej dwa wyrazy z następujących:
„i”, „oraz”, „ale”, „że”, „lub”."""
    result = []
    for sentece in array:
        split = Reduce.splitFromChars(sentece,ignore=Reduce.nonWhiteValues())
        c = mincontains
        for word in split:
            if words.__contains__(word):
                c-=1
            if c<=0:
                result.append(sentece)
                break
    return result





"""k. Funkcja, która wypisuje na wyjściu tylko zdania w czwartym kwartylu pod względem
długości zdania (kryterium – liczba znaków).
l. Funkcja wypisująca tylko te zdania, których wyrazy są w porządku leksykograficznym."""



def getKwartyl(array:list[str])->list[str]:
    max_len = len(max(array,key=lambda x: len(x)))
    result = []
    for sentence in array:
        print(max_len,len(sentence))
        if len(sentence)<=max_len//4:
            result.append(sentence)
    return result

def getIfSorted(array:list[str])->list[str]:
    result = []
    for sentence in array:
        isValid = True
        split = Reduce.splitFromChars(sentence,ignore=Reduce.nonWhiteValues())
        for i in range(1, len(split)):
            if split[i] < split[i - 1]:
                isValid = False
                break
        if isValid:
            result.append(sentence)
    return result


print(getIfSorted(["a"]))