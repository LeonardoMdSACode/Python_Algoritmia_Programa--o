if __name__ == '__main__':
    A=float(input("Digite o primeiro número: "))
    B=float(input("Digite o segundo número: "))
    if A>B :
        Maior=A
    else:
        Maior=B
    print(f"{Maior:1.3f} é o maior dos dois números: {A:1.3f} e {B:1.3f}")