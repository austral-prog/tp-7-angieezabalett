def enumerate_list(list):
    lista = []
    for posicion, elemento in enumerate(list):
        if elemento != "":
            largo = len(lista)
            lista.append(f"{largo}. {elemento}")
    return lista


def enumerate_backwards(list):
    lista = []
    for posicion, elemento in enumerate(list):
        if elemento != "":
            largo = len(lista)
            lista.append(f"{largo}. {elemento[::-1]}")
    return lista
