from datetime import datetime, timedelta
if __name__ == "__main__":
    LuaCheia=input("Data da lua cheia após equinócio primavera (dd/mm/aaaa): ")
    LuaCheia=datetime.strptime(LuaCheia, "%d/%m/%Y")
    DiaSem=LuaCheia.weekday()
    QuintaFeiraSanta=LuaCheia+timedelta(days=3-DiaSem)
    DomPascoa=LuaCheia+timedelta(days=6-DiaSem)
    Ndom,Qua=6,40
    ParaTras=DomPascoa+timedelta(days=-Ndom-Qua)
    QuartaFeiraCinzas=ParaTras+timedelta(days=2-ParaTras.weekday())
    print(f"Início da Quaresma (Quarta-feira de Cinzas): {QuartaFeiraCinzas:%d/%m/%Y}")
    print(f"Fim da Quaresma (Quinta-feira Santa): {QuintaFeiraSanta: %d/%m/%Y}")
    print(f"Domingo de Páscoa:{DomPascoa: %d/%m/%Y}")