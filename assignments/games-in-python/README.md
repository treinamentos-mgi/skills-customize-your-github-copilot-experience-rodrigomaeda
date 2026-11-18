
# 📘 Assignment: Games in Python

## 🎯 Objective

Construa um jogo da forca em Python para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória.

## 📝 Tasks

### 🛠️ Implementar as Rodadas e os Palpites

#### Descrição
Complete o código inicial para selecionar uma palavra aleatória e permitir que o jogador tente adivinhá-la, revelando as letras corretas ao longo do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar a palavra secreta aleatoriamente da lista `words` usando `random.choice()`.
- Inicializar `guessed_letters`, `incorrect_guesses` e `max_incorrect` para controlar o estado do jogo.
- Exibir cada letra ainda não descoberta como `_` e revelar as letras já adivinhadas nas posições corretas.
- Solicitar um palpite de letra a cada rodada e atualizar o estado do jogo conforme o palpite.

### 🛠️ Controlar as Tentativas e Encerrar o Jogo

#### Descrição
Continue as rodadas até que o jogador descubra a palavra ou esgote o limite de palpites incorretos; então, informe o resultado.

#### Requisitos
O programa concluído deve:

- Aumentar `incorrect_guesses` quando o palpite não estiver na palavra secreta.
- Mostrar quantas tentativas incorretas ainda restam, com base em `max_incorrect`.
- Encerrar o jogo quando todas as letras forem descobertas ou o limite de tentativas incorretas for atingido.
- Exibir uma mensagem de vitória quando a palavra for descoberta; caso contrário, exibir uma mensagem de derrota e revelar a palavra secreta.