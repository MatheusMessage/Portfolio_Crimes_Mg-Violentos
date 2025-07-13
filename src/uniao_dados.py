# src/uniao_dados.py

import pandas as pd
import glob
import os
from limpeza import tratar_dados_df

def uniao_arquivos_csv(pasta_entrada, arquivo_saida, encoding='utf-8', sep=';'):
    arquivos = glob.glob(os.path.join(pasta_entrada, '*.csv'))
    if not arquivos:
        print(f'[ERRO] Nenhum arquivo CSV encontrado na pasta: {pasta_entrada}')
        return

    lista_dfs = []
    for arquivo in arquivos:
        print(f'Lendo arquivo: {arquivo}')
        df_temp = pd.read_csv(arquivo, encoding=encoding, sep=sep)
        lista_dfs.append(df_temp)

    df_unificado = pd.concat(lista_dfs, ignore_index=True)
    print(f'Total de linhas antes do tratamento: {df_unificado.shape[0]}')
    print(f'Total de colunas: {df_unificado.shape[1]}')

    # Aplica tratamento
    df_tratado = tratar_dados_df(df_unificado)

    print(f'Total de linhas após tratamento: {df_tratado.shape[0]}')
    print(f'Total de colunas após tratamento: {df_tratado.shape[1]}')

    pasta_saida = os.path.dirname(arquivo_saida)
    if pasta_saida and not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    df_tratado.to_csv(arquivo_saida, index=False, encoding=encoding, sep=sep)
    print(f'Arquivo unificado e tratado salvo em: {arquivo_saida}')


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))

    pasta_entrada = os.path.normpath(os.path.join(base_dir, '..', 'data', 'raw'))
    arquivo_saida = os.path.normpath(os.path.join(base_dir, '..', 'data', 'processed', 'crimes_unificado_bruto.csv'))

    print(f'Caminho da pasta de entrada: {pasta_entrada}')
    print(f'Caminho do arquivo de saída: {arquivo_saida}')

    uniao_arquivos_csv(pasta_entrada, arquivo_saida)