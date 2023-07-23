if __name__=='__main__':
    while True:
        A=int(input("Limite inferior "))
        B=int(input("Limite superior "))
        if A<B:
            break
    if A%2==0:
        A+=1
    for Impar in range (A,B+1,2):
        print(Impar)