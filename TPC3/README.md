# TPC2: Corrida para o 100
# # Autor: 
Iara Gonçalves;
114372; 
Foto:<img width="1206" height="903" alt="image" src="https://github.com/user-attachments/assets/7de1be52-e4cf-490d-8a4c-09af65c99228" />

## Resumo: O trabalho de casa dado na terceira aula da teórica e prática tem como intuito criar um programa em python para o jogo "Corrida para o 100", em que o total começa no zero, o jogador e o computador alternam somando um número de 1 a 10 ao total e quem atingir exatamente o número 100 vence.

# Código:
print("O computador começa! Boa sorte.")
total = 0

num_computador = 10
total = total + num_computador
print(f"O computador adiciona {num_computador}. Total = {total}")

while total < 100:
    num_jogador = int(input("Escolhe um número de 1 a 10: "))
    total = total + num_jogador
    print(f"Adicionou {num_jogador}. Total = {total}")
    
    if total == 100:
        print("Ganhaste!!")
        break
    
    num_computador = 11 - num_jogador
    total = total + num_computador
    print(f"Computador adiciona {num_computador}. Total = {total}")
    
    if total == 100:
        print("O computador ganhou!")
        break
