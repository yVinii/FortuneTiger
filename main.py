import time

# Lista de números fornecidos (sem os 0s que podem interferir no cálculo)
numeros = [226.52,
628.28,
2480,
7827.29,
12438.15,
9257.79,
6386.81,
0.27,
3513.13,
8085.29,
107048.15,
30372.6,
45319.22,
51899.9,
23769.82,
690.69,
]

# Defina o valor alvo
alvo = 24036.57

def encontrar_combinacao_v2(numeros, alvo, tempo_maximo=3600):
    dp = {0: []}  # Iniciando o mapa com a soma 0 e combinação vazia
    inicio = time.time()  # Hora de início
    for num in numeros:
        if time.time() - inicio > tempo_maximo:  # Verifica se o tempo passou do limite
            print("Tempo máximo atingido!")
            return None
        # Processando as combinações já existentes
        for soma in list(dp.keys()):
            nova_soma = soma + num
            if nova_soma == alvo:
                return dp[soma] + [num]
            if nova_soma < alvo and nova_soma not in dp:
                dp[nova_soma] = dp[soma] + [num]
    return None

# Buscar a combinação
combinacao = encontrar_combinacao_v2(numeros, alvo, tempo_maximo=3600)

if combinacao:
    print(f'Combinacao encontrada: {combinacao}')
else:
    print("Nenhuma combinação encontrada ou tempo máximo atingido.")
