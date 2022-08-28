palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'futuro', 'google')
#print(f'Na palavra {palavras[n].upper()} temos: ')
for m in palavras:
    print(f'A palavra {m.upper()} possui as seguintes vogais: ', end='')
    for s in m:
        if s in 'AaEeIiOoUu':
            print(s.upper(), end=' ')
    print('')
