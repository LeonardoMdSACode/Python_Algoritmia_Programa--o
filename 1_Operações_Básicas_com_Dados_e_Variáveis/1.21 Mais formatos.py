import datetime
if __name__ == '__main__':
    N1, N2 = 45,46
    print(f"{N1:+05d}")
    print(str(-N1).zfill(7))
    print(N1, end=" "); print(N2)
    print(f"{N1:2d}\t{N2:04d} \n")
    print(f"{'Olá, mundo!':>20}")
    print(f"{'Olá, mundo!':*>20}")
    print(f"{'Olá, mundo!':^20}")
    print(f"{'Olá, mundo!':.4}")
    print("{:{NC}.{CD}f}".format(1.7182, NC=6, CD=2))
    print("{:%d/%m/%y %H:%M}".format(datetime.datetime(2018,10,5, 16, 10)))