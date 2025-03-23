import tools


def getAskYellSentence(input:str)->str:
    """Funkcja, która wypisuje na wyjściu tylko zdania, które są pytaniami lub wykrzyknieniami."""
    result = ""
    prev_char = ''
    current = ''

    for char in input:
        current = current + char
        if tools.isItEnd(prev_char,char):
            if char == '!' or char == '?':
                result = result + current
            current = ""
        prev_char = char
    if len(current)>1 and (current[-1]=='!' or current[-1]=='?'):
        result = result + current
    return result

print(getAskYellSentence("chuj dupa cycki! to niej est wykrzyknienie! hehe. jebac! disa? asdad!!!"))