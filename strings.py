string = 'Vem Tranquiloooo'
string2 = 'Pode vir'

print(string)

"""Exibindo pedaços da string"""
print(string[1:5])
print(string[0])
print(string[-5:])

"""Exibindo string reversa"""
print(string[::-1])

"""Concatenando strings"""
print(string + " " + string2)

"""tamanho da string"""
print(len(string))

"""index da string"""
print(string.index('q'))

"""contando quantas vezes uma letra aparece"""
print(string.count('o'))

"""Converter para letra maiuscula"""
print(string.upper())

"""Converter para minuscula"""
print(string.lower())

"""Cortando strings"""
print(string.split(" "))
print(string.split(" ")[0])
print(string.split(" ")[1])

"""Substituindo strings"""
print(string.replace("o", "a", 2))







#exercicio
frase = 'No dia mais claro, na noite mais escura, nenhum mal escapará a minha visão! Que aqueles que adoram o poder do mal, temam o meu poder. A LUZ DO LANTERNA VERDE!'
print(len(frase))
print(len(frase.split(" ")))

for i in frase.replace(',', '').replace('!', '').split(" "):
    if i in ['claro', 'escura', 'LANTERNA', 'VERDE']:
        print(i)

