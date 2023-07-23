import datetime
if __name__ == '__main__':
    DNasc=input("Digite a sua data de nascimento (dd/mm/aaaa) ")
    dia, mes, ano= map(int, DNasc.split('/'))
    DataNasc=datetime.date(ano, mes, dia)
    print ("Data de nacscimento:")
    print(DataNasc.strftime("%d-%m-%Y"))
    print (DataNasc.strftime("%m-%d-%y"))
    print(f"{DataNasc:%d/%m/%y}")