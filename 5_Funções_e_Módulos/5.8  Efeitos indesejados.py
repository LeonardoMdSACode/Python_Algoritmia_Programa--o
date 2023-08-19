def Triplo(N):
    N*=3
    return N
def Dobro(N):
    N*=2
    return N
if __name__=='__main__':
    N=int(input("Digite um número "))
    Triplo(N)
    print(f"Triplo={N}")
    Dobro(N)
    print(f"Dobro do triplo = {N}")