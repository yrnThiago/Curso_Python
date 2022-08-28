ex = list()
p = '('
pp = ')'
expressao = str(input('Digite a expressão: '))
ex.append(expressao)
if expressao.count(p) == expressao.count(pp):
        if expressao[0] == '(' and expressao[-1] == ')':
            print('Sua expressão está válida!')
        else:
            print('Sua expressão está errada!')
else:
    if expressao.count(p) != expressao.count(pp):
        print('Sua expressão está errada!')
