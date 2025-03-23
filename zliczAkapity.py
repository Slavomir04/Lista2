import sys
import io
import re
from functions.Reduce import paragraphCounter

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
def deleteWhiteSpaces(book:str):
    return "\n".join(" ".join(line.split()) for line in book.split("\n")).strip()

def divideIntoSentences(book:str):
    return re.split(r'(?<=[.!?])', deleteWhiteSpaces(book))

if __name__ == '__main__':
    data = sys.stdin.read()
    data = divideIntoSentences(data)
    print(paragraphCounter(data))
