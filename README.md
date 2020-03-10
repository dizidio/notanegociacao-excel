# Nota de Negociação (Day Trade) -> Excel

Conversão entre notas de negociação em PDF para uma tabela em Excel, evitando o preenchimento manual dos valores negociados em day trade.

**Atenção:** Testado apenas em notas de corretagem da Clear para negociações do tipo Day-Trade.

## Como utilizar
Inserir todos os PDFs das notas de negociação na mesma pasta do projeto e executar o arquivo *notas.py* com Python3.

```
python notas.py
```

### Prerequisites

O script foi testado em Python 3.7.5 utilizando os seguintes pacotes

```
pdfminer3 (2018.12.03.0)
pandas (0.25.3)
```

### TODO

* Permitir a utilização de Notas provenientes de outras corretoras.
* Compatibilidade com notas de outros tipos de operação (opções/swing-trade).

## Autor

* **Diogo Izidio**
