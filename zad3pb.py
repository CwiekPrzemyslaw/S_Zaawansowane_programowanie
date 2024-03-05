lista_c = [*range(0, 10)]


def parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

