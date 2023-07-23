if __name__=='__main__':
    A=float(input("Digite o primeiro número: "))
    B=float(input("Digite o segundo número: "))
    C=float(input("Digite o terceiro número: "))
    if A>B :
        if A>C :
            Maior=A
        else:
            Maior=C
    elif B>C:
        Maior=B
    else: 
       Maior=C
    print(f"{Maior:3.2f} é o maior de {A:3.2f}, {B:3.2f} e {C:3.2f}")