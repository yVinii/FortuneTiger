import tkinter as tk
from tkinter import messagebox
import random

# Definir os emojis e os valores de pontos associados
emojis = {
    "🤑": 20,
    "😎": 5,
    "🤩": 2,
    "😋": 1.6,
    "😶": 1,
    "🙄": 0.6,
    "👽": 40  # Coringa com valor 40
}

# Função para gerar um grid 3x3 com emojis aleatórios
def gerar_grid():
    return [[random.choice(list(emojis.keys())) for _ in range(3)] for _ in range(3)]

# Função auxiliar para calcular pontuação de uma combinação (linha ou diagonal)
def calcular_combinacao(combinacao):
    base = [emoji if emoji != "👽" else None for emoji in combinacao]
    if base.count(None) > 0:
        if base.count(None) == len(base):
            return emojis["👽"] * 10
        dominante = [emoji for emoji in base if emoji is not None]
        if len(set(dominante)) == 1:
            base = [dominante[0] if emoji is None else emoji for emoji in base]
    if len(set(base)) == 1:
        return emojis[base[0]] * 10
    return 0

# Funções para verificar linhas e diagonais
def calcular_linha_1(grid): return calcular_combinacao(grid[0])
def calcular_linha_2(grid): return calcular_combinacao(grid[1])
def calcular_linha_3(grid): return calcular_combinacao(grid[2])
def calcular_diag_1(grid): return calcular_combinacao([grid[i][i] for i in range(3)])
def calcular_diag_2(grid): return calcular_combinacao([grid[i][2 - i] for i in range(3)])

# Função para calcular os pontos totais
def calcular_pontos(grid):
    pontos_linha_1 = calcular_linha_1(grid)
    pontos_linha_2 = calcular_linha_2(grid)
    pontos_linha_3 = calcular_linha_3(grid)
    pontos_diag_1 = calcular_diag_1(grid)
    pontos_diag_2 = calcular_diag_2(grid)

    total_pontos = pontos_linha_1 + pontos_linha_2 + pontos_linha_3 + pontos_diag_1 + pontos_diag_2

    if pontos_linha_1 > 0 and pontos_linha_2 > 0 and pontos_linha_3 > 0:
        total_pontos *= 10

    return total_pontos

# Classe principal do jogo
class TigrinhoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tigrinho Cassino")
        self.pontos = 100

        # Frame para exibir os pontos
        self.frame_top = tk.Frame(master)
        self.frame_top.pack(pady=10)

        self.label_pontos = tk.Label(self.frame_top, text=f"Pontos: {self.pontos}", font=("Arial", 16))
        self.label_pontos.pack()

        # Frame para o grid
        self.frame_grid = tk.Frame(master)
        self.frame_grid.pack(pady=10)

        self.grid_labels = [[tk.Label(self.frame_grid, text="", font=("Arial", 20), width=4, height=2) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid_labels[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Botão para rodar a roleta
        self.frame_bottom = tk.Frame(master)
        self.frame_bottom.pack(pady=10)

        self.botao_rodar = tk.Button(self.frame_bottom, text="Rodar Roleta", command=self.rodar_roleta, font=("Arial", 14))
        self.botao_rodar.pack()

    def rodar_roleta(self):
        if self.pontos < 10:
            messagebox.showinfo("Fim de Jogo", "Você não tem pontos suficientes para jogar!")
            return

        self.pontos -= 10
        grid = gerar_grid()

        for i in range(3):
            for j in range(3):
                self.grid_labels[i][j].config(text=grid[i][j])

        ganhos = calcular_pontos(grid)
        self.pontos += ganhos

        self.label_pontos.config(text=f"Pontos: {self.pontos}")

        if ganhos > 0:
            messagebox.showinfo("Parabéns!", f"Você ganhou {ganhos} pontos!")
        else:
            messagebox.showinfo("Tente Novamente", "Você não ganhou pontos desta vez.")

# Iniciar a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = TigrinhoApp(root)
    root.mainloop()
