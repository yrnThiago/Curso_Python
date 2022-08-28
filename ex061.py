print('=>' * 20)
print('        GERADOR DE PA ')
print('<=' * 20)
primeiro = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a sua razão? '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo = termo + r
    cont += 1
print('Fim')