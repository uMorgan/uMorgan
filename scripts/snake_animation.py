import os
import random
from datetime import datetime, timedelta
import time
import subprocess

class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.snake = [(5, 5), (5, 6), (5, 7)]  # Posição inicial da cobra
        self.direction = (0, 1)  # Movendo para a direita
        self.food = self.generate_food()
        self.score = 0
        
    def generate_food(self):
        while True:
            food = (random.randint(0, self.height-1), random.randint(0, self.width-1))
            if food not in self.snake:
                return food
    
    def move(self):
        # Calcula nova posição da cabeça
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Verifica colisão com as paredes
        if (new_head[0] < 0 or new_head[0] >= self.height or
            new_head[1] < 0 or new_head[1] >= self.width):
            return False
        
        # Verifica colisão com a própria cobra
        if new_head in self.snake:
            return False
        
        # Adiciona nova cabeça
        self.snake.insert(0, new_head)
        
        # Verifica se comeu a comida
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()
        
        return True
    
    def get_board(self):
        board = [["⬜" for _ in range(self.width)] for _ in range(self.height)]
        
        # Desenha a cobra
        for pos in self.snake:
            board[pos[0]][pos[1]] = "🟩"
        
        # Desenha a comida
        board[self.food[0]][self.food[1]] = "🍎"
        
        return board

def run_git_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Erro ao executar comando: {command}")
        return False

def create_commit(board, score):
    commit_message = f"snake: score={score}\n"
    for row in board:
        commit_message += "".join(row) + "\n"
    
    # Cria um arquivo temporário para o commit
    with open("snake.txt", "w") as f:
        f.write(commit_message)
    
    # Comandos git
    if not run_git_command("git add snake.txt"):
        return False
    
    if not run_git_command(f'git commit -m "{commit_message}"'):
        return False
    
    if not run_git_command("git push origin main"):
        return False
    
    # Remove o arquivo temporário
    os.remove("snake.txt")
    return True

def check_git_setup():
    # Verifica se o git está configurado
    if not run_git_command("git config --get user.name"):
        print("Erro: Git não está configurado. Configure seu nome com:")
        print("git config --global user.name \"Seu Nome\"")
        return False
    
    if not run_git_command("git config --get user.email"):
        print("Erro: Git não está configurado. Configure seu email com:")
        print("git config --global user.email \"seu.email@exemplo.com\"")
        return False
    
    # Verifica se o repositório está inicializado
    if not os.path.exists(".git"):
        print("Erro: Repositório Git não inicializado. Execute:")
        print("git init")
        return False
    
    # Verifica se o remote está configurado
    if not run_git_command("git remote get-url origin"):
        print("Erro: Remote 'origin' não configurado. Execute:")
        print("git remote add origin https://github.com/seu-usuario/snake-game.git")
        return False
    
    return True

def main():
    if not check_git_setup():
        return
    
    game = SnakeGame()
    moves = 0
    max_moves = 50  # Número máximo de movimentos
    
    print("Iniciando animação do jogo da cobrinha...")
    print("Pressione Ctrl+C para parar a qualquer momento")
    
    try:
        while moves < max_moves:
            # Muda a direção aleatoriamente
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            game.direction = random.choice(directions)
            
            # Move a cobra
            if not game.move():
                print("Game Over!")
                break
            
            # Cria o commit
            board = game.get_board()
            if not create_commit(board, game.score):
                print("Erro ao criar commit. Parando...")
                break
            
            print(f"Movimento {moves + 1}/{max_moves} - Score: {game.score}")
            moves += 1
            time.sleep(1)  # Espera 1 segundo entre os commits
            
    except KeyboardInterrupt:
        print("\nAnimação interrompida pelo usuário")
    
    print("Animação finalizada!")

if __name__ == "__main__":
    main() 