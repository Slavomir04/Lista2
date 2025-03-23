
def longestSentence(input:str)->str:
    """Funkcja wypisująca najdłuższe zdanie w książce (kryterium – liczba znaków)."""
    max_sentence = ""
    current = ''
    for char in input:
        current += char
        if char == '\n':
            if len(current) > len(max_sentence):
                max_sentence = current
            current = ''
    if input[-1]!='\n' and len(current)+1 > len(max_sentence):
        max_sentence = current
    return max_sentence

#print(longestSentence("\n1234567\n123\n123456789\n12345678dd\n"))