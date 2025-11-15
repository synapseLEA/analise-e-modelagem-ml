import streamlit as st
from ..funcoes_modelos import arvore_decisao

modelo = arvore_decisao

st.set_page_config(
    page_title='Árvore de Decisão',
    page_icon='🌳' 
)

sessao_grafico_correlacao = st.container(
    border=True
)
sessao_grafico_correlacao.pyplot(
    fig = modelo.grafico_correlacao()
)