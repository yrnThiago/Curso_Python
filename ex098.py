from time import sleep


def contador(inicio, fim, passo=1):
    if inicio > fim and passo > 0:
        print(f'--- Contagem de {inicio} até {fim} de {passo} em {passo} ---')
        for v in range(inicio, fim - passo, -passo):
            sleep(0.25)
            print(v, end=' ')
        print('FIM!')
    elif inicio < fim and passo > 0:
        print(f'--- Contagem de {inicio} até {fim} de {passo} em {passo} ---')
        for v in range(inicio, fim + passo, passo):
            sleep(0.25)
            print(v, end=' ')
        print('FIM!')
    elif passo < 0:
        print(f'--- Contagem de {inicio} até {fim} de {-1*passo} em {-1*passo} ---')
        for v in range(inicio, fim + passo,  passo):
            sleep(0.25)
            print(v, end=' ')
        print('FIM!')
    elif passo == 0:
        print(f'--- Contagem de {inicio} até {fim} de {passo} em {passo} ---')
        for v in range(inicio, fim,  passo):
            sleep(0.25)
            print(v, end=' ')
        print('FIM!')




contador(1, 10)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: : '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
contador(inicio, fim, passo)
print('Tenha um bom dia! ')

