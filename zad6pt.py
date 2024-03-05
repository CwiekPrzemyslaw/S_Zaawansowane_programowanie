def funkcja_6(lista1: list, lista2: list):
    final_list = lista1 + lista2
    final_list = list(dict.fromkeys(final_list))
    return [x**3 for x in final_list]


print(funkcja_6([1, 2, 3, 4], [2, 3, 6, 10]))
