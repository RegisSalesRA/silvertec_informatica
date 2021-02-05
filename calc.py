lista = ['16','16','15']
    
lista_int = []
for item in lista:
    item = int(item)
    lista_int.append(item)
    #for int in item:

total = sum(lista_int)
print(total)