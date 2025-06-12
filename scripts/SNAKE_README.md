# 🐍 Snake Game no GitHub

Este repositório contém scripts para criar uma animação do jogo da cobrinha (Snake Game) usando commits do GitHub. A animação será visível no seu perfil do GitHub através do gráfico de contribuições.

## 📋 Requisitos

- Python 3.6+
- Git instalado e configurado
- Repositório Git inicializado

## 🚀 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/snake-game.git
cd snake-game
```

2. Execute o script de animação:
```bash
python snake_animation.py
```

## 🎮 Como funciona

O script `snake_animation.py` cria uma sequência de commits que formam uma animação do jogo da cobrinha. Cada commit representa um frame da animação, onde:

- ⬜ representa o espaço vazio
- 🟩 representa a cobra
- 🍎 representa a comida

## ⚙️ Personalização

Você pode personalizar o jogo modificando as seguintes variáveis no arquivo `snake_animation.py`:

- `width` e `height`: Tamanho do tabuleiro
- `max_moves`: Número máximo de movimentos
- `time.sleep()`: Intervalo entre os commits

## 📝 Notas

- O script cria commits reais no seu repositório
- Cada commit contém um arquivo temporário `snake.txt`
- O arquivo é removido após cada commit
- A animação será visível no seu perfil do GitHub

## ⚠️ Aviso

Use este script com cuidado, pois ele cria commits reais no seu repositório. Recomenda-se usar em um repositório de teste ou em um branch separado.

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias no código ou reportar bugs através de issues e pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 