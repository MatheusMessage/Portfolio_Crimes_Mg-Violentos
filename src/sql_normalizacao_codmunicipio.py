# src/sql_normalizacao_codmunicipio.py

import sqlite3

# Caminho para o banco principal e o secundário (IBGE)
db_crimes = "data/database/crimes_mg.sqlite"

# Conecta ao banco de crimes
conn = sqlite3.connect(db_crimes)
cursor = conn.cursor()

# Anexa o banco de municípios IBGE
cursor.execute("ATTACH DATABASE 'data/database/municipios_ibge.sqlite' AS ibge")

# Atualiza o codmunicipio com base no codincompleto do IBGE
cursor.execute("""
    UPDATE crimes
    SET codmunicipio = (
        SELECT i.codcompleto
        FROM ibge.municipios i
        WHERE crimes.codmunicipio = i.codincompleto
    )
    WHERE EXISTS (
        SELECT 1
        FROM ibge.municipios i
        WHERE crimes.codmunicipio = i.codincompleto
    )
""")

# Atualiza o nome do município para o padrão do IBGE (nomemunicipio)
cursor.execute("""
    UPDATE crimes
    SET municipio = (
        SELECT i.nomemunicipio
        FROM ibge.municipios i
        WHERE crimes.codmunicipio = i.codcompleto
    )
    WHERE EXISTS (
        SELECT 1
        FROM ibge.municipios i
        WHERE crimes.codmunicipio = i.codcompleto
    )
""")

# Atualiza o nome do município para caixa alta (UPPER)
cursor.execute("""
    UPDATE crimes
    SET municipio = UPPER(municipio)
""")

# Salva e fecha a conexão
conn.commit()
conn.close()

print("[✔] codmunicipio normalizado com dados do IBGE e nomes de municípios atualizados e convertidos para caixa alta.")
