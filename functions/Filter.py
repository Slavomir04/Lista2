import Reduce

def filterWordsCount(array,mincount=4):
    result = []
    for sentence in array:
        s = Reduce.splitFromChars(sentence,ignore=Reduce.nonWhiteValues())
        if len(s)>=mincount:
            result.append(s)
    return result


test = ['asdad asdadsa asdada asdada']
print(filterWordsCount(test))