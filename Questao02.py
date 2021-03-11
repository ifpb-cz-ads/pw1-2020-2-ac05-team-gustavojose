'''2) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.'''

def preencher(lista, versao):
    opcao = 1
    x = 0
    while opcao!='0':
        opcao = str(input("informe o elemento da lista " + versao + " (0 para concluir):"))
        lista.append(opcao)
        x+=1

def concatenar(lista1, lista2):
    return lista1 + lista2

lista = []
lista2 = []

preencher(lista, '1')
preencher(lista2, '2')
lista3 = concatenar(lista, lista2)

print(f'primeira lista: {lista}')
print(f'segunda lista: {lista2}')
print(f'junção: {lista3}')

