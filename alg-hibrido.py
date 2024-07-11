import random
import time

def ordenacao_selecao(arr):
    n = len(arr)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]

def ordenacao_rapida(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        esq = [x for x in arr se x < pivo]
        meio = [x for x em arr se x == pivo]
        dir = [x for x em arr se x > pivo]
        return ordenacao_rapida(esq) + meio + ordenacao_rapida(dir)

def ordenacao_hibrida_rapida_selecao(arr, limite):
    ordenacao_hibrida(arr, 0, len(arr) - 1, limite)

def mediana_de_tres(arr, baixo, alto):
    meio = (baixo + alto) // 2
    candidatos_pivo = [(arr[baixo], baixo), (arr[meio], meio), (arr[alto], alto)]
    candidatos_pivo.sort(key=lambda x: x[0])
    return candidatos_pivo[1][1]

def ordenacao_selecao_sublista(arr, baixo, alto):
    for i in range(baixo, alto + 1):
        indice_min = i
        for j in range(i + 1, alto + 1):
            se arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]

def ordenacao_hibrida(arr, baixo, alto, limite):
    if alto - baixo + 1 <= limite:
        ordenacao_selecao_sublista(arr, baixo, alto)
    else:
        indice_pivo = mediana_de_tres(arr, baixo, alto)
        arr[baixo], arr[indice_pivo] = arr[indice_pivo], arr[baixo]
        pivo = arr[baixo]
        i = baixo + 1
        for j in range(baixo + 1, alto + 1):
            se arr[j] < pivo:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[baixo], arr[i - 1] = arr[i - 1], arr[baixo]
        ordenacao_hibrida(arr, baixo, i - 2, limite)
        ordenacao_hibrida(arr, i, alto, limite)

def gerar_lista_aleatoria(tamanho):
    return [random.randint(0, 1000000) para _ em range(tamanho)]

def medir_tempo(funcao_ordenacao, arr, *args):
    tempo_inicio = time.time()
    se args:
        funcao_ordenacao(arr, *args)
    else:
        funcao_ordenacao(arr)
    tempo_fim = time.time()
    return tempo_fim - tempo_inicio

# Tamanhos dos conjuntos de dados
tamanhos = [1000, 10000, 50000, 500000]
num_testes = 5  # Número de testes para média

for tamanho em tamanhos:
    tempos_selecao = []
    tempos_rapida = []
    tempos_hibrida16 = []
    tempos_hibrida64 = []
    tempos_hibrida256 = []
    
    for _ em range(num_testes):
        dados = gerar_lista_aleatoria(tamanho)
        
        # Medir tempo para Ordenação por Seleção
        dados_selecao = dados[:]
        tempo_selecao = medir_tempo(ordenacao_selecao, dados_selecao)
        tempos_selecao.append(tempo_selecao)
        
        # Medir tempo para Ordenação Rápida
        dados_rapida = dados[:]
        tempo_rapida = medir_tempo(ordenacao_rapida, dados_rapida)
        tempos_rapida.append(tempo_rapida)
        
        # Medir tempo para Ordenação Híbrida (16)
        dados_hibrida16 = dados[:]
        tempo_hibrida16 = medir_tempo(ordenacao_hibrida_rapida_selecao, dados_hibrida16, 16)
        tempos_hibrida16.append(tempo_hibrida16)
        
        # Medir tempo para Ordenação Híbrida (64)
        dados_hibrida64 = dados[:]
        tempo_hibrida64 = medir_tempo(ordenacao_hibrida_rapida_selecao, dados_hibrida64, 64)
        tempos_hibrida64.append(tempo_hibrida64)
        
        # Medir tempo para Ordenação Híbrida (256)
        dados_hibrida256 = dados[:]
        tempo_hibrida256 = medir_tempo(ordenacao_hibrida_rapida_selecao, dados_hibrida256, 256)
        tempos_hibrida256.append(tempo_hibrida256)
    
    print(f"Conjunto de Dados: {tamanho} elementos")
    print(f"Tempo médio Ordenação por Seleção: {sum(tempos_selecao) / num_testes:.6f} segundos")
    print(f"Tempo médio Ordenação Rápida: {sum(tempos_rapida) / num_testes:.6f} segundos")
    print(f"Tempo médio Ordenação Híbrida (16): {sum(tempos_hibrida16) / num_testes:.6f} segundos")
    print(f"Tempo médio Ordenação Híbrida (64): {sum(tempos_hibrida64) / num_testes:.6f} segundos")
    print(f"Tempo médio Ordenação Híbrida (256): {sum(tempos_hibrida256) / num_testes:.6f} segundos")
    print()
