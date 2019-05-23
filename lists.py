#lista = ['Homer', 30, 'Moe', 'Bart', 10, 'Bob', 'Lisa', 1984]
#lista2 = [1967, 1982, 1954, 1938]
#
#print(lista)
#
#print(lista[0])
#print(lista[1:3])
#print(lista[2:])
#print(lista * 2)
#
#print(lista.append('asd'))
#print(lista)
#del(lista[2])
#print(lista)
#lista.insert(5, 'Barney')
#print(lista.pop(3))
#
#print(lista2)
#lista2.sort()
#print(lista2)
#

lista = ["Guerras Secretas", "A Guerra do Alto Evolucionário", "Inferno", "Ataque Atlantes", "Atos de Vingança",  "Dinastina M"]
print(lista)

print(len(lista))
print(lista[2] + " " + str(lista[4]))
print(lista[1] + " " + lista[3])

print(lista.pop(lista.index('Inferno')))
del(lista[2])

print(lista.sort())
print(lista)
lista.insert(2, 'A essência do medo')
print(lista)


