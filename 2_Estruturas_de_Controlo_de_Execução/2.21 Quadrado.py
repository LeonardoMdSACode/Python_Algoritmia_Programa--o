if __name__=='__main__':
    Carat1, Carat2, N='X', 'o', 6
    for I in range(1, N+1):
        for J in range(1+N+1):
            if (I+J)%2 == 0:
                print(Carat1, end="")
            else:
                print(Carat2, end="")
        print()