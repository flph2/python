# Lista de 1 a 100
lista = list(range(1, 101))
print(lista)

# Pares e impares
pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(pares)
print(impares)

# numeros entre 1000 e 2000
lista = list(range(1000, 2001))
nova_lista = []

for n in lista:
    if (n % 7 == 0) and (n % 5 != 0):
        nova_lista.append(n)

print(nova_lista)


# contadores inversos
count = 0
count2 = 99

while count <= 99:
    print(str(count) + '-' + str(count2))
    count += 1
    count2 -= 1


# Loop infinito
while True:
    for n in range(1, 50):
        if n ** 3 == 6859:
            print(n)
    break

# Desenhar em ascii
qtd = 8

for i in range(qtd):
    for n in range(i):
        print("*", end='')
    print('')

# desenhar em ascii 2
y = '*'
for i in range(1, 8):
    print(y)
    y += '*'
