import math
if __name__=='__main__':
    A=float(input("Digite o coef. de x^2: "))
    B=float(input("Digite o coef. de x: "))
    C=float(input("Digite o termo independente: "))
    Disc=math.pow(B,2)-4*A*C
    if Disc>0:
        print(f"x1={(-B+math.sqrt(Disc))/(2*A):5.2f}")
        print(f"x2={(-B-math.sqrt(Disc))/(2*A):5.2f}")
    elif (Disc==0):
        print(f"x1=x2 {-B/(2*A):5.2f}\n")
    else:
        print("Raízes imaginárias")