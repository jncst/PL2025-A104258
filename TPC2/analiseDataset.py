import re

def ler_dataset(file_name):

    with open(file_name, "r", encoding="utf-8-sig") as f:       # ler apenas para leitura
        linhas = f.read()
    
        # Expressão regular para dividir linhas, ignorando newlines dentro de aspas
    padrao_linhas = r'\n(?=(?:[^"]*"[^"]*")*[^"]*$)'
    linhas = re.split(padrao_linhas, linhas)        # Divide o conteúdo em linhas corretamente

    dados = []

        # Expressão regular para dividir corretamente
    padrao = r';(?=(?:[^"]*"[^"]*")*[^"]*$)'

    for linha in linhas[1:]:

        campos = re.split(padrao, linha)
        campos = [campo.strip('"') for campo in campos]

        if len(campos) == 7:
            nome, _, _, periodo, compositor, _, _ = campos
            dados.append((nome, periodo, compositor))
    
    return dados

def processar_dados(dados):

    compositores = set()        # sets são ordenados
    distPeriodo = {}    # n obras por período
    obrasPeriodo = {}   # periodo e set alfabético das obras

    for linha in dados:

        nome, periodo, compositor = linha

        compositores.add(compositor)        # adicionar compositor à lista

        if periodo not in distPeriodo:      # meter o nr de obras na distribuição de períodos
            distPeriodo[periodo] = 0
            obrasPeriodo[periodo] = []      # como tem 0 entradas, também iniciamos este com 0 entradas

        distPeriodo[periodo] += 1
        obrasPeriodo[periodo].append(nome)
        
    return sorted(compositores), distPeriodo, {period: sorted(obras) for period, obras in obrasPeriodo.items()}
        #ordena tudo, as obras do dicionario tambem são ordenadas, items() percorre os pares chave,valor

def escrever_resultados(compositores, distPeriodo, obrasPeriodo):

    with open("output.txt", "w", encoding="utf-8") as f:       # módulo para ler um ficheiro como input

        f.write("Lista ordenada de compositores:\n")
        f.write("\n".join(compositores) + "\n\n")

        f.write("Distribuição das obras por período:\n")
        for periodo,nobras in distPeriodo.items():
            f.write(periodo + ": " + str(nobras) + "\n")
        f.write("\n")

        f.write("Obras por período:\n")
        for periodo, obras in obrasPeriodo.items():
            f.write(periodo + ": " + "\n".join(obras) + "\n")

def main():

    file_name = "obras.csv"
    dados = ler_dataset(file_name)
    compositores, distPeriodo, obrasPeriodo = processar_dados(dados)
    escrever_resultados(compositores, distPeriodo, obrasPeriodo)

if __name__ == "__main__":
    main()