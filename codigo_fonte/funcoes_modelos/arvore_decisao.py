from funcoes_auxiliares.limpar_dataframe import dataframeLimpo
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df = dataframeLimpo()

def visualizar_dataframe(quantidadeLinhas:int):
    return df.head(quantidadeLinhas)

def colunas_correlacao():
    correlacao = df.corr()
    return correlacao

def variaveis_correlacao():
    correlacao = df.corr()
    colunas_correlacao = correlacao['diagnosed_diabetes']
    colunas_correlacao = colunas_correlacao[abs(colunas_correlacao.values) > 0.19].drop(['diabetes_stage','diagnosed_diabetes']).rename(
        'Coeficiente de Correlação'
    )
    return colunas_correlacao

def grafico_correlacao():
    fig, axs = plt.subplots(
        figsize=(21, 12)
    )
    correlacao = df.corr()
    sns.heatmap(
        correlacao,
        annot=True,
        fmt='.2f',
        cmap='YlGnBu'
    )
    plt.title("Correlação das variáveis númericas")
    return fig

def dados_treino_teste():
    correlacao = df.corr()
    colunas_correlacao = correlacao['diagnosed_diabetes']
    colunas_correlacao = colunas_correlacao[abs(colunas_correlacao.values) > 0.19].drop(['diabetes_stage','diagnosed_diabetes']).index
    X = df[colunas_correlacao]
    y = df['diagnosed_diabetes']
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )    


def grafico_matrix_confusao():
    pass