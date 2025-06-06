import random

# Tamanho do tabuleiro
tamanho = 3
 
# Quantos navios
total_navios = 3

# Tabuleiros
tabuleiro = [["🌊" for _ in range(tamanho)] for _ in range(tamanho)]
tabuleiro_oculto = [["🌊" for _ in range(tamanho)] for _ in range(tamanho)]

# Posicionar os navios
colocados = 0
while colocados < total_navios:
    linha = random.randint(0, tamanho - 1)
    coluna = random.randint(0, tamanho - 1)
    if tabuleiro_oculto[linha][coluna] != "🚢":
        tabuleiro_oculto[linha][coluna] = "🚢"
        colocados += 1

# Função para mostrar o tabuleiro visível
def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

# Contador de acertos
acertos = 0

print("🎮 BEM-VINDO AO JOGO DE BATALHA NAVAL!")
print("Dica: O mar é 🌊, acerto é 💥, erro é ❌")
print()

# Jogo principal
while acertos < total_navios:
    mostrar_tabuleiro()

    try:
        linha = int(input("Escolha a linha (0 a 4): "))
        coluna = int(input("Escolha a coluna (0 a 4): "))

        if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
            print("⚠️ Coordenadas fora do tabuleiro! Tente novamente.")
            continue

        if tabuleiro[linha][coluna] in ["💥", "❌"]:
            print("⛔ Você já atacou essa posição. Escolha outra.")
            continue

        if tabuleiro_oculto[linha][coluna] == "🚢":
            print("💥 Você acertou um navio!")
            tabuleiro[linha][coluna] = "💥"
            acertos += 1
        else:
            print("❌ Você errou.")
            tabuleiro[linha][coluna] = "❌"

    except ValueError:
        print("❗ Entrada inválida! Digite números inteiros de 0 a 4.")

print("\n🏆 PARABÉNS! Você destruiu todos os navios!")
mostrar_tabuleiro()
