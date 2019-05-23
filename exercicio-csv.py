import csv

lista_filmes = [{
    'nome': 'asdasd',
    'data': 'asdasd',
    'diretor': 'asdsd'
},
{
    'nome': 'asdasd',
    'data': 'asdasd',
    'diretor': 'asdasd'
}]

with open('filmes.csv', 'w', newline='') as f:
    l = csv.writer(f, delimiter=' ', quotechar='|')
    l.writerow(['nome', 'data','diretor'])
    for i in lista_filmes:
        string = i['nome'],i['data'], i['diretor']
        l.writerow(string)

    #l.writerow(['warriors, os selvagens da noite', '01/02/1979', 'Walter Hill' ])
    #l.writerow(['O senhor dos aneis, o retorno do rei', '25/12/2003', 'Peter Jackson' ])
    #l.writerow(['matrix', '21/05/1999', 'Lana Wachowski'])

lista = []
with open('filmes.csv', 'r', newline='') as f:
    l = csv.reader(f, delimiter=' ', quotechar='|')
    for row in l:
        lista.append(row)

for i in range(0, len(lista), 2):
    print(lista[i])

#print(lista[0])
#print(lista[2])

for i in range(len(lista)):
    print(lista[i][0])
