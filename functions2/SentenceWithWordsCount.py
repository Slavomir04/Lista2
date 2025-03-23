import tools


def getSentenceWithWordsCount(input:str,sep=' ',min=4)->str:
    """Funkcja wypisująca tylko zdania zawierające co najwyżej 4 wyrazy."""
    result = ""
    current_sentence = ""
    count = 0
    word = ''
    previous_char = ''
    for char in input:
        current_sentence += char
        if char.isalpha():#tools.isWhiteChar(char):
            word = word + char
        else:
            if(len(word)>0):
                 count +=1
                 word = ''
            if tools.isItEnd(previous_char,char):#char == '\n':
                if (len(current_sentence) > 0 and count >= min):
                    result += current_sentence + sep
                current_sentence = ""
                count = 0
                word = ''
        previous_char = char
    return result


#print(getSentenceWithWordsCount('Hello World dupa dupa.kurwa mac.chuj chuj hucj chuj.'))


