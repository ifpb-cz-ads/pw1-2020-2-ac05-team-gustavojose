L=[15,7,27,39]
x=0
p=int(input("Digite o valor a procurar:"))
while x < len(L):
    if p in L:
        print(f'O numero {p} foi encontrado na posição {L.index(p)} da lista')
        break
    else:
        print(f'O numero {p} não está presente na lista')
        break
    x+=1
