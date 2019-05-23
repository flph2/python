
a = 0

if a <= 10:
    print('menor')
else:
    print('maior')

if a == 1:
    print('é um')
elif a > 1 and a <= 10:
    print('esta entre 1 e 10')
elif a == 0:
    print('é zero')
elif a < 1:
    print('é um numero negativo')
else:
    print('maior q 10')


teste = 'Teste 123 teste'

if 'Teste' in teste:
    print('Achei')


if '123' in teste:
    print('tem numero')
else:
    print('nao tem numero')