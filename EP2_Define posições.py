def define_posicoes(linha,coluna,orientacao,tamanho):
    if orientacao not in ['vertical', 'horizontal']:
        return []
    else:
        posicao = []
        if orientacao == 'vertical':
            for i in range(linha,linha+tamanho):
                posicao.append([i,coluna])
        else:
            for i in range(coluna,coluna+tamanho):
                posicao.append([linha,i])
    return posicao