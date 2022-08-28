s = int(input('Digite um valor e descubra a sua tabuada: '))
for mult in range(1, 11):
    print('{} x {:2} = {}'.format(s, mult, s*mult))
