if __name__=='__main__':
    Dias= {
        2:29,
        4:30,
        6:30,
        9:30,
        11:30
    }
    Mes=int(input("Número do mês "))
    print(f"O mês {Mes:2d} tem {Dias.get(Mes,31):2d} dias")