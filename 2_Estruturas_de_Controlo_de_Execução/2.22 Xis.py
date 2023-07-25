if __name__=='__main__':
    Carat, Ponto, Dimensao="X", ".", 10
    for Linha in range(1, Dimensao+1):
        for Coluna in range(1, Dimensao+1):
            if Linha==Coluna or Coluna==Dimensao-Linha+1:
                print(Carat, end="")
            else:
                print(Ponto, end="")
        print()