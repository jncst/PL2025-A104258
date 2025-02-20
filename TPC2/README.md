# TPC2 - Análise de um dataset de obras musicais
### 2025-02-20

### João Andrade Costa, A104258
<img src =https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A tarefa proposta foi de implementar um programa que lê um dataset de obras musicais num ficheiro csv, processá-lo e criar uma lista ordenada alfabeticamente dos compositores`, a distribuição das obras por período, e um dicionárioem que a cada período está associada uma lista alfabética dos títulos das obras desse período.

### Leitura
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para implementar o programa, foi criado o programa [analiseDataset.py](analiseDataset.py) que, primeiramente, abre um ficheiro csv [obras.csv](obras.csv) para leitura e em seguida usa uma expressão regular `r'\n(?=(?:[^"]*"[^"]*")*[^"]*$)'` para dividir corretamente as linhas, ignorando os caracteres *newline* dentro de aspas. Após isto, usa outra expressão regular: `r';(?=(?:[^"]*"[^"]*")*[^"]*$)'` para dividir as linhas com *re.split()*, em seguida, cada linha remove as aspas da descrição com *.strip('"')*, e por fim, apenas os campos de *nome*, *período*, e *compositor*, pois apenas esses vão ser necessários.

### Processamento
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Na função de processamento, primeiramente é criado um *set* para armazenar os compositores, um *dicionário* para a distribuição de obras por período, e outro *dicionário* do nome das obras por período. Percorrendo cada linha dos dados armazenados, a cada compositor adiciona ao *set* previamente criado, de seguida, verifica se o período já se encontra no respetivo dicionário, caso não esteja, no dicionário de ocorrências inicializa com 0 obras, e no outro, com uma lista de obras vazia. Depois, independentemente se o período já se encontrava registado ou não, adiciona uma ocorrência da obra e o nome desta aos respetivos dicionáarios.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No final, quando retorna o *set* e dicionários armazenados, primeiro ordena o *set* com *sorted()* e em seguida as obras do dicionário de obras por período com o mesmo método.

## Resultados
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A escrita de resultados é feita para o ficheiro [output.txt](output.txt), isto é realizado por uma função que o abre para escrita e recebe o *set* e os dicionários previamente criados e ordenados. De seguida, assinala cada alínea que está a escrever, primeiro com *"Lista ordenada de compositores:"* e depois os respetivos compositores, utilizando o método *join()*, colocando cada um numa nova linha. A distribuição de obras por período é assinalada com *"Distribuição das obras por período:"* e itera sobre os *items()* e escreve com a sintaxe `periodo: numero de obras`, novamente, cada item na sua linha. Por fim, as obras por período são apresentadas com *"Obras por período:"* e da mesma forma que a distribuição de obras por período foi feita, escreve para o ficheiro, utilizando também o método *join()* previamente mencionado para as obras de cada período.