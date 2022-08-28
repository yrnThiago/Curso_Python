def leiaint(prompt=None):
    if prompt is None:
        prompt = 'Digite um número: '
    inpt = input(prompt)
    while not inpt.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
        inpt = input(prompt)
    return int(inpt)


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}. ')
