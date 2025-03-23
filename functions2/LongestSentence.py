import tools
def longestSentence(input:str)->str:
    """Funkcja wypisująca najdłuższe zdanie w książce (kryterium – liczba znaków)."""
    max_sentence = ""
    current = ''
    previous_char = ''
    for char in input:
        current += char
        if tools.isItEnd(previous_char,char):#char == '\n':
            if len(current) > len(max_sentence):
                max_sentence = current
            current = ''
        previous_char = char
    if len(current) > len(max_sentence):
        max_sentence = current
    return max_sentence

#print(longestSentence(".1234567. 123. 123456789. 1234567812312 1232112321 12321 1."))