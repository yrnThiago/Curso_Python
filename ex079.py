valores = list()
while True:
    p = int(input('Digite um valor: '))
    if p not in valores:
        valores.append(p)
        print('Valor adicionado com sucesso. ')
    else:
        if p in valores:
            print('Valor duplicado! Não vou adicionar. ')
    c = input('Deseja continuar? (S/N) ').upper()
    if c == 'N':
        break
print('-=' * 20)
print(f'Você digitou os valores: {sorted(valores)}')