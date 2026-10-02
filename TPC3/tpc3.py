print("O computador começa! Boa sorte.")
total = 0

num_computador = 1
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