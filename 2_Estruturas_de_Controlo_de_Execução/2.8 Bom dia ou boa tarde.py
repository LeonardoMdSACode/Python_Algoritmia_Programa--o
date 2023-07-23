import datetime
if __name__=='__main__':
    Meiodia=12
    Msg="Bom dia!"
    HoraCorrente=datetime.datetime.now().hour
    if HoraCorrente>Meiodia:
        Msg="Boa tarde!"
    print(Msg)