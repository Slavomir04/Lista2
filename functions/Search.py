


def longestSentence(array:list[str])->str:
    return max(array,key= lambda x: len(x))


def longestSentence2(array:list[str])->str:
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

def zdaniePodrzedne(array):
    for sentence in array:
        s = sentence.split(',')
        if len(s)>1:
            return sentence
    return ""
