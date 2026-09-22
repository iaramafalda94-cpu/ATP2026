# TPC2: Adivinha o número
# # Autor: 
Iara Gonçalves;
114372; 
Foto:<img width="1206" height="903" alt="image" src="https://github.com/user-attachments/assets/7de1be52-e4cf-490d-8a4c-09af65c99228" />

## Resumo: O trabalho de casa dado na segunda aula da teórica e prática tem como intuito criar um programa em python para o jogo "adivinha o número", em que esse mesmo jogo poderia ter duas modalidades: o computador pensa num número (entre 0 e 100)e o utilizador tenta adivinhar ou o utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar;    Quem tenta adivinhar responde com uma das afirmações: "Acertou", "O número que pensei é Maior" ou "O número que pensei é Menor". Uma vez descoberto o número o programa deve terminar imprimindo o número de tentativas que quem adivinhou usou para chegar ao resultado.

## resultados (programa em python):
[Jogo adivinha o número.py](https://github.com/user-attachments/files/32538463/Jogo.adivinha.o.numero.py)

# Código:
inicio= input("Olá jogador vamos jogar ao jogo ´adivinha o número`, eu ja pensei no meu número entre 0 e 100! Podes tentar adivinhar respondendo apenas com um número inteiro. Boa sorte! Escreve: ´ . ` ,para começar o jogo")
if inicio== ".":
    n= int(input("adivinha o número:"))
    tentativas = 1
    while n!=23:
        if n>23:
            n= int(input("o número que pensei é menor, tenta novamente:"))
        elif n<23:
            n= int(input("o número que pensei é maior, tenta novamente:"))
        tentativas = tentativas + 1
    print("Acertou!")
    print(f"Usaste {tentativas} tentativas para acertar no número que pensei")
else:
    print("Erro! Não escreveste ´ . ` para iniciar o jogo")
