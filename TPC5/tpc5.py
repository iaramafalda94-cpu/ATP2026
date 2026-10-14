def guardarturma(turma, fnome):
    file = open(fnome,"w")
    for aluno in turma:
        nome,id,notas= aluno
        file.write(f"{nome}#{id}#{notas[0]}#{notas[1]}#{notas[2]}|")
    file.write("\n")
    file.close()

def carregarturma(fnome):
    turma = []
    file = open(fnome,"r")
    for line in file:
        aluno= line.split("|")
        for e in aluno[:-1]:
            nome,id,nota1,nota2,nota3= e.split("#")
            notas=[float(nota1),float(nota2),float(nota3)]
            aluno=(nome,id,notas)
        turma.append(aluno)
    file.close()
    return turma

def menu():
    opcao=-1
    turma=[]
    while opcao!=0:
        print("""MENU: 
        1: Criar uma turma;
        2: Inserir um aluno na turma;
        3: Listar a turma;
        4: Consultar um aluno por Id;
        8: Guardar a turma em ficheiro;
        9: Carregar uma turma dum ficheiro;
        0: Sair da aplicação 
        """)
        opcao=int(input("escolha uma opção: "))
        
        if opcao ==1:
            turma=[]
            n=1
            while n<=5:
                notas=[]
                nome=input(f"escreva o nome do aluno {n}: ")
                id=input(f"escreva o id do aluno {n}: ")
                nota1=float(input(f"escreva a nota 1 do aluno {n}: "))
                nota2=float(input(f"escreva a nota 2 do aluno {n}: "))
                nota3=float(input(f"escreva a nota 3 do aluno {n}: "))
                notas = [nota1, nota2, nota3]
                aluno=(nome,id,notas)
                turma.append(aluno)
                n=n+1
            print(turma)
        
        elif opcao==2:
            notas=[]
            nome=input("insira o nome do aluno: ")
            id=input("insira o id do aluno: ")
            nota1=float(input("escreva a nota 1 do aluno:  "))
            nota2=float(input("escreva a nota 2 do aluno:  "))
            nota3=float(input("escreva a nota 3 do aluno:  "))
            notas = [nota1, nota2, nota3]
            aluno=(nome,id,notas)
            turma.append(aluno)
            print(turma)

        elif opcao==3:
            if turma==[]:
                print("a turma esta vazia")
            else:
                print("lista de alunos:")
                for aluno in turma:
                    nome,id,notas=aluno
                    print(f"nome: {nome}, id: {id}, notas: {notas}")
        
        elif opcao==4:
            id1=input("qual o id do aluno que quer consultar? ")
            for aluno in turma:
                if aluno[1]==id1:
                    print("o aluno é: ", aluno[0])
                else:
                    print("esse aluno nao esta presente na lista ")
        
        elif opcao==8:
            guardarturma(turma,"turma.txt")
            print("turma guardada em turma.txt")

        elif opcao==9:
            carregarturma("turma.txt")
            print("turma carregada:", turma)

            
        elif opcao==0:
            print("a aplicação terminou")
    return turma
print(menu())