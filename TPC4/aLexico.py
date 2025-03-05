import sys
import re

def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, "r", encoding="utf-8") as f:       # módulo para ler um ficheiro como input
        return f.read().strip().split('\n')
    
def analizadorLexico(file):

    token_spec = [
        ('COMMENT', r'^#.*'),              # Comentários começados com #
        ('NUM', r'\d+'),                    # Números, por exemplo: 1000
        ('BRACES', r'[{}]'),                # { e }
        ('DOISPONTOS', r':'),               # :     
        ('PREFX', r'\w+(?=:)'),             # Prefixo como dbo:       
        ('SUFX', r'(?<=:)\w+'),             # Sufixo como :name
        ('VAR', r'\?[\w]+'),                 # Variáveis começadas com ?
        ('STRING', r'"[^"]*"'),             # Strings
        ('KEYWORD', r'[a-zA-Z]+\b'),        # Operadores de SQL
        ('AT', r'@[a-zA-Z]+'),              # @palavra
        ('ENDPOINT', r'\.'),                # Pontos finais das linnhas
        ('SKIP', r'[\s\t]+'),               # Passar espaços à frente
        ('ERRO', r'.+')                      # Tudo que caia fora desta sintaxe
    ]

    token_regex = '|'.join([f'(?P<{id}>{expreg})' for (id,expreg) in token_spec])
    reconhecidos = []
    linha = 1

    mo = re.finditer(token_regex, file)
    for m in mo:

        dict = m.groupdict()

        if dict['COMMENT']:
            t = ('COMMENT', dict['COMMENT'], linha, m.span())
        elif dict['NUM']:
            t = ('NUM', int(dict['NUM']), linha, m.span())
        elif dict['BRACES']:
            t = ('BRACES', dict['BRACES'], linha, m.span())
        elif dict['DOISPONTOS']:
            t = ('DOISPONTOS', dict['DOISPONTOS'], linha, m.span())
        elif dict['SUFX']:
            t = ('SUFX', dict['SUFX'], linha, m.span())
        elif dict['PREFX']:
            t = ('PREFX', dict['PREFX'], linha, m.span())
        elif dict['VAR']:
            t = ('VAR', dict['VAR'], linha, m.span())
        elif dict['STRING']:
            t = ('STRING', dict['STRING'], linha, m.span())
        elif dict['KEYWORD']:
            t = ('KEYWORD', dict['KEYWORD'], linha, m.span())
        elif dict['AT']:
            t = ('AT', dict['AT'], linha, m.span())
        elif dict['ENDPOINT']:
            t = ('ENDPOINT', dict['ENDPOINT'], linha, m.span())
        elif dict['SKIP']:
            pass
        else:
            t = ('ERRO', m.group(), linha, m.span())
        
        if not dict['SKIP']: reconhecidos.append(t)

    return reconhecidos
        

def main():

    file = ler_ficheiro("input.txt")
    content = analizadorLexico("\n".join(file))

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(str(t) for t in content))

if __name__ == "__main__":
    main()