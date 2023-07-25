if __name__=='__main__':
    Espaco, Larg, Comp, Carat=" ",5,10,"X"
    for C in range(Comp):
        print(Carat, end="")
    print()
    for L in range(Larg-2):
        print(Carat, end="")
        for W in range (2, Comp):
            print(Espaco, end="")
        print(Carat)
    for C in range(Comp):
        print(Carat, end="")
    print()

    # Ou
    # if __name__=='__main__':
    #     Espaco, Larg, Comp, Carat=" ", 5, 10, "X"~
    #     L="X"+(Comp-2)*(Espaco)+"X\n"
    #     R=Comp*"X"+"\n"+((Larg-1)*L)+Comp*("X")
    #     print(R)