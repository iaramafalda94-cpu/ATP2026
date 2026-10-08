# TPC4: Aplicação para manipulação de listas de inteiros
# # Autor: 
Iara Gonçalves;
114372; 
Foto:<img width="1206" height="903" alt="image" src="https://github.com/user-attachments/assets/7de1be52-e4cf-490d-8a4c-09af65c99228" />

## Resumo: O trabalho de casa dado na quarta aula da teórica e prática tem como intuito criar um programa em python para uma aplicação de manipulação de números reais, em que o programa exibe um menu com várias opções e o utilizador deve selecionar a opção que pretender tendo em conta a manipulação que quer fazer nos números presentes na lista.

# Código:
import random
def menu():
    opcao=-1
    lista=[]
    while opcao!=0:
        print("""MENU: 
        (1) Criar Lista 
        (2) Ler Lista 
        (3) Soma
        (4) Média
        (5) Maior
        (6) Menor
        (7) estaOrdenada por ordem crescente
        (8) estaOrdenada por ordem decrescente
        (9) Procura um elemento
        (0) Sair 
        """)
        opcao=int(input("escolha uma opção: "))
        
        if opcao ==1:
            n=int(input("escolha o tamanho da lista: "))
            lista= [random.randint(1,100) for i in range(n)]    
            print("Lista criada:", lista)
            
            
        elif opcao==2:
            lista=[]
            num=int(input("quantos numeros quer inserir na lista?"))
            for i in range(num):
                valor=int(input(f"escreva o numero {i+1}:"))
                lista.append(valor)
            print("Lista lida:",lista)
        
        elif opcao==3:
            soma=0
            for i in lista:
                soma=soma+i
            print("a soma é:", soma)
        
        elif opcao==4:
            soma=0
            total=0
            for i in lista:
                total=total + 1
                soma=soma + i
            print("a média é:",soma/total)
        
        elif opcao==5:
            maior=lista[0]
            for i in lista:
                if i>maior:
                    maior=i
            print("o maior é:", maior) 

        elif opcao==6:
            menor=lista[0]
            for i in lista:
                if i<menor:
                    menor=i
            print("o menor é:", menor)
        
        elif opcao == 7:
            ordenado = True
            for i in range(len(lista)-1):
                if lista[i] > lista[i+1]:
                    ordenado = False

            if ordenado:
                print("Sim")
            else:
                print("Não")
        
        elif opcao==8:
            ordenado = True
            for i in range(len(lista)-1):
                if lista[i] < lista[i+1]:
                    ordenado = False

            if ordenado:
                print("Sim")
            else:
                print("Não")
        elif opcao==9:
            i = 0
            resposta = -1
            elem = int(input("escolha o numero que quer procurar: "))

            while i < len(lista):
                if lista[i] == elem:
                    resposta = i
                i = i + 1
            print(resposta)


            
        elif opcao==0:
            print("a aplicação terminou")
    return lista
print(menu())
