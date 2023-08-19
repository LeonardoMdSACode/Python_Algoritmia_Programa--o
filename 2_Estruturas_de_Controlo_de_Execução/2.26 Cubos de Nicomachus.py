if __name__=='__main__':
    Impar=1
    N=int(input("Limite superior do intervalo de inteiros "))
    for I in range (1, N+1):
        Cubo, Ts=0, ""
        for J in range(1, I+1):
            Cubo+=Impar
            Ts+="+"+str(Impar)
            Impar+=2
        print(f"{I} ao cubo={Ts}={Cubo}")