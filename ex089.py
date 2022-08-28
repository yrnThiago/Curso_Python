boletim = list()
while True:
    nome = str(input('Aluno(a): '))
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    mais = str(input('Deseja continuar? (S/N) ')).upper()
    if 'N' in mais:
        break
print('=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 20)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 20)
    aluno = int(input('Mostrar notas de qual aluno? (999 para sair do programa) '))
    print('--' * 20)
    if aluno == 999:
        print('Saindo do programa..')
        break
    if aluno <= len(boletim) - 1:
        print(f'As notas de {boletim[aluno][0]} são {boletim[aluno][1]}')
print('*** VOLTE SEMPRE ***')