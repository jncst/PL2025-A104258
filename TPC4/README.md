# TPC4 - Analisador Léxico
### 2025-03-05

### João Andrade Costa, A104258
<img src =https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A tarefa proposta foi a implementação de um analisador léxico que processa um ficheiro de texto e identifica diferentes tipos de tokens, como variáveis, números, operadores SQL, sufixos e prefixos, entre outros. O objetivo é construir um analisador que possa identificar e categorizar os diferentes elementos presentes no ficheiro de entrada.

### Leitura
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Para a implementação do programa, foi criado o ficheiro [analisador_lexico.py](analisador_lexico.py), que primeiro lê um ficheiro de texto (por exemplo, [input.txt](input.txt)) utilizando o método `ler_ficheiro()`. O conteúdo do ficheiro é lido e dividido em linhas, removendo espaços desnecessários através do método *.strip().split('\n')*.

## Análise Lexical
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A análise léxical é realizada através da função `analizadorLexico()`, que utiliza expressões regulares para identificar os diferentes tipos de tokens. A função utiliza uma lista de especificações de token, cada uma com uma expressão regular correspondente, para identificar e classificar as palavras no ficheiro de entrada.

### Tipos de Tokens Identificados:
- **Comentário:** Identifica as linhas que começam com `#`.
- **Números:** Identifica sequências de dígitos.
- **Chavetas (`{` e `}`):** Identifica chaves usadas na sintaxe.
- **Prefixos:** Identifica prefixos como `dbo:`.
- **Sufixos:** Identifica sufixos como `:name`.
- **Variáveis:** Identifica variáveis que começam com `?`.
- **Strings:** Identifica texto entre aspas duplas.
- **Palavras-chave:** Identifica operadores ou palavras-chave como `select`, `where`, etc.
- **Links:** Identifica `@palavra` para links ou referências.
- **Fim de linha:** Identifica os pontos finais de uma linha com `.`.

### Resultados
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após a análise, os tokens identificados são gravados num ficheiro de saída (neste caso, [output.txt](output.txt)). Cada token é representado por uma tupla contendo o tipo do token, o valor identificado, o número da linha e o intervalo de caracteres onde o token foi encontrado. O resultado final é guardado utilizando a instrução `with open("output.txt", "w", encoding="utf-8") as f:`, garantindo que todos os caracteres especiais sejam corretamente processados.

### Exemplo de Entrada
```txt
# Comentário no início
dbo:MusicalArtist ?nome ?desc
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
}
```

### Exemplo de Saída
```txt
('COMMENT', '# DBPedia: obras de Chuck Berry', 1, (0, 31))
('KEYWORD', 'select', 1, (33, 39))
('VAR', '?nome', 1, (40, 45))
('VAR', '?desc', 1, (46, 51))
('KEYWORD', 'where', 1, (52, 57))
('BRACES', '{', 1, (58, 59))
('VAR', '?s', 1, (64, 66))
('KEYWORD', 'a', 1, (67, 68))
('PREFX', 'dbo', 1, (69, 72))
('DOISPONTOS', ':', 1, (72, 73))
('SUFX', 'MusicalArtist', 1, (73, 86))
('ENDPOINT', '.', 1, (86, 87))
...
```