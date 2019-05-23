import re

frase = '123 testando'
x = re.findall("testa", frase)
print(x)

x2 = re.search('te', frase)
print(x2.string)