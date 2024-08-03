import os

pasta_fastas = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\WAfastasDermonecrotic'
fastas_1 = os.listdir(pasta_fastas)

for arquivo2 in fastas_1:
    caminho_do_arquivo = os.path.join(pasta_fastas, arquivo2)
    # Abrir o arquivo de entrada para leitura
    with open(caminho_do_arquivo, 'r') as file:
        linhas = file.readlines()
    # Processar cada linha removendo a palavra específica
    linhas_modificadas = [linha.replace(r"\n", '\n') for linha in linhas]
    # Escrever as linhas modificadas no mesmo arquivo
    with open(caminho_do_arquivo, 'w') as file:
        file.writelines(linhas_modificadas)

# caminho_do_arquivo = r'C:\Users\giova\OneDrive\Área de Trabalho\Python testes e estudos\WAfastasDermonecrotic\Acanthoscurria_geniculata.fasta'

# with open(caminho_do_arquivo, 'r') as file:
#     linhas = file.readlines()
# # Processar cada linha removendo a palavra específica
# linhas_modificadas = [linha.replace(r"\n", '\n') for linha in linhas]
# # Escrever as linhas modificadas no mesmo arquivo
# with open(caminho_do_arquivo, 'w') as file:
#     file.writelines(linhas_modificadas)