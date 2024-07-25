import pandas as pd
import os

pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'

pasta_pep = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\pepLer'

peps = os.listdir(pasta_pep)

arquivos = os.listdir(pasta_planilhas)

arquivo_desejado = arquivos[0]
pep_desejado = os.path.join(pasta_pep, peps[0])

df =  pd.read_excel(os.path.join(pasta_planilhas, arquivo_desejado))

print(pep_desejado)

for index, row in df.iterrows():
        if row.iloc[2] == "Dermonecrotic":
            with open(pep_desejado, 'r')as file:
                conteudo = file.read()

            inicio = conteudo.find(row.iloc[0])
            fim = conteudo.find(">", inicio)

            if inicio != -1 and fim != -1:
                substring = conteudo[inicio:fim]
                print(substring)
                
            # print(f"{row.iloc[0]}")
            


