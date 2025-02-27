# TPC3 - Conversor de MarkDown para HTML
### 2025-02-27

### João Andrade Costa, A104258
<img src =https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A tarefa proposta foi a implementação de um programa que lê um ficheiro em formato Markdown, processa o seu conteúdo e converte-o para HTML, preservando a formatação dos elementos básicos especificados na sintaxe fundamental do Markdown.

### Leitura
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Para a implementação do programa, foi criado o ficheiro [conversor.py](conversor.py), que primeiramente lê um ficheiro Markdown [input.md](input.md) e divide o seu conteúdo por linhas, utilizando o método *.strip().split('\n')* para remover espaços desnecessários e garantir um processamento correto.

## Conversão
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A conversão do Markdown para HTML é realizada através de várias funções, cada uma responsável por transformar um tipo específico de elemento Markdown:

### Conversão de Cabeçalhos
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A função `convertHeader(file)` utiliza uma expressão regular `r'^(#{1,3}) (.+)$'` e *re.sub()* para substituir os cabeçalhos Markdown (`#`, `##`, `###`) por elementos HTML `<h1>`, `<h2>` e `<h3>`.

### Conversão de Negrito e Itálico
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A função `convertBoldandItalic(file)` substitui os textos entre `**` por `<b>` para negrito e os textos entre `*` por `<i>` para itálico, utilizando as expressões regulares `r'\*\*(.+)\*\*'` e `r'\*(.+)\*'`.

### Conversão de Listas Ordenadas
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A função `convertList(file)` verifica linhas que começam com um número seguido de um ponto (`1. item`), indicando uma lista ordenada. Se encontrar uma sequência de elementos de lista, envolve-os com as tags `<ol>` e `<li>`.

### Conversão de Links e Imagens
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A função `convertLinkandImage(file)` identifica e substitui links Markdown `[texto](url)` por `<a href="url">texto</a>` e imagens `![alt](src)` por `<img src="src" alt="alt"/>` através das expressões regulares `r'\[(.+?)\]\s*\((.+?)\)'` e `r'!\[(.+?)\]\s*\((.+?)\)'`, respetivamente.

## Resultados
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Após a conversão, o conteúdo processado é guardado no ficheiro [output.html](output.html) através do método *.join('\n')* para garantir que cada linha seja corretamente formatada. O ficheiro é então gravado utilizando *with open("output.html", "w", encoding="utf-8") as f:* para escrita com suporte a caracteres especiais.