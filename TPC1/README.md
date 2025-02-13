# TPC1 - Somador On/Off
### 2025-02-13

### João Andrade Costa, A104258
<img src =https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A tarefa proposta foi de implementar um programa que some todas as sequências de dígitos que encontra num texto. Sempre que encontrar a string `Off` em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado; em oposição, sempre que encontra a string `On`, igualmente em qualquer combinação de maiúsculas e minúsculas, o comportamento é novamente ligado. Por fim, se encontrar o caracter `=`, o resultado da soma é colocado na saída.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para implementar o programa, foi criado o programa [somador.py](somador.py) que, primeiramente, abre um ficheiro de texto, neste caso o [input.txt](input.txt) para percorrer na sua execução. A função assume que o comportamento inicial para o somador está ligado, sendo armazenado um booleano iniciado com `True`, depois começa por separar o texto por espaços, usando o método *split()*. Em seguida percorre essa coleção de palavras e executa um pattern matching para ver se cada palavra é igual a "Off" ou "On" para desativar/ativar o comporamento. Caso não corresponda a nenhum dos dois, veerifica então se é "=", neste caso, imprime para a saída o contador que mantém com o total dos números, inicialmente declarado como 0. Caso uma palavra não for nenhuma dessas strings, verifica então se é um dígito com o método *isdigit()*, caso seja, e o comportamento de soma estiver ligado, então soma esta palavra (convertendo para int com *int(palavra)*) ao contador do total.

## Resultados
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quando o programa imprime para a saída, na verdade imprime para um ficheiro [output.txt](output.txt), sendo cada soma escrita na sua própria linha, com cada execução a adicionar ao conteúdo previamente presente no ficheiro (inicialmente vazio).