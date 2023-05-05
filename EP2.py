import random as rd

def define_posicoes(linha,coluna,orientacao,tamanho):
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
        frota[nome_navio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

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

#Jogo
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

# Tabuleiros
tabuleiro_oponente = posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota)

# Listas para Check de Jogadas
jogadas_anteriores = []
jogadas_anteriores_oponente = []

# Condição continuação de jogo
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))

    # Jogador joga
    Check_Jogadas = True

    while Check_Jogadas:
        linha = coluna = ''
        while linha not in [0,1,2,3,4,5,6,7,8,9]:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            if linha not in [0,1,2,3,4,5,6,7,8,9]:
                print('Linha inválida!')
        
        while coluna not in [0,1,2,3,4,5,6,7,8,9]:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            if coluna not in [0,1,2,3,4,5,6,7,8,9]:
                print('Coluna inválida!')
        
        jogada = [linha,coluna]

        if jogada in jogadas_anteriores:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha, coluna))
        else:
            Check_Jogadas = False
    
    jogadas_anteriores.append(jogada)

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha, coluna)

    # Oponente Joga
    Check_Jogadas = True

    while Check_Jogadas:
        linha = coluna = jogada = ''
        while linha not in [0,1,2,3,4,5,6,7,8,9]:
            linha = rd.randint(0,9)
        
        while coluna not in [0,1,2,3,4,5,6,7,8,9]:
            coluna = rd.randint(0,9)
        
        jogada_oponente = [linha,coluna]

        if jogada_oponente not in jogadas_anteriores_oponente:
            Check_Jogadas = False

    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha,coluna))

    jogadas_anteriores_oponente.append(jogada_oponente)

    tabuleiro_jogador = faz_jogada(tabuleiro_jogador,linha, coluna)

    # Verifica quantos navios foram afundados
    afund_oponente = afundados(frota_oponente,tabuleiro_oponente)

    afund_jogador = afundados(frota,tabuleiro_jogador)

    # Verifica se alguém ganhou o jogo
    if afund_oponente == 10:
        jogando = False
        print('Parabéns! Você derrubou todos os navios do seu oponente!')

    if afund_jogador == 10:
        jogando = False
        print('Xi! O oponente derrubou toda a sua frota =(')