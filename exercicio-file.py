import datetime
import os

agora = datetime.datetime.now()

#exemplo2
filename = agora.strftime('%Y-%m-%d.txt')

with open(filename, 'w') as f:
    for i in range(10):
        f.writelines(('teste %d\n') % (i))
        #f.writelines('teste' + str(i))
    f.close()

with open(filename, 'r') as f:
    lines = f.readlines()
    print(lines[0])
    print(lines[4])

with open(filename, 'a') as f:
    f.write('teste novalinha\n')
    f.close()

nomes = []
for i in range(1, 6):
    nomes.append('arquivo' + str(i) + '.txt')

print(nomes)

for f in nomes:
    fl = open(f, 'w')
    fl.close()

for i in os.listdir():
    if 'arquivo' in i:
        print(i)

