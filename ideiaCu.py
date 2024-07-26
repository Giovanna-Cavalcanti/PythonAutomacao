import pandas as pd
import os
import json

def ler_arquivo_codigos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'
pasta_pep = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\pepLer'
nomes = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\nomes.txt'
indice = 0

peps = os.listdir(pasta_pep)
arquivos_planilhas = os.listdir(pasta_planilhas)

nomes_arquivos = ler_arquivo_codigos(nomes)

coisa = []

for planilha in arquivos_planilhas:
    caminho_arquivo = os.path.join(pasta_planilhas, planilha)
    
    df = pd.read_excel(caminho_arquivo)
    
    # Verificar e imprimir os valores da primeira coluna onde a terceira coluna é "Dermonecrotic"
    for index, row in df.iterrows():
        if row.iloc[2] == "Dermonecrotic":
            for pep in peps:
                caminho_pep = os.path.join(pasta_pep, pep)
                with open(caminho_pep, 'r')as file:
                    conteudo = file.read()
                inicio = conteudo.find(row.iloc[0])
                fim = conteudo.find(">", inicio)
                if inicio != -1 and fim != -1:
                    substring = conteudo[inicio:fim]
                    coisa.append({
                        "conteudo": substring
                    })
                    save_to_json(coisa, ler_arquivo_codigos(nomes)[indice] + ".json")
                    # print(coisa)
                    indice += 1
                    coisa = []




