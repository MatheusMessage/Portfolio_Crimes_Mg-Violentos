# src/limpeza.py

import pandas as pd
import unicodedata
import re

def remover_acentos_e_caracteres_especiais(texto):
    if not isinstance(texto, str):
        return texto
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto)
    texto = texto.strip()
    return texto

def normalizar_nome_coluna(nome):
    nome = remover_acentos_e_caracteres_especiais(nome)
    nome = nome.lower()
    return nome

def tratar_dados_df(df: pd.DataFrame) -> pd.DataFrame:
    # Normaliza nomes das colunas
    df.columns = [normalizar_nome_coluna(c) for c in df.columns]

    # Cria coluna data a partir de mes e ano
    if 'mes' in df.columns and 'ano' in df.columns:
        df['mes'] = df['mes'].astype(str).str.zfill(2)
        df['ano'] = df['ano'].astype(str)
        df['data'] = pd.to_datetime(df['ano'] + '-' + df['mes'] + '-01', errors='coerce')

    # Se houver coluna 'data_ocorrencia', converte para datetime
    if 'data_ocorrencia' in df.columns:
        df['data_ocorrencia'] = pd.to_datetime(df['data_ocorrencia'], errors='coerce', dayfirst=True)

    # Remove linhas sem data válida (em 'data' ou 'data_ocorrencia')
    if 'data' in df.columns:
        df = df.dropna(subset=['data'])
    elif 'data_ocorrencia' in df.columns:
        df = df.dropna(subset=['data_ocorrencia'])

    # Remove colunas totalmente nulas
    df = df.dropna(axis=1, how='all')

    # Remove acentos e caracteres especiais das colunas de texto
    colunas_texto = df.select_dtypes(include='object').columns
    for col in colunas_texto:
        df[col] = df[col].apply(remover_acentos_e_caracteres_especiais)

    return df