if __name__ =="__main__":
    mensagem="Bem-vindo ao Python!\n"
    print (f"{mensagem:>50}")
    print (f"{mensagem:^50}")
    print (f"{mensagem:<50}")


if __name__ == '__main__':
    mensagem="Bem-vindo ao Python!\n"
    print(f"{mensagem}".rjust(50))
    print(f"{mensagem}".center(50))
    print(f"{mensagem}".ljust(50))
