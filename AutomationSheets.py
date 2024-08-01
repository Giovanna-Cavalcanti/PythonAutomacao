import pandas as pd
import os
import json

def ler_arquivo_codigos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]

def save_to_json(data, filename):
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
def save_to_txt(data, filename):
    output_dir = 'fastas'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w') as txt_file:
        for sequence in data:
            txt_file.write(f'{sequence}\n')

pasta_planilhas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\planilhasxlsx'
pasta_pep = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\pepLer'
nomes = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\nomes.txt'
indice = 0

peps = os.listdir(pasta_pep)
planilhas = os.listdir(pasta_planilhas)
nomes_arquivos = ler_arquivo_codigos(nomes)
coisa = []

for planilha in planilhas:
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
                        # "conteudo": substring
                        substring
                    })
    # print(coisa)
    # save_to_json(coisa, ler_arquivo_codigos(nomes)[indice] + ".json")
    save_to_txt(coisa, "allDermonecroticsSpiders.fasta")
    # indice += 1
    # coisa = []
            




