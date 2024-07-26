import pandas as pd
import os
import json

def ler_arquivo_codigos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]

pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'
pasta_pep = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\pepLer'
nomes = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\nomes.txt'

peps = os.listdir(pasta_pep)
arquivos_planilhas = os.listdir(pasta_planilhas)

pep_desejado = os.path.join(pasta_pep, peps[0])
arquivo_desejado = arquivos_planilhas[0]

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        

df =  pd.read_excel(os.path.join(pasta_planilhas, arquivo_desejado))

coisa = []


for index, row in df.iterrows():
        if row.iloc[2] == "Dermonecrotic":
            with open(pep_desejado, 'r')as file:
                conteudo = file.read()

            inicio = conteudo.find(row.iloc[0])
            fim = conteudo.find(">", inicio)

            if inicio != -1 and fim != -1:
                substring = conteudo[inicio:fim]
                coisa.append({
                    "conteudo": substring
                })
                # with open(arquivo_output, 'a')as file: 
                #     file.write(substring)
    
        
save_to_json(coisa, ler_arquivo_codigos(nomes)[0] + ".json")



