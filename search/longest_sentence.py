import tools
import sys
import io




def longestSentence(input:str)->str:
    """Funkcja wypisująca najdłuższe zdanie w książce (kryterium – liczba znaków)."""
    tools.checkText(input)
    tools.checkIsEmpty(input)

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

if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


    book = sys.stdin.read()

    print(longestSentence(book))