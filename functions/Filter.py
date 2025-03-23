from markdown_it.common.utils import isValidEntityCode

import Reduce


def getSentenceWithWordsCount(array:list[str],mincount=4)->list[str]:
    """Funkcja wypisująca tylko zdania zawierające co najwyżej 4 wyrazy."""
    result = []
    for sentence in array:
        splited = Reduce.splitFromChars(sentence,Reduce.nonWhiteValues())
        if len(splited) >= mincount:
            result.append(sentence)
    return result

def getFirstSentences(array:list[str],number:int=20)->list[str]:
    """Funkcja wypisująca pierwszych 20 zdań"""
    return array[:number]

def getAskYellSentence(array:list[str])->list[str]:
    """Funkcja, która wypisuje na wyjściu tylko zdania, które są pytaniami lub wykrzyknieniami."""
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



def getKwartyl(array:list[str])->list[str]:
    """Funkcja, która wypisuje na wyjściu tylko zdania w czwartym kwartylu pod względem
długości zdania (kryterium – liczba znaków)."""
    max_len = len(max(array, key=lambda x: len(x)))
    quart_len = int(max_len // 4) + (1 if max_len % 4 != 0 else 0)
    result = []
    for sentence in array:
        if len(sentence) <= quart_len:
            result.append(sentence)
    return result

def getIfSorted(array:list[str])->list[str]:
    """Funkcja wypisująca tylko te zdania, których wyrazy są w porządku leksykograficznym."""
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


