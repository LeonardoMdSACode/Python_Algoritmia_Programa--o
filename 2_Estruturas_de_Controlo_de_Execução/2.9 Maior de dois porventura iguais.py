if __name__=='__main__':
    A=float(input("Digite o primeiro número: "))
    B=float(input("Digite o segundo número: "))
    if (A>B):
        print(f"{A} é o maior.")
    elif B>A:
        print(f"{B} é o maior.")
    else:
        print("Os dois números são iguais.")