import datetime
if __name__ == '__main__':
    DataCorrente=datetime.datetime.today()
    print("Data corrente", datetime.date.today().strftime("%d-%m-%y"))
    print(DataCorrente.strftime("%d-%m-%Y %H:%M:%S"))
    print(DataCorrente.strftime("%m-%d-%y %H:%M:%S"))
    print(DataCorrente.strftime("%d/%m/%y"))
    print(DataCorrente.strftime("%H:%M:%S"))