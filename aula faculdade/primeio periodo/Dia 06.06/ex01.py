'''
lista = [1,2,3]
print(lista)
lista[0] = 2
print(lista)
lista.append(4)
print(lista)
lista.remove(3)
'''

#tupla
'''
tupla = (1,2,3)
print(tupla)
tupla[0] = 10 #não é possivel adicionar (imutáveis)
print(tupla)
'''
#coordenadas = (10,20)
#dados_pessoais = ("Ana", 22, "Juan", 23)


#.count
#tupla = (100, 1000, 10, 1)
#print(tupla.count(2))#4

#.index

#print(tupla.index(1)) #3


#Conjuntos > set
#estrutura não ordenada e sem elementos
#repetivivos
#numeros = {4,1,3,6,3,2,2,5}
#print(numeros)

#numeros.add(9)
#print(numeros)
#numeros.remove(4)
#print(numeros)
#numeros.discard(9)
#print(numeros)


#1 União - union
#2 intersecção

a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
