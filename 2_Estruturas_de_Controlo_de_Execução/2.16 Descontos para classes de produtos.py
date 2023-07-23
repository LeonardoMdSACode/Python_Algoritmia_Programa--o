if __name__=='__main__':
    Desconto={
        "VEG":0.15,
        "LAT":0.10,
        "CER":0.10,
        "AGU":0.10,
    }
    CProd=input("Três primeiras letras da classe do produto? ".upper())
    print(f"Os produtos de classe {CProd:3} têm {Desconto.get(CProd,0.01):2.0%} de desconto")