import matplotlib.pyplot as plt
def medias(tabMeteo):  
    res = []
    for tuplo in tabMeteo:
        media= (tuplo[1] + tuplo[2])/2
        data= tuplo[0]
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):   
    file=open(fnome,"w")
    for data,tmin,tmax,p in t:
        ano,mes,dia=data
        file.write(f"{ano}-{mes}-{dia}#{tmin}#{tmax}#{p}| \n") 
    file.close()
    return

def carregaTabMeteo(fnome):    
    res = []
    file=open(fnome,"r")
    for line in file:
        x=line.split("|")
        for e in x[:-1]:
            data,tmin,tmax,p= e.split("#")
            ano,mes,dia=data.split("-")
        res.append(((int(ano),int(mes),int(dia)),float(tmin), float(tmax), float(p)))
    file.close()
    return res

def tempMin(tabMeteo):    
    res=0
    min=[]
    for t in tabMeteo:
        min.append(t[1])
    min.sort()
    res=min[0]
    return res

def amplTerm(tabMeteo):   
    res = []
    for tuplo in tabMeteo:
        amplitude= (tuplo[2] - tuplo[1])
        data= tuplo[0]
        res.append((data,amplitude))
    return res

def maxChuva(tabMeteo):    
    p_max=[]
    for t in tabMeteo:
        data=t[0]
        p_max.append(t[3])
        p_max.sort()
        max_prec= p_max[-1]
    return (data, max_prec)

def diasChuvosos(tabMeteo, p):    
    res=[]
    for e in tabMeteo:
        if e[3]>p:
            prec=e[3]
            data=e[0]
            res.append((data,prec))
    return res

def maxPeriodo(tabMeteo, p):    
    res=0
    for e in tabMeteo:
        if e[3]<p:
            res=res+1
        else:
            res=0
    return res

def grafTabMeteo(t):      
    y_min= [ tmin for data, tmin, *_ in t]    
    y_max= [ tmax for data, tmin, tmax, *_ in t]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    print(y_min)
    print(y_max)
    print(x)
    
    plt.plot(x,y_min, color="purple", marker="o", label="Temperatura minima em ºC")
    plt.plot(x,y_max, color="blue", marker="o", label="Temperatura maxima em ºC")
    plt.legend()
    plt.grid()
    plt.show()

    
    y= [p for data,tmin,tmax,p in t]
    x1 = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    print(y)
    print(x1)

    plt.plot(x1,y, color= "green", marker="o", label="Pluviosidade")
    plt.legend()
    plt.grid()
    plt.show()
    
    return

def menu():
    tabMeteo=[]
    n=int(input("Quantos dias pretende registar na tabela metereologica?"))
    for i in range(n):
        print(f"registo dia {i+1}:  ")
        ano=int(input("ano:  "))
        mes=int(input("mês:  "))
        dia=int(input("dia:  "))

        tmin=float(input("temperatura mínima:  "))
        tmax=float(input("temperatura máxima:  "))
        p=float(input("precipitação:  "))

        elemento=((ano,mes,dia), tmin, tmax, p)
        tabMeteo.append(elemento)
    print(tabMeteo)
    opcao=-1
    while opcao!=0:
        print("""MENU: 
        (1) Calcular a temperatura média de cada dia
        (2) Guardar uma tabela meteorológica num ficheiro de texto 
        (3) Carregar uma tabela meteorológica do ficheiro de texto
        (4) Calcular a temperatura mínima mais baixa registada na tabela
        (5) Calcular a amplitude térmica de cada dia
        (6) Calcular o dia em que a precipitação registada teve o seu valor máximo
        (7) Calcular os dias em que a precipitação ultrapassou um certo limite 
        (8) Calcular o número consecutivo de dias em que a precipitação foi inferior a um certo limite
        (9) Desenhar os gráficos de temperatura minima, máxima e pluviosidade
        (0) Sair 
        """)
        opcao=int(input("escolha uma opção: "))

        if opcao==1:
            medias(tabMeteo)
            print("medias:",medias(tabMeteo))

        elif opcao==2:
            guardaTabMeteo(tabMeteo, "tabMeteo.txt")
            print("Tabela guardada em tab.txt ")

        elif opcao==3:
            carregaTabMeteo("tabMeteo.txt")
            print("tabela carregada", tabMeteo)

        elif opcao==4:
            tempMin(tabMeteo)
            print("temperatura minima e respetivo dia: ", tempMin(tabMeteo))

        elif opcao==5:
            amplTerm(tabMeteo)
            print("amplitude termica de cada dia: ", amplTerm(tabMeteo))

        elif opcao==6:
            maxChuva(tabMeteo)
            print("precipitação maxina e respetivo dia: ", maxChuva(tabMeteo))

        elif opcao==7:
            p=float(input("escolha o limite de precipitação:  "))
            diasChuvosos(tabMeteo, p)
            print(f"a precipitação ultrapassou o limite {p} nos seguintes dias: ", diasChuvosos(tabMeteo,p))

        elif opcao==8:
            p=float(input("escolha o limite de precipitação:  "))
            maxPeriodo(tabMeteo, p)
            print(f"a precipitação foi inferior a {p} durante {maxPeriodo(tabMeteo,p)} dias consecutivos")

        elif opcao==9:
            grafTabMeteo(tabMeteo)
            print("graficos:  ",grafTabMeteo(tabMeteo))

        elif opcao==0:
            print("A aplicação terminou.")

    return tabMeteo
menu()