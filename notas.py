from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io
import re
import pandas as pd
import os


files_pdf = [f for f in os.listdir('.') if f.endswith('.pdf')]

columns = ['Data',
'Venda disponível',
'Compra disponível',
'Venda Opções',
'Compra Opções',
'Valor dos negócios',
'IRRF',
'IRRF Day Trade (proj.)',
'Taxa operacional',
'Taxa registro BMF',
'Taxas BMF (emol+f.gar)',
'Outros Custos',
'Impostos',
'Ajuste de posição',
'Ajuste day trade',
'Total de custos operacionais',
'Outros',
'IRRF operacional',
'Total Conta Investimento',
'Total Conta Normal',
'Total liquido',
'Total líquido da nota']

pos_credebt = [4,9,13,14,18,19,20]


df = pd.DataFrame(columns = columns)


for pdf in files_pdf:

    print('Arquivo: {}'.format(pdf[-12:-4]))
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf, 'rb') as fh:

        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()


    possible_tables = [m.start() for m in re.finditer('Venda disponívelCompra', text)]
    possible_tables_end = [m.start() for m in re.finditer('\+Custos BM&F', text)]

    for start,end in zip(possible_tables, possible_tables_end):
        current_text = text[start:end]
        regex_values = re.compile(r'\d+,\d\d|\d\.\d+,\d\d')
        values = regex_values.findall(current_text)
        values = [float(f.replace('.','').replace(',','.')) for f in values]
        regex_creditdebt = re.compile(r'\| [CD]')
        creditdebt = regex_creditdebt.findall(current_text)

        if values:
            for i,pos_cd in enumerate(pos_credebt):
                values[pos_cd] = values[pos_cd]*(-1) if creditdebt[i].endswith('D') else values[pos_cd]

            print(values)

            df.loc[len(df)] = [pdf[-12:-4]] + values

df['Data'] = pd.to_datetime(df.Data).dt.date
df.to_excel('NotasDeNegociacao.xlsx')

df_grouped = df.groupby([pd.to_datetime(df.Data).dt.month, pd.to_datetime(df.Data).dt.year]).sum()
df_grouped.to_excel('NotasMes.xlsx')
        #if values:
        #    print(values)

