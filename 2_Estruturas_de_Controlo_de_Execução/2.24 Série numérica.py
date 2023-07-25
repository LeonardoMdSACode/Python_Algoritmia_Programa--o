if __name__=='__main__':
    Termos, P, Numerador, Denominador=95, 0, 1, 0
    for T in range (1, Termos+1):
        if T%2 ==0:
            Numerador+=2
        else:
            Denominador+=2
        P +=Numerador/Denominador
    print(f"Somatório dos {Termos} da série ={P:3.2f}")