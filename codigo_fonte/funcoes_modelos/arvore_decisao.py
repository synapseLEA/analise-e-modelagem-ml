from funcoes_auxiliares.limpar_dataframe import dataframeLimpo
import matplotlib.pyplot as plt
import seaborn as sns
df = dataframeLimpo()

def grafico_correlacao():
    fig, axs = plt.subplots()
    correlacao = df.corr()
    sns.heatmap(
        correlacao,
        annot=True,
        fmt='.2f',
        cmap='YlGnBu'
    )
    plt.title("Correlação das variáveis númericas")
    return fig

    