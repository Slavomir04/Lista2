import sys
import io
import tools




def paragraphCounter(book:str)->int:
    """Funkcja zliczająca akapity w tekście (akapit jest oddzielony pustą linią)."""

    tools.checkText(book)
    tools.checkIsEmpty(book)
    count = 0

    for i in range(0, len(book)-2, 1):
        if (book[i:i+2] == "\n\n"):
            count += 1

    return count

if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    name = sys.stdin.read()

    print(paragraphCounter(name))