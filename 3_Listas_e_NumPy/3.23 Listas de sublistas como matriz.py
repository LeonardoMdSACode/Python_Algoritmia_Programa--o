if __name__=='__main__':
    L=[[10,50,30],[1,20,67],[10,2,8],[12,25,66],[15,20,45],[13,22,67]]
    print (f"Matriz ({len(L)}x{len(L[0])}):")
    for I in range (0, len(L)):
        for J in range (0, len(L[0])):
            print(f"{L[I][J]:3d}\t", end="")
        print()