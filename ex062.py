print('=>' * 20)
print('        GERADOR DE PA ')
print('<=' * 20)
primeiro = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a sua razão? '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo = termo + r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados. '.format(total))