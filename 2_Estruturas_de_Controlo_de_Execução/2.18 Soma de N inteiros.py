if __name__=='__main__':
    Soma=0
    N=int(input("Limite superior do intervalo? "))
    for I in range(1,N+1,1):
        Soma+=I
    print(f"Total da adição dos {N:2d} inteiros positivos={Soma:3d}")