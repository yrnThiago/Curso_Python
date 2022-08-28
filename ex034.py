s = float(input('Qual o salário do funcionário: R$'))
if s > 1250.00:
    a = (s / 100) * 10
else:
    a = (s / 100) * 15
sa = s + a
print('Salário do funcionário: R${:.2f}'.format(s))
print('O valor do aumento é: R${:.2f} '.format(a))
print('Salário do funcionário(com aumento): R${:.2f} '.format(sa))





