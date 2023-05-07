# Testbed TSCH RPC Client

Cliente para executar procedimentos remotamente por meio da API Testbed TSCH Data Analysis.

## 1. Modo de uso

* **-a | --addr**: Endereço da API.
* **-p | --port**: Porta da API.
* **-i | --intv**: Intervalo para execução periódica do procedimento remoto. Se o valor for **0**, o procedimento é executado apenas uma vez.
* **-r | --rpc**: Nome do procedimento remoto que será executado.
* **-g | --args**: Argumentos do procedimento remoto que será executado separados por vírgula.
* **-t | --testbed**: Nome do testbed cujos dados serão utilizados pelo procedimento remoto.

## 2. Lista de procedimentos remotos

### 2.1 Analyze

Realiza cálculos sobre os dados brutos do testbed, gerando novas informações que são gravadas no banco de dados.

#### 2.1.1 Argumentos

* **all**: Serão analisadas todas as informações disponíveis.

#### 2.1.2 Exemplo

```
./src/main.py -r analyze -g all -t testbed007
```
