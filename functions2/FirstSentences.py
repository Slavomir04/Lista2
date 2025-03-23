
import tools



def getFirstSentences(input:str,number:int=20)->str:
    result = ''
    previous_char = ''
    for char in input:
        if number<=0:
            break
        else:
            result = result + char
            if tools.isItEnd(previous_char,char):
                number-=1
        previous_char = char
    return result



##print(getFirstSentences('1.2.3.4.5.6.7.8.10',10))