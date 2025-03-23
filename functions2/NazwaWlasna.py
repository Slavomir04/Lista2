
import tools
def procentNazwaWlasnych(input:str)->str:
    """Funkcja licząca procent zdań, które zawierają przynajmniej jedną nazwę własną (niech
nazwą własną będzie każdy wyraz napisany wielką literą, nie będący pierwszym wyrazem
w zdaniu)."""
    counter_sentences= 0
    counter = 0

    isThere = False
    first = True
    previous_char = ''
    for char in input:
        if tools.isItEnd(previous_char,char):
            counter_sentences += 1
            if (not first) and isThere:
                counter += 1
            isThere = False
            first = True
        elif not previous_char.isalpha() and char.isupper():
            if first:
                first = False
            else:
                isThere = True
        previous_char = char
    if (not first) and isThere:
        counter += 1
    return counter/counter_sentences*100


print(procentNazwaWlasnych('Jest Nazwa wlasna! Nie ma nazwy wlasnej? Tu tez nie. Tu Tak!'))