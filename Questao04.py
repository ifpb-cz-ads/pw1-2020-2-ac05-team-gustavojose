'''4) Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:

(()) OK
()()(()()) OK
()) Erro'''

def verificar(expressao):
    pilha = []
    for c in expressao:
        if c==')' and len(pilha)==0:
            return False
        if c=='(':
            pilha.append(c)
        else:
            topo=pilha[-1]
            if topo=='(' and c==')':
                pilha.pop()
            else:
                return False
    if len(pilha)==0:
        return True
    else:
        return False

string = str(input("informe a expressão:"))
if verificar(string) == True:
    print(string + " OK")
else:
    print(string + " Erro")

