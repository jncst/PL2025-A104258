def somador(texto):
    ligado = True       # começamos com o comportamento ligado
    soma = 0

    palavras = texto.split()

    for palavra in palavras:
        palavra = palavra.lower()

        if palavra == "off":
            ligado = False
        elif palavra == "on":
            ligado = True
        elif palavra == "=":
            print(soma)

        elif ligado and palavra.isdigit():
            soma += int(palavra)
        
def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        return f.read().strip()
    
def main():
    textof = ler_ficheiro("input.txt")
    somador(textof)