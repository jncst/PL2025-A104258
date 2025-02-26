import re

def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:       # módulo para ler um ficheiro como input
        return f.read().strip().split('\n')

def convertHeader(file):        # conversor de cabeçalhos

    newText = []
    
    for linha in file:

        linha = re.sub(r'^(#{1,3}) (.+)$', lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', linha)

        newText.append(linha)
    
    return newText

def convertBoldandItalic(file):

    newText = []

    for linha in file:
        linha = re.sub(r'\*\*(.+)\*\*', r'<b>\1</b>', linha)
        linha = re.sub(r'\*(.+)\*', r'<i>\1</i>', linha)

        newText.append(linha)

    return newText

def convertList(file):

    inList = False
    newText = []

    for linha in file:

        match = re.match(r'^\s*(\d+)\.\s*(.+)$', linha)

        if match:
            if not inList:

                newText.append("<ol>")      # começar a lista
                inList = True

                newText.append(f"<li>{match.group(2)}</li>")
            
            else:
                newText.append(f"<li>{match.group(2)}</li>")       # adiciona se ja tivermos numa lista
        else:
            if inList:
                newText.append("</ol>")
                inList = False          # acabaram os elementos da lista
            newText.append(linha)       # meter as cenas do texto normais

    return '\n'.join(newText)

def convertLink(file):

    newText = []

    for linha in file:

        linha = re.sub(r'\[(.+?)\]\s*\((.+?)\)', r'<a href="\2">\1</a>', linha)

        newText.append(linha)

    return newText

def convertImage(file):

    newText = []

    for linha in file:

        linha = re.sub(r'!\[(.+?)\]\s*\((.+?)\)', r'<img src="\2" alt="\1"/>', linha)

        newText.append(linha)

    return newText

def main():
    file = ler_ficheiro("input.md")

    file = convertHeader(file)
    file = convertBoldandItalic(file)
    file = convertList(file)
    file = convertLink(file)
    file = convertImage(file)

    with open("output.html", "w", encoding="utf-8") as f:
        f.write('\n'.join(file))

if __name__ == "__main__":
    main()