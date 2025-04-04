# listar, moeda, selecionar, sair
import json

total = 0
stock = []

def carregar(jason):

    global stock

    with open(jason, "r", encoding="utf-8") as f:
        stock = json.load(f)


def listar():                                  
    print("maq:")
    print("cod  |  nome  |  quantidade  |  preço")
    print("-------------------------------------")

    for prod in stock:
        print(f"{prod['cod']}  {prod['nome']}  {prod['quant']}  {prod['preco']}")

def coindisplay(moedas_cents):
    euros = moedas_cents // 100                     # divisão inteira do total
    cents = moedas_cents % 100                      # resto da divisão são os cêntimos

    if euros != 0:
        return(f"{euros}e{cents}c")
    else:
        return(f"{cents}c")



def moeda(moedas_str):

    global total                                    # diz ao programa que usamos a varaiável global

    moedas_str = moedas_str.strip().rstrip('.')     # remover os espaços e .
    moedas = moedas_str.split(',')                  # dividir pelas vírgulas

    for moed in moedas:
        
        moed = moed.strip()

        if moed.endswith("e"):
            valor = int(moed[:-1])                  # atribuir o valor até ao último elemento exclusive, vai ser o e ou c
            total += valor * 100                    # valor vai ser guardado em cêntimos 

        elif moed.endswith("c"):
            valor = int(moed[:-1])
            total += valor

    print(f"Saldo = {coindisplay(total)}")


def selecionar(cod):

    global stock
    global total

    for prod in stock:
        if prod["cod"] == cod:                      # passar à verificação do saldo
            if total / 100 > prod["preco"]:         # tem saldo
                prod["quant"] -= 1

                print(f"Pode retirar o produto dispensado {prod["nome"]}.")
                total -= prod["preco"] * 100

                print(f"Saldo = {coindisplay(total)}")

            else:                                   # não tem saldo
                print("Saldo insuficiente para satisfazer o seu pedido.")

                print(f"Saldo = {coindisplay(total)}; Pedido = {coindisplay(prod["preco"])}.")


def sair(jason):
    
    global stock

    with open(jason, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

def main():

    carregar("stock.json")                          # carregar o json é a primeira coisa a fazer

    while True:
        comando = input(">> ").strip()
        if not comando:
            continue

        cmd = comando.split()[0].upper()            # reconhecer os comandos mesmo quando estão em minúscula

        if cmd == "LISTAR":
            listar()

        elif cmd == "MOEDA":
                # Queremos a parte que contém as moedas
            moedas_str = comando[len("MOEDA"):].strip()
            moeda(moedas_str)
        
        elif cmd == "SELECIONAR":
            codigo = comando[len("SELECIONAR"):].strip()
            selecionar(codigo)

        elif cmd == "SAIR":
            sair("stock.json")
            break

        else:
            print("maq: Comando não reconhecido.")
        
if __name__ == "__main__":
    main()