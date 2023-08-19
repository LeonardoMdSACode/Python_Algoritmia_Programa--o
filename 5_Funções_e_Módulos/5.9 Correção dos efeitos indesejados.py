def Triplo():
    global N
    N*=3
    return N
def Dobro():
    global N
    N*=2
    return N
if __name__=='__main__':
    N=int(input("Digite um número "))
    Triplo()
    print(f"Triplo={N}")
    Dobro()
    print(f"Dobro do triplo = {N}")