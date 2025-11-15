import streamlit as st
from funcoes_modelos import arvore_decisao

modelo = arvore_decisao

st.set_page_config(
    page_title='Árvore de Decisão',
    page_icon='🌳' 
)

st.markdown("""
## 🌳 Análise do Modelo de Árvore de Decisão

Este documento detalha as métricas de avaliação e a metodologia estrutural utilizada para analisar o desempenho do modelo de **Árvore de Decisão** em um problema de classificação (diagnóstico de diabetes).

---

### 📊 Métricas Chave de Classificação

Para um modelo de classificação como este, as métricas são essenciais para entender a performance, especialmente considerando o desequilíbrio potencial nas classes e o custo dos diferentes tipos de erro.

* **Acurácia (Accuracy):** O percentual geral de previsões corretas. É o indicador mais direto do desempenho do modelo.
* **Precisão (Precision):** A proporção de identificações **positivas preditas** que foram realmente corretas (Verdadeiros Positivos). Importante quando se deseja minimizar **Falsos Positivos (FP)** (i.e., evitar classificar alguém saudável como doente).
* **Recall (Revocação ou Sensibilidade):** A proporção de casos **positivos reais** que foram corretamente identificados. Essencial quando se deseja minimizar **Falsos Negativos (FN)** (i.e., evitar deixar de diagnosticar um caso real de diabetes).
* **F1-Score:** A média harmônica entre **Precisão** e **Recall**. Oferece uma métrica de equilíbrio robusta, sendo a preferida para avaliação em cenários com classes desbalanceadas.

---

### 📝 Estrutura da Página de Análise

A página do Streamlit será organizada em etapas sequenciais para fornecer uma narrativa completa, da exploração dos dados à validação do modelo:

1.  **Visualização e Exploração Inicial do DataFrame**
    * **Objetivo:** Obter uma visão rápida da qualidade do conjunto de dados, incluindo a identificação de **valores máximos e mínimos**, a distribuição dos dados e a presença de **valores ausentes ou desconhecidos** que necessitam de tratamento (limpeza).
2.  **Análise de Correlação e Seleção de Features**
    * **Objetivo:** Identificar as variáveis que apresentam maior **correlação** com o diagnóstico de diabetes (variável alvo). Utilização de **gráficos de correlação (Mapas de Calor)** para guiar a seleção das *features* mais relevantes para o modelo.
3.  **Preparação de Dados e Treinamento do Modelo**
    * **Objetivo:** Realizar a **separação dos dados** em conjuntos de **Treino** e **Teste**. Em seguida, aplicar os dados de treino ao algoritmo de **Árvore de Decisão** para a criação do modelo de classificação.
4.  **Visualização da Matriz de Confusão**
    * **Objetivo:** Apresentar graficamente a **Matriz de Confusão** para verificar, de forma detalhada, o número exato de **Acertos** (VP e VN) e **Erros** (FP e FN) cometidos pelo modelo no conjunto de teste.
5.  **Relatório de Métricas e Interpretação dos Resultados**
    * **Objetivo:** Apresentar e discutir os valores calculados para **Acurácia, Precisão, Recall e F1-Score**. O foco é entender como cada métrica se **modela ao problema** e validar o desempenho geral do modelo.
---
""")

quantidadeLinhas = st.number_input(
    label='Selecione a quantidade de linhas que deseja visualizar: ',
    min_value=5,
    max_value=12
)
st.dataframe(
    data=modelo.visualizar_dataframe(quantidadeLinhas)
)

sessao_grafico_correlacao = st.container(
    border=True
)
sessao_grafico_correlacao.pyplot(
    fig = modelo.grafico_correlacao()
)

sessao_grafico_correlacao.dataframe(
    data=modelo.colunas_correlacao()
)

print("teste")