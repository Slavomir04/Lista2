import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def whiteCharCounter(book:str)->int:
    """Funkcja zliczająca wszystkie znaki w tekście, z pominięciem białych znaków."""
    counter = 0

    for i in range(0, len(book), 1):
        if (not book[i].isspace()):
            counter += 1

    return counter

if __name__ == "__main__":
    name = sys.stdin.read()

    print(whiteCharCounter(name))