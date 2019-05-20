myDict = {
    "name": "Antony",
    "surname": "Edward Stark",
    "phrase": "Genius, billionaire, playboy, philanthropist"
}

print(myDict)
print(myDict['name'])
print(myDict['surname'])

""" Add item to dict"""
myDict['hero'] = 'Iron Man'
print(myDict)

""" Remove a item from dict"""
item = myDict.pop('name')
print(item)
print(myDict)

""" Remove ultimo item do dicionario"""
item = myDict.popitem()
print(item)
print(myDict)

colors = ['Red', 'Golden', 'Silver']
myDict['colors'] = colors
print(myDict)
print(myDict['colors'][0:2])

print(myDict.values())
print(myDict.keys())