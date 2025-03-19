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
    result = []
    for sentence in array:
        a = dict()
        for word in words:
            a.update({word: mincontains})
        splited = Reduce.splitFromChars(sentence,ignore=Reduce.nonWhiteValues())
        for word in splited:
            temp = a.get(word)
            if temp is not None:
                if temp>0:
                    a.update({word: temp-1})
        isValid = True
        for value in a.values():
            if value>0:
                isValid = False
                break
        if isValid:
            result.append(sentence)
    return result






print(getContainsWords([" i i i i i dupa","asdasdad"]))