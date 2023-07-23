if __name__ == '__main__':
    E1, E2 = len("Porto"), "Lisboa "
    E3, E4 = "fica na Estremadura ", "coimbra".upper()
    E5 = "Maria Adelaide Carvalho"[6:15]
    E6, E7, E8 = "ABCD", "ABBCD", "ABCCD"
    E9, E10 = "Miguel Costa Porto", "  Bom dia  "#.strip(" ")
    print(E1)
    print(E2+E3)
    print(E4)
    print(E5)
    print(E6==E7)
    print(E7<E8)
    print(E9.find("Porto", 1, len(E9)))
    print(E10)