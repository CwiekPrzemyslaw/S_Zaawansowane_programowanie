lista_b = [1, 2, 3, 4, 5]


def mnoz_liczb(lista):
    liczby2 = []
    if len(lista) == 5:
        for liczba in lista:
            liczba = liczba * 2
            liczby2.append(liczba)
    return liczby2


def mnoz_liczb2(lista):
    if len(lista) == 5:
        lista_mnoz = [i * 2 for i in lista]
    return lista_mnoz
