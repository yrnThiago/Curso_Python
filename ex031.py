v = float(input('Qual a distância da viagem: '))
p1 = v*0.50
p2 = v*0.45
if v > 200:
    print('A distância da viagem: {:.0f}km. \nO valor da passagem é de: R${:.2f}. \n(R$0.50/Km para viagens acima de 200Km)'.format(v, p1))
else:
    print('A distância da viagem: {:.0f}km. \nO valor da passagem é de: R${:.2f}. \n(R$0.45/Km para viagens abaixo de 200Km)'.format(v, p2))

