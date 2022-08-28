mais = homem = fmenos = 0
from time import sleep
while True:
    print('->' * 20)
    print('         CADASTRE UMA PESSOA ')
    print('->' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo? (M/F) ').upper())
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            fmenos += 1
    print('--' * 20)
    if idade > 18:
        mais += 1
    c = str(input('Quer continuar? (S/N) ').upper())
    if c == 'N':
        break
sleep(1)
print('--' * 20)
print(f'{mais} pessoas tem mais de 18 anos. ')
print(f'{homem} homens foram cadastrados. ')
print(f'{fmenos} mulheres abaixo de 20 anos foram cadastradas. ')
print('--' * 20)