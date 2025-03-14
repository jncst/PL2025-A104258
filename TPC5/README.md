# TPC5 - Máquina de Vending
### 2025-03-14

### João Andrade Costa, A104258
<img src="https://github.com/user-attachments/assets/afe8f9d7-90b8-4331-81e3-0b0aaac8c56e" alt="imagem" width="400" />

## Resumo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A tarefa proposta foi a implementação de uma máquina de vending que simula a interação com o utilizador através de comandos. O programa carrega o stock de produtos a partir de um ficheiro JSON, processa comandos (como LISTAR, MOEDA, SELECIONAR e SAIR) e, ao terminar, atualiza o ficheiro com o stock atualizado. O saldo inserido pelo utilizador é manipulado em cêntimos, garantindo cálculos precisos e a exibição correta dos valores.

### Leitura
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Para a implementação deste programa, foi criado o ficheiro [vending.py](vending.py). Este ficheiro contém funções para carregar o stock de produtos (armazenados em [stock.json](stock.json)), listar os produtos, processar a inserção de moedas, permitir a seleção de um produto e finalizar a sessão salvando o stock atualizado.

## Funcionamento
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ao iniciar, o programa carrega o stock de produtos do ficheiro JSON e inicializa um saldo global (em cêntimos) com o valor 0. Em seguida, o programa entra num ciclo onde aguarda comandos do utilizador. Cada comando é interpretado e processado, atualizando o saldo ou o stock conforme necessário. Para além disso, o programa tem deteção para comandos não escritos em maiúsculas e para comandos não reconhecidos

### Comandos Aceitos
- **LISTAR:** Exibe o stock atual de produtos, mostrando o código, nome, quantidade e preço.
- **MOEDA:** Permite inserir moedas no formato, por exemplo, `1e, 20c, 5c, 5c.`. Os valores são convertidos para cêntimos e somados ao saldo global.
- **SELECIONAR:** Permite selecionar um produto através do seu código. O programa verifica se o saldo é suficiente para a compra, atualiza o stock (decrementando a quantidade) e deduz o valor do produto do saldo.
- **SAIR:** Finaliza a sessão, salva o stock atualizado no ficheiro JSON e encerra o programa.

### Detalhes do Código
- **Carregar Stock:**  
  A função responsável por carregar o stock (`carregar`) lê o ficheiro [stock.json](stock.json) e armazena os dados numa variável global. Se o ficheiro existir e estiver formatado corretamente, os produtos serão carregados para uso no programa.

- **Listar Produtos:**  
  A função `listar` apresenta, no ecrã, os produtos do stock num formato tabular. Cada produto é exibido com o seu código, nome, quantidade e preço, facilitando a consulta pelo utilizador.

- **Formatação de Saldo:**  
  A função `coindisplay` converte o saldo, armazenado em cêntimos, para uma representação mais legível (por exemplo, "1e30c" para 130 cêntimos). Esta função é utilizada sempre que o saldo é exibido ao utilizador.

- **Processamento de Moedas:**  
  A função `moeda` processa a string de moedas inserida pelo utilizador, que pode conter valores em euros (terminados por "e") ou cêntimos (terminados por "c"). Cada valor é convertido para cêntimos e somado à variável global `total`.  

- **Seleção de Produtos:**  
  A função `selecionar` recebe o código do produto pretendido e verifica, para cada produto, se o saldo é suficiente para a compra. Se o saldo for adequado, o produto é dispensado (a quantidade é decrementada) e o preço é deduzido do saldo. Caso contrário, é informado ao utilizador que o saldo é insuficiente e o valor necessário é exibido.

- **Finalização e Persistência:**  
  Ao receber o comando `SAIR`, a função `sair` guarda o stock atualizado de volta no ficheiro [stock.json](stock.json) e o programa é finalizado. Desta forma, o estado da máquina é mantido entre as execuções.

### Exemplo de Interação
```
>> LISTAR
maq:
cod  |  nome  |  quantidade  |  preço
-------------------------------------
A23  água 0.5L  8  0.7
B11  refrigerante 0.5L  5  1.6
C05  sumo 0.33L  10  1.1
>> MOEDA 1e, 20c, 5c, 5c.
Saldo = 1e30c
>> SELECIONAR A23
Pode retirar o produto dispensado "água 0.5L".
Saldo = 60c
>> SELECIONAR A23
Saldo insuficiente para satisfazer o seu pedido.
Saldo = 60c; Pedido = 70c.
>> SAIR
```