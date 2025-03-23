def paragraphCounter(book:str)->int:
    """Funkcja zliczająca akapity w tekście (akapit jest oddzielony pustą linią)."""
    count = 0

    for i in range(0, len(book) - 1, 1):
        if (book[i:i+2] == "\n\n"):
            count += 1

    return count

def whiteCharCounter(book:str)->int:
    """Funkcja zliczająca wszystkie znaki w tekście, z pominięciem białych znaków."""
    counter = 0

    for i in range(0, len(book), 1):
        if (not book[i].isspace()):
            counter += 1

    return counter

def countSentences(title:str)->int:
    counter = 0
    separators = ["?", ".", "!"]
    for i in range(0, len(title), 1):
        if (title[i] in separators):
            counter+=1
    return counter

def countPercent(title:str)->float:
    counter = 0
    isOwnNameFinded = False
    separators_combination = ["— ", "\n\n", "! ", ". ", "? "]
    separators = ["?", ".", "!"]
    for i in range(2, len(title), 1):
        if (title[i].isupper() and title[i-2:i] not in separators_combination and title[i-1] == " "):
            isOwnNameFinded = True
        elif (title[i] in separators and isOwnNameFinded):
            counter+=1
            isOwnNameFinded = False

    return counter





