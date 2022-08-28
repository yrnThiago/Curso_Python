def area(a, b):
    t = a * b
    print(f'A área do terreno {a}x{b} é de {t}m²')


print('--- CONTROLE DE TERRENOS ---')
largura = float(input('LARGURA em METROS: '))
comprimento = float(input('COMPRIMENTO em METROS: '))
area(a=largura, b=comprimento)
