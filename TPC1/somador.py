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
            with open("output.txt", "a", encoding="utf-8") as f:       # módulo para ler um ficheiro como input
                f.write(str(soma) + "\n")

        elif ligado and palavra.isdigit():
            soma += int(palavra)
        
def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:       # módulo para ler um ficheiro como input
        return f.read().strip()
    
if __name__ == "__main__":
    textof = ler_ficheiro("input.txt")      # especificamos o input para a função
    somador(textof)