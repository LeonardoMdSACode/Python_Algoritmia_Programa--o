if __name__ == '__main__':
    Aumento=20
    D1=float(input("Digite a despesa do primeiro dia: "))
    D2=D1*(1+Aumento/100)
    D3=D2*(1+Aumento/100)
    D4=D3*(1+Aumento/100)
    Dmed=(D1+D2+D3+D4)/4
    print(f"Despesa média diária {Dmed:3.2f} €")