import sys
import io
import re
from functions.Reduce import countPercent
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def checkPreambula(book:str):
     line_counter = 0
     counter = 0
     isPreambula = False
     while line_counter <= 10:
         if (book[counter:counter+3] == "\n\n\n"):
             isPreambula = True
             line_counter += 2
         elif (isPreambula == True and book[counter] != "\n" and book[counter] != " "):
             return counter
         elif (book[counter:counter+2] == "\n\n"):
             line_counter += 1

         counter+=1
     return 0


def checkEnd(book:str):
    for counter in range(0, len(book) - 1, 1):
       if (book[counter:counter + 5] == "-----"):
           return counter

def deleteWhiteSpaces(book:str):
    return "\n".join(" ".join(line.split()) for line in book.split("\n")).strip()

def divideIntoSentences(book:str):
    return re.split(r'(?<=[.!?])', deleteWhiteSpaces(book))


if __name__ == "__main__":
    name = sys.stdin.read()

    title = deleteWhiteSpaces(name)







