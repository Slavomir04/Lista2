


def getAskYellSentence(input:str)->str:
    """Funkcja, która wypisuje na wyjściu tylko zdania, które są pytaniami lub wykrzyknieniami."""
    result = ""
    prev = ''
    current = ''
    for char in input:
        current = current + char
        if char =='\n':
            if prev == '!' or prev == '?':
                result = result + current
            current = ""
        prev = char
    if len(current)>1 and current[-1]=='!' or current[-1]=='?':
        result = result + current
    return result

#print(getAskYellSentence("chuj dupa cycki!\n to niej est wykrzyknienie! hehe\n jebac! disa?"))