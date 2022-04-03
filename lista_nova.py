v = [30,12,30,18,12]

#Tamanho da lista

tam = len(v)

#Adicionando elementos

v.append(7)

print(tam)

print(v)

#Verificar se elemento está na lista

if 30 in v:
	print("30 esta na lista")

#Removendo um elemento da lista

del v[3:]
print(v)

#Ordenando a lista

v.sort()

print(v)
#Ordenando, mas precisa ser atribuida a uma variável
m = sorted(v)
print(m)

#Imprimir do maior para o menor
v.sort(reverse=True)
print(v)

#Invertendo a lista do último para o primeiro
v.reverse()
print(v)

