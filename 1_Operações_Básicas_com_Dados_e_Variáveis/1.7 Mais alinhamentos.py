if __name__ == '__main__':
    E1, E2=20, 15
    nome1, nome2, nome3="Ivo Gala", "Joana Silva", "Teresa Gomes"
    local1, local2, local3="Porto", "Lisboa", "Braga"
    print(f"{nome1:<{E1}} {local1:<{E2}}")
    print(f"{nome2:^{E1}} {local2:>{E2}}")
    print(f"{nome3} \t {local3}\n")