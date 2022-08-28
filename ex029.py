vel = int(input('Velocidade atual do veículo: '))
vel1 = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou o limite de 80km/h! A Multa é de R${:.2f}. (R$7.00 por km acima do limite). '.format(vel1))
else:
    print('Você está no limite da via! Continue sendo um motorista exemplar! ')
