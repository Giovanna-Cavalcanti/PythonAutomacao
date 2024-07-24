import pandas as pd
import os

pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'

arquivos = os.listdir(pasta_planilhas)

for planilha in arquivos:
    caminho_arquivo = os.path.join(pasta_planilhas, planilha)
    
    df = pd.read_excel(caminho_arquivo)
    
    # Verificar e imprimir os valores da primeira coluna onde a terceira coluna é "Dermonecrotic"
    for index, row in df.iterrows():
        if row.iloc[2] == "Dermonecrotic":
            print(f"Arquivo: {planilha}, Valor: {row.iloc[0]}")