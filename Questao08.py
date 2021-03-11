'''8) A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.'''

T = [ -10, -8, 0, 1, 2, 5, -2, -4]

def media(t):
    soma = 0
    media = 0.0
    for e in t:
        soma += e
    media = soma / len(t)
    return media

def maior(t):
    maior = t[0]
    for e in t:
        if(e > maior):
            maior = e
    return maior
    
def menor(t):
    menor = t[0]
    for e in t:
        if(e < menor):
            menor = e
    return menor

print('Temperaturas: ', T)
print('Temperatura média: ', media(T))
print('Maior temperatura: ', maior(T))
print('Menor temperatura: ', menor(T))

