import os
import random
from datetime import datetime, timedelta

def create_snake_commit():
    # Padrão do jogo da cobrinha
    snake_pattern = [
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    ]

    # Posição inicial da cobra
    snake_positions = [(5, 5), (5, 6), (5, 7)]
    
    # Direção inicial
    direction = (0, 1)  # Movendo para a direita
    
    # Comida
    food_position = (3, 3)
    
    # Atualiza o padrão com a cobra e a comida
    for pos in snake_positions:
        row, col = pos
        snake_pattern[row] = snake_pattern[row][:col] + "🟩" + snake_pattern[row][col+1:]
    
    row, col = food_position
    snake_pattern[row] = snake_pattern[row][:col] + "🍎" + snake_pattern[row][col+1:]
    
    # Cria o commit message
    commit_message = "snake: "
    for row in snake_pattern:
        commit_message += row + "\n"
    
    # Cria um arquivo temporário para o commit
    with open("snake.txt", "w") as f:
        f.write(commit_message)
    
    # Comandos git
    os.system("git add snake.txt")
    os.system(f'git commit -m "{commit_message}"')
    
    # Remove o arquivo temporário
    os.remove("snake.txt")

if __name__ == "__main__":
    create_snake_commit() 