import tools

def longestSentence_non_sam_char(input:str)->str:
    """Funkcja wyszukująca najdłuższe zdanie, w którym żadne dwa sąsiadujące słowa niezaczynają się na tę samą literę"""
    current = ''
    last_word = ''
    word = ''
    max = ''
    isGood = True
    for char in input:
        current +=char

        if char == '\n':
            if len(word)>0 and word[0]==last_word[0]:
                isGood = False
            if isGood and len(max)<len(current):
                max = current
            current = ''
            last_word = ''
            word = ''
            isGood = True
        elif not tools.isWhiteChar(char):
            if len(word)>0:
                if len(last_word)>0 and word[0]==last_word[0]:
                    isGood = False
                last_word = word
            word = ''
        else:
            word += char
    if len(word) > 0 and len(last_word)>0 and word[0] == last_word[0]:
        isGood = False
    if isGood and len(max) < len(current)+(1 if input[-1]!='\n' else 0):
        max = current

    return max

#print(longestSentence_non_sam_char("abc abd 131232121dojnazinasudsanodnasodna\na b c d e f g h j k l\n a b c 1231231232112321321321131231233"))