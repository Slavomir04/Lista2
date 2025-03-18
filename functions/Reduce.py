def __nonWhiteValues()->list[str]:
    return [' ',',','.','-','/']

def __splitFromChars(string:str,ignore:list[str],nondigit=False)->list[str]:
    if(len(ignore)==0):
        return str
    result = []
    array = []
    for c in string:
        if ignore.__contains__(c) or (nondigit and c.isdigit()):
            if(len(array)>0):
                result.append(''.join(array))
            array = []
            continue
        else:
            array.append(c)
    if(len(array)>0):
        result.append(''.join(array))
    return result

def paragraphCounter(array:list[str])->int:
    return len(array)

def whiteCharCunter(array:list[str])->int:
    c =0
    for line in array:
        for c in line:
            if (ord('a')<=ord(c) and ord(c)<=ord('z') ) or (ord('A')<=ord(c) and ord(c)<=ord('Z')):
                c+=1

    return c

def oneNameCounterInLine(line:str)->int:
        c=0
        a = __splitFromChars(string=line,ignore=__nonWhiteValues(),nondigit=True)
        for i in range(1,len(a)):
            first_char = a[i][0]
            if ord('A') <= ord(first_char) <= ord('Z'):
                c+=1
        return c

def procentNazwaWlasnych(array:list[str])->float:
    if(len(array)==0):
        raise "array is empty"
    c=0
    for x in array:
        if oneNameCounterInLine(x)!=0:
            c+=1
    return c/len(array)*100






