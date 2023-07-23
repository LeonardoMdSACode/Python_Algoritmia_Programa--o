if __name__=='__main__':
    LimApro, LimDist=10,16
    Nome=input("Nome do aluno: ")
    UC1=int(input("Nota de Programacção "))
    UC2=int(input("Nota de Matemática "))
    UC3=int(input("Nota de Sistema de Informação "))
    Situacao="Reprovado"
    if UC1>=LimApro and UC2>=LimApro and UC3>=LimApro:
        Situacao="Aprovado"
    if ((UC1>=LimDist and UC2>=LimDist and UC3>=LimApro) or
        (UC1>=LimDist and UC3>=LimDist and UC2>=LimApro) or
        (UC2>=LimDist and UC3>=LimDist and UC1>=LimApro)) :
        Situacao="Aprovado com distinção"
    print(f"{Nome} --- {Situacao}")