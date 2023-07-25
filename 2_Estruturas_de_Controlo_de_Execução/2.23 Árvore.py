# if __name__=='__main__':
#     C, Espaco="*", " "
#     A=int(input("Número de linhas da árvore "))
#     Impar=1
#     Inicio=int(((A-1)*2+1)/2)
#     for L in range (1, A+1):
#         for CEsp in range(1, Inicio+1):
#             print(Espaco, end="")
#         for CAste in range(1, Impar+1):
#             print(C, end="")
#         print()
#         Impar+=2
#         Inicio-=1

# Ou
if __name__=='__main__':
    C, Espaco="*", " "
    A = int(input("Número de linhas da árvore "))
    Impar=1
    Inicio=int(((A-1)*2+1)/2)
    for L in range (1, A+1):
        print(Inicio*Espaco, end="")
        print(Impar*C, end="")
        print()
        Impar+=2
        Inicio-=1