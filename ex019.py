import random
a1 = str(input('Primeiro  aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print("O aluno sorteado foi o(a): {}".format(sorteado))


