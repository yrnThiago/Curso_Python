turma = dict()


def notas(*n, sit=None):
    """
    -> Função para analisar notase situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    media = cont = 0
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    for m in n:
        media += m
    media = media / len(n)
    turma['media'] = media
    if sit is True:
        if media == 10:
            turma['situaçao'] = 'EXCELENTE!'
        elif media == 9:
            turma['situaçao'] = 'ÓTIMA!'
        elif 8 >= media > 6:
            turma['situaçao'] = 'BOA!'
        elif 6 >= media > 4:
            turma['situaçao'] = 'RAZOÁVEL!'
        else:
            turma['situaçao'] = 'RUIM!'

    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
