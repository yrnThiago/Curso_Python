from datetime import date


def voto(a):
    idade = date.today().year - a
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO! '
    elif idade == 17 or idade == 16 or idade >= 65:
        return f'Com {idade} anos, VOTO OPCIONAL! '
    elif idade < 16:
        return f'Com {idade} anos, NÃO VOTA! '


print('--' * 20)
nascimento = int(input('Em qual ano você nasceu? '))
print(voto(nascimento))

