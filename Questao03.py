lista1 = [1,2,3]
lista2 = [1,5,6]
lista3 = lista1 + lista2

lista3 = list(dict.fromkeys(lista3))
print(lista3)