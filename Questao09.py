string = 'Maximus'
cont = {}

for char in string:
    cont.setdefault(char,0)
    cont[char] +=1

print(cont)