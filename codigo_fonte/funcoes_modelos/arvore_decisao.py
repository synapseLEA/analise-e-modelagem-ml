from funcoes_auxiliares.limpar_dataframe import dataframeLimpo
import matplotlib.pyplot as plt
import seaborn as sns

df = dataframeLimpo()

def visualizar_dataframe(quantidadeLinhas:int):
    return df.head(quantidadeLinhas)

def colunas_correlacao():
    correlacao = df.corr()
    return correlacao

def variaveis_correlacao():
    correlacao = df.corr()
    variaveisMelhorCorrelacao = correlacao[abs(correlacao.values) > 0.19]
    return variaveisMelhorCorrelacao

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

def grafico_matrix_confusao():
    pass