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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes_navio:
        linha, coluna = posicao
        if linha < 0 or coluna < 0 or linha > 9 or coluna > 9:
            return False
        for navio in frota.values():
            for pos in navio:
                if posicao in pos:
                    return False
    return True

# Apêndice
tipos = ["porta-aviões","navio-tanque","contratorpedeiro","submarino"]
quant_navio = {"porta-aviões":1,"navio-tanque":2,"contratorpedeiro":3,"submarino":4}
d = {1:'vertical', 2:'horizontal'}
frota = {}
tamanho = 4

#Programa
for navio in tipos:
    i = 0
    Posicao_valida = True
    temp_frota = frota
    while i < quant_navio[navio]:
        Posicao_valida = True
        while Posicao_valida:
            print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanho))
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            
            if navio != 'submarino':
                vertical_horizontal = int(input('[1] Vertical [2] Horizontal: '))
                orientacao = d[vertical_horizontal]
        
            if posicao_valida(frota,linha,coluna,orientacao,tamanho) == True:
                preenche_frota(frota, navio,linha,coluna,orientacao,tamanho)
                Posicao_valida = False
            else:
                print('Esta posição não está válida!')
        i+=1
    tamanho -= 1

print(frota)


