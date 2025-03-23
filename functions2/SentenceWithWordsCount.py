import tools


def getSentenceWithWordsCount(input:str,sep=' ',min=4)->str:
    result = ""
    current_sentence = ""
    count = 0
    word = ''
    for char in input:
        current_sentence += char
        if tools.isWhiteChar(char):
            word = word + char
        else:
            if(len(word)>0):
                 count +=1
                 word = ''
            if char == '\n':
                if (len(current_sentence) > 0 and count >= min):
                    result += current_sentence + sep
                current_sentence = ""
                count = 0
                word = ''
    if (len(current_sentence) > 0 and count >= min):
        result += current_sentence + sep
    return result


print(getSentenceWithWordsCount('Hello World dupa dupa\nkurwa mac\nchuj ci, w pysk jebany debilu'))

    #"""Funkcja wypisująca tylko zdania zawierające co najwyżej 4 wyrazy."""
