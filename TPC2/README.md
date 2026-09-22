inicio= input("Olá jogador vamos jogar ao jogo ´adivinha o número`, eu ja pensei no meu número entre 0 e 100! Podes tentar adivinhar respondendo apenas com um número inteiro. Boa sorte! Escreve: ´ . ` ,para começar o jogo")
if inicio== ".":
    n= int(input("adivinha o número:"))
    while n!=23:
        if n>23:
            n= int(input("o número que pensei é menor, tenta novamente:"))
        elif n<23:
            n= int(input("o número que pensei é maior, tenta novamente:"))
    print("Acertou!")
else:
    print("Erro! Não escreveste ´ . ` para iniciar o jogo")
