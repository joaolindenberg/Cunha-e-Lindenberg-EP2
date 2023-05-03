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


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota:
        frota[nome_navio] = []
        frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    else:
        frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(infos):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
    ]
    for coordenadas in infos.values():
        for posicao in coordenadas:
            for x, y in posicao:
                tabuleiro[x][y] = 1
    return tabuleiro



def afundados(infos, tabuleiro):
    afundados = 0
    for coordenadas in infos.values():
        for posicao in coordenadas:
            afundado = True
            for x, y in posicao:
                if tabuleiro[x][y] != 'X':
                    afundado = False
            if afundado:
                afundados += 1
    return afundados
