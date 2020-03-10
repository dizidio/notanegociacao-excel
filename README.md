# Nota de Negociação (Day Trade) -> Excel

Conversão entre notas de negociação em PDF para uma tabela em Excel, evitando o preenchimento manual dos valores negociados em day trade.

**Atenção:** Testado apenas em notas de corretagem da Clear para negociações do tipo Day-Trade.

## Como utilizar
Inserir TODOS os PDFs das notas de negociação na mesma pasta do projeto e executar o arquivo *notas.py* com Python3.

```
python notas.py
```

## Pré-Requisitos

O script foi testado em Python 3.7.5 utilizando os seguintes pacotes

```
pdfminer3 (2018.12.03.0)
pandas (0.25.3)
```


## Saída

A saída consiste em dois arquivos do tipo XLSX:

```
NotasDeNegociacao.xlsx - contém informações sobre cada nota individual
NotasMes.xls - informações sobre o conjunto das notas dividido mensalmente
```


Cada arquivo possui as seguintes colunas, retiradas diretamente das Notas de Negociação:

* Venda disponível
* Compra disponível
* Venda Opções
* Compra Opções
* Valor dos negócios
* IRRF
* IRRF Day Trade (proj.)
* Taxa operacional
* Taxa registro BMF
* Taxas BMF (emol+f.gar)
* Outros Custos
* Impostos
* Ajuste de posição
* Ajuste day trade
* Total de custos operacionais
* Outros
* IRRF operacional
* Total Conta Investimento
* Total Conta Normal
* Total liquido
* Total líquido da nota


## TODO

* Permitir a utilização de Notas provenientes de outras corretoras.
* Compatibilidade com notas de outros tipos de operação (opções/swing-trade).

## Autor

* **Diogo Izidio**
