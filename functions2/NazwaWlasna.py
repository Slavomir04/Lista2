

def procentNazwaWlasnych(input:str)->str:
    """Funkcja licząca procent zdań, które zawierają przynajmniej jedną nazwę własną (niech
nazwą własną będzie każdy wyraz napisany wielką literą, nie będący pierwszym wyrazem
w zdaniu)."""
    counter_sentences= 0
    counter = 0

    isThere = False
    first = True
    prev = ''
    for char in input:
        if char == '\n':
            counter_sentences += 1
            if (not first) and isThere:
                counter += 1
            isThere = False
            first = True
        elif prev==' ' and char.isupper():
            if first:
                first = False
            isThere = True
        prev = char
    if input[-1] != '\n':
        counter_sentences += 1
    if (not first) and isThere:
        counter += 1
    return counter/counter_sentences*100


#print(procentNazwaWlasnych('Tak Nie\nCi na imiIe Taj\nnie'))