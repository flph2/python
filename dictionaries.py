#myDict = {
#    "name": "Antony",
#    "surname": "Edward Stark",
#    "phrase": "Genius, billionaire, playboy, philanthropist"
#}
#
#print(myDict)
#print(myDict['name'])
#print(myDict['surname'])
#
#""" Add item to dict"""
#myDict['hero'] = 'Iron Man'
#print(myDict)
#
#""" Remove a item from dict"""
#item = myDict.pop('name')
#print(item)
#print(myDict)
#
#""" Remove ultimo item do dicionario"""
#item = myDict.popitem()
#print(item)
#print(myDict)
#
#colors = ['Red', 'Golden', 'Silver']
#myDict['colors'] = colors
#print(myDict)
#print(myDict['colors'][0:2])
#
#print(myDict.values())
#print(myDict.keys())
#

carros = [
    {
        'marca': 'asdasd',
        'modelo': 'modelo1',
        'codinome': 'asdasd',
    },
    {
        'marca': 'asdasd',
        'modelo': 'modelo2',
        'codinome': 'asdasd',
    }
]


carro1 = carros[0]
carro2 = carros[1]

print(carro1['modelo'])
print(carro2['modelo'])


tamanho = len(carros)
print(tamanho)

modelos = []

for c in range(0, tamanho):
    modelos.append(carros[c]['modelo'])
    modelos.append(carros[c]['codinome'])


codinomes = []
for c in range(0, tamanho):
    codinomes.append(carros[c]['codinome'])

modelos.sort()
print(modelos)

print(carros[0])
print(carros[1])
