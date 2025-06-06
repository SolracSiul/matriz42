print("lets go guyyyss")
def exibir_tabela(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-"*9)

exibir_tabela(["x","y"])
#print("sorak".join("rodrigues"))

def verificarVitoria(tabuleiro, jogador):
    # Verifica linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Verifica colunas
    for col in range(3):
        if all(tabuleiro[lin][col] == jogador for lin in range(3)):
            return True

    # Verifica diagonal principal (↘)
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    # Verifica diagonal secundária (↙)
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    # Se nenhuma condição de vitória foi encontrada
    return False

def jogo_da_velha():
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]  # matriz 3x3
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabela(tabuleiro)

        try:
            linha = int(input("Informe a linha (0, 1 ou 2): "))
            coluna = int(input("Informe a coluna (0, 1 ou 2): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        # Verifica se a jogada é válida
        if linha not in range(3) or coluna not in range(3):
            print("Linha ou coluna fora do intervalo!")
            continue

        if tabuleiro[linha][coluna] != "":
            print("Essa posição já está ocupada!")
            continue

        # Marca a jogada
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        # Verifica vitória
        if verificarVitoria(tabuleiro, jogador_atual):
            exibir_tabela(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        # Verifica empate
        elif jogadas == 9:
            exibir_tabela(tabuleiro)
            print("Empate!")
            break

        # Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"