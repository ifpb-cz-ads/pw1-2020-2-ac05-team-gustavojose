'''5) Modifique o programa abaixo de forma a realizar a mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída do while.

L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
achou=False
x=0
while x<len(L):
    if L[x]==p:
            achou=True
            break
        x+=1
if achou:
    print("%d achado na posição %d" % (p,x))
else:
    print("%d não encontrado" % p)
    
6) Modifique o programa anterior para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.'''

def procurar(n):
    print("%d achado primeiro" % (p))

L=[15,7,27,39]
p=int(input("Digite o valor a procurar:"))
v=int(input("Digite outro valor a procurar também:"))
x=0
while x<len(L):
    if L[x]==p:
        print("%d achado primeiro" % (p))
        break
    elif L[x]==v:
        print("%d achado primeiro" % (v))
        break
    elif x+1==len(L):
        print("Nem %d, nem %d foram encontrados" % (p, v))
    x+=1

