import random
def run():
    numero_aletorio = random.randint(1,100)
    numero_elejido = int(input("Ingresa un num: "))
    while numero_aletorio != numero_elejido:
        if numero_elejido < numero_aletorio:
            print("INGRESA UN NUMERO MAS ALTO: ")
        else:
            
            print("INGRESA UN NUMERO MAS BAJO")
        numero_elejido = int(input("Ingresa un num: "))
    print("-----GANASTE-----")

if __name__ == "__main__":
    run()