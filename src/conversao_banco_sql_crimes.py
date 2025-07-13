# src/conversao_ibge_sql.py

import sqlite3
import pandas as pd
import os
from limpeza import tratar_dados_df

def criar_banco_municipios(csv_path, db_path):
    # Verifica se o arquivo CSV existe
    if not os.path.exists(csv_path):
        print(f"[ERRO] Arquivo CSV não encontrado: {csv_path}")
        return

    # Tenta múltiplos encodings
    encodings = ['utf-8', 'latin1']
    for enc in encodings:
        try:
            df = pd.read_csv(csv_path, sep=';', encoding=enc)
            break
        except UnicodeDecodeError:
            print(f"[AVISO] Falha ao ler com encoding {enc}, tentando próximo...")
    else:
        print("[ERRO] Não foi possível ler o CSV com os encodings testados.")
        return

    # Aplica o tratamento usando o script limpeza.py
    df = tratar_dados_df(df)

    # Cria a pasta do banco, se necessário
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Conecta ao banco
    conn = sqlite3.connect(db_path)
    
    # Salva a tabela
    df.to_sql('municipios_ibge', conn, if_exists='replace', index=False)
    print(f"[INFO] Banco criado e dados importados: {db_path}")
    conn.close()


if __name__ == '__main__':
    csv_path = 'docs/Municipios_pre_tratados.csv'
    db_path = 'data/database/municipios_ibge.sqlite'
    criar_banco_municipios(csv_path, db_path)