# TPC6 - Recursivo Descendente para expressões aritméticas
### 2025-03-30

### João Andrade Costa, A104258
<img src="https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e" alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A tarefa proposta consistiu na implementação de um parser LL(1) recursivo descendente que reconhece e avalia expressões aritméticas, porém o parser utilizado é do tipo LR. O analisador léxico e sintático foram construídos utilizando a biblioteca PLY (Python Lex-Yacc), permitindo a interpretação de expressões envolvendo adição, subtração, multiplicação e divisão, com suporte para parêntesis para definir precedência de operações.

## Funcionamento
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; O programa é composto por duas partes principais: o analisador léxico([recursivodesc_lex.py](recursivodesc_lex.py)), que identifica os tokens presentes na expressão, e o analisador sintático, que constrói a árvore sintática e avalia o resultado da expressão fornecida pelo utilizador([recursivodesc_yacc.py](recursivodesc_yacc.py)).

### Tokens e Gramática
- **Tokens reconhecidos:**
  - Números inteiros positivos.
  - Operadores aritméticos: `+`, `-`, `*`, `/`.
  - Parêntesis `(` e `)`, para agrupar subexpressões.

- **Gramática utilizada:**
  - A gramática foi definida de forma a respeitar a precedência dos operadores, onde a multiplicação e divisão têm maior precedência que a adição e subtração.
  - O uso de recursão permite estruturar a avaliação das expressões de acordo com a hierarquia dos operadores.

### Modo de Operação
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; O utilizador introduz uma expressão aritmética, que é analisada e processada pelo parser. Caso a expressão seja válida, o seu resultado é calculado e exibido. Se houver erros, como caracteres inválidos ou expressões mal formadas, é apresentada uma mensagem de erro apropriada.

## Exemplo de Interação
```
>> 2+3
5
>> 67-(2+3*4)
53
>> (9-2)*(13-4)
63
```

## Conclusão
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Este trabalho permitiu aprofundar o conhecimento sobre análise sintática e a implementação de parsers utilizando uma abordagem recursiva descendente. A utilização de PLY mostrou-se eficaz na criação de analisadores léxicos e sintáticos em Python, facilitando a construção de linguagens simples baseadas em regras formais.