import os
import sqlite3
import pandas as pd
from limpeza import tratar_dados_df  # Importa sua função de limpeza

def criar_banco_municipios(csv_path, db_path):
    # Verifica se o arquivo CSV existe
    if not os.path.exists(csv_path):
        print(f"[ERRO] Arquivo CSV não encontrado: {csv_path}")
        return
    
    # Lê o CSV com separador ';'
    df = pd.read_csv(csv_path, sep=';', encoding='latin1')  # Tente 'latin1' por segurança
    
    # Aplica a limpeza para normalizar colunas e remover acentos etc
    df = tratar_dados_df(df)
    
    # Cria pasta do banco caso não exista
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Conecta/cria banco SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Cria tabela municipios (ajuste colunas conforme seu CSV pre-tratado)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS municipios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codmunicipio INTEGER,
        municipio TEXT,
        populacao INTEGER
    )
    ''')
    
    conn.commit()
    
    # Importa os dados para tabela municipios, substituindo dados antigos
    df.to_sql('municipios', conn, if_exists='replace', index=False)
    
    print(f"[INFO] Dados importados para o banco: {db_path}")
    conn.close()

if __name__ == '__main__':
    csv_file = 'docs/Municipios_pre_tratados.csv'
    db_file = 'data/database/municipios_ibge.sqlite'
    criar_banco_municipios(csv_file, db_file)