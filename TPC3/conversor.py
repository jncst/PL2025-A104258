import re

def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:       # módulo para ler um ficheiro como input
        return f.read().strip()

def convertHeader(file):        # conversor de cabeçalhos
    
    for linha in file:

        linha = re.sub(r'^(#{1,3}) (.+)$', lambda m: f'<h{len(m.group(1))}>\2</h{len(m.group(1))}>', linha)

def convertBoldandItalic(file):

    for linha in file:
        linha = re.sub(r'*(.+)*', r'<i>\1</i>')
        linha = re.sub(r'**(.+)**', r'<b>\1</b>')

def convertList(file):

    inList = False
    newText = []

    for linha in file:

        match = re.match(r'^\s*(d+)\.\s*(.+)$', linha)

        if match:
            if not inList:

                newText.append("<ol>")      # começar a lista
                inList = True

                newText.append("<li>\2</li>")
            
            else:
                newText.append("<li>\2</li>")       # adiciona se ja tivermos numa lista
        else:
            if inList:
                newText.append("</ol>")
                inList = False          # acabaram os elementos da lista
            newText.append(linha)       # meter as cenas do texto normais

        return '\n'.join(newText)
    