if __name__=='__main__':
    Fat=1
    N=int(input("Digite um inteiro positivo inferior a 32: "))
    for M in range (N, 1, -1):
        Fat*=M
    print(f"{N}!={Fat}")
