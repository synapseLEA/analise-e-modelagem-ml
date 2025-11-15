import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

def dataframeLimpo():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio_atual)
    caminho_csv = os.path.join(
        diretorio_raiz,
        '..',
        'banco-dados',
        'bruto',
        'diabetes_dataset.csv'
    )
    df = pd.read_csv(caminho_csv)
    colunas_categoricas = df.select_dtypes(include='object').columns
    for coluna in colunas_categoricas:
        le = LabelEncoder()
        df[coluna] = le.fit_transform(df[coluna])
    return df
