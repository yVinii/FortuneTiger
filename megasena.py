import random
from collections import Counter

def gerar_jogos_e_calcular_frequentes(n_jogos=10000):
    # Gerar n_jogos de 6 números entre 1 e 60
    jogos = [tuple(sorted(random.sample(range(1, 61), 6))) for _ in range(n_jogos)]
    # Contar frequência de cada número
    frequencia = Counter(num for jogo in jogos for num in jogo)
    # Retornar os 6 números mais frequentes
    return [num for num, _ in frequencia.most_common(6)]

# Lista para guardar os resultados dos 100 ciclos
resultados_mais_frequentes = []

# Executar o processo 100 vezes
for _ in range(100):
    mais_frequentes = gerar_jogos_e_calcular_frequentes()
    resultados_mais_frequentes.extend(mais_frequentes)

# Contar frequência dos números mais frequentes em todas as 100 execuções
frequencia_final = Counter(resultados_mais_frequentes)

# Obter os 6 números mais frequentes no total
mais_frequentes_final = [num for num, _ in frequencia_final.most_common(6)]

print("Os 6 números mais frequentes após 100 execuções são:", mais_frequentes_final)
