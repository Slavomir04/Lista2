


def longestSentence(array:list[str])->str:
    return max(array,key= lambda x: len(x))

def __test(x):
    x = x.split(' ')
    last = x[0]
    for i in (1,len(x)):
        if(last[0]==x[i][0]):
            return False
    return True
def longestSentence2(array:list[str])->str:
    """Funkcja wyszukująca najdłuższe zdanie, w którym żadne dwa sąsiadujące słowa niezaczynają się na tę samą literę"""
        return max(array,key= lambda x: if __test(x) len(x) else 0)

