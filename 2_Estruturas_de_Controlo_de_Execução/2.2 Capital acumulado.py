import math
if __name__ == '__main__':
    X, I, N=1000, 0.01, 2
    Capacum=X*math.pow((1+I),N)
    print(f"{X:5.2f}€ capitalizados durante {N} anos à taxa anual de {I: 4.1%} resultam em {Capacum:7.2f}€")