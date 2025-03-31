import pandas as pd
import os

# Caminho para o CSV
csv_path = os.path.join(os.path.dirname(__file__), '../../data/operadoras.csv')

# Primeiro carregue o DataFrame
df = pd.read_csv(csv_path, sep=";", encoding="utf-8")

# Agora aplique a substituição de valores nulos
df = df.where(pd.notnull(df), None)

def buscar_operadoras(termo):
    """Busca operadoras no DataFrame com tratamento de valores nulos"""
    try:
        # Converter todos os valores para string e fazer busca case-insensitive
        filtrados = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(termo).any(), axis=1)]
        
        # Garantir que nenhum valor NaN/NA reste
        return filtrados.replace({pd.NA: None, pd.NaT: None}).to_dict(orient='records')
    except Exception as e:
        print(f"Erro ao buscar operadoras: {str(e)}")
        return []