if __name__ == '__main__':
    Nome=input("Digite o nome do vendedor -> ")
    Sbase=float(input("Digite o salário-base ->"))
    C=float(input("Digite a comissão por cada carro vendido -> "))
    P=float(input("Digite a percentagem sobre o valor das vendas" + " (%) -> "))
    Ncarros=int(input("Digite o número de carros vendidos -> "))
    Vvendas=float(input("Digite o valor das vendas -> "))
    Sal = Sbase+Ncarros*C+Vvendas*P/100
    print(f"Salário a processar para {Nome} -> {Sal:7.2f} €")