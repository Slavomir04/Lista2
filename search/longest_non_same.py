import tools

import sys
import io



def longestSentence_non_sam_char(input:str)->str:
    """Funkcja wyszukująca najdłuższe zdanie, w którym żadne dwa sąsiadujące słowa niezaczynają się na tę samą literę"""
    tools.checkText(input)
    tools.checkIsEmpty(input)

    current = ''
    last_word = ''
    word = ''
    max = ''
    isGood = True
    previous_char = ''
    for char in input:
        current +=char

        if tools.isItEnd(previous_char,char):
            if len(word) > 0 and len(last_word)>0 and word[0]==last_word[0]:
                isGood = False
            if isGood and len(max)<len(current):
                max = current
            current = ''
            last_word = ''
            word = ''
            isGood = True
        elif not char.isalpha():#not tools.isWhiteChar(char):
            if len(word)>0:
                if len(word) > 0 and len(last_word)>0 and word[0]==last_word[0]:
                    isGood = False
                last_word = word
            word = ''
        else:
            word += char
        previous_char = char
    if len(word) > 0 and len(last_word)>0 and word[0] == last_word[0]:
        isGood = False
    if isGood and len(max) < len(current)+(1 if input[-1]!='\n' else 0):
        max = current

    return max

if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


    book = sys.stdin.read()

    print(longestSentence_non_sam_char(book))