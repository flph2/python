import random
n = random.randrange(10000, 99999)
print(n)

coc = random.choice(['cara', 'coroa'])
print(coc)

megasena = []
count = 0
while True:
    n = random.randrange(1, 61)
    if n not in megasena:
        megasena.append(n)
        count += 1
    if count >= 6:
        break

print(megasena)