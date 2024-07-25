import pandas as pd
import os

pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'
pasta_pep = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\pepLer'

peps = os.listdir(pasta_pep)

arquivos_planilhas = os.listdir(pasta_planilhas)

for planilha in arquivos_planilhas:
    caminho_arquivo = os.path.join(pasta_planilhas, planilha)
    
    df = pd.read_excel(caminho_arquivo)
    
    # Verificar e imprimir os valores da primeira coluna onde a terceira coluna é "Dermonecrotic"
    for index, row in df.iterrows():
        if row.iloc[2] == "Dermonecrotic":
            print(f"{planilha}, {row.iloc[0]}")
            
            