L=[15,7,27,39,2,10,11]
x=0
p=int(input("Digite o primeiro valor: "))
p2=int(input("Digite o segundo valor: "))
for x in range(x, len(L)):
    if p in L:
       L.index(p)
    else:
        print('O primeiro valor não está na lista')
        break

    if p2 in L:
        L.index(p2)  
    else:
        print('O segundo valor não está na lista')  
        break

if p in L and p2 in L:
    print(f'O valor {p} foi encontrado na posição {L.index(p)} e o valor {p2} foi encontrado na posição {L.index(p2)}')


