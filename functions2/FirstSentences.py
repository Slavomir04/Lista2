


def getFirstSentences(input:str,number:int=20)->str:
    result = ''
    for char in input:
        if number<=0:
            break
        else:
            result = result + char
            if char=='\n':
                number-=1

    return result



#print(getFirstSentences('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13',10))