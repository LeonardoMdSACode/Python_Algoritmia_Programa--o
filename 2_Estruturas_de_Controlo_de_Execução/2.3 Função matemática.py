import math
if __name__ == '__main__':
    X=float(input("Digite o valor de x="))
    Y=float(input("Digite o valor de Y="))
    F=(Y+math.sqrt(abs(2*X+10)))/(2*X)
    print(f"F({X:1.0f},{Y:1.0f})={F:6.3f}")