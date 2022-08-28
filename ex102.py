def fatorial(n=1, show=False):
    print('--' * 20)
    if show:
        f = 1
        cont = 0
        for v in range(n, 0, -1):
            cont += 1
            if cont < n:
                print(f'{v} x', end=' ')
            else:
                if cont == n:
                    print(f'{v} = ', end='')
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f


print(fatorial(5, show=False))

