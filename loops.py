def index_of_by_index(word, list, index):
    for position, element in enumerate(list):
        if position >= index:
            if element == word:
                return position
    else:
        return -1

def index_of_empty(list):
    for position, element in enumerate(list):
        if element == "":
            return position
    return -1


def index_of(word, list):
    for indice, element in enumerate(list):
        if element == word:
            return indice
    else:
        return -1


def put(word, list):
    for position in range(0, len(list)):
        if list[position] == "":
            list[position] = word
            return position
    return -1


def remove(word, list):
    cant = 0
    for position, element in enumerate(list):
        if element == word:
            list[position] = ""
            cant = cant + 1
    return cant
