import random
import time

def testar_ate_acertar(escolhidos):
    tentativas = 0
    sorteado = []
    
    # Enquanto o jogo sorteado não for igual ao escolhido
    while sorteado != escolhidos:
        sorteado = sorted(random.sample(range(1, 61), 6))  # Gerar um jogo
        tentativas += 1
    
    return tentativas

# Seus números escolhidos
meus_numeros = sorted([6, 16, 24, 36, 41, 53])  # Números escolhidos

# Iniciar o timer
inicio = time.time()

# Rodando a simulação
tentativas_necessarias = testar_ate_acertar(meus_numeros)

# Finalizar o timer
fim = time.time()
tempo_decorrido = fim - inicio

print(f"Os números {meus_numeros} foram sorteados após {tentativas_necessarias} tentativas.")
print(f"Tempo total: {tempo_decorrido:.2f} segundos.")
