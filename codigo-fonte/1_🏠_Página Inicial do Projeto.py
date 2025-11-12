import streamlit as st
import os

st.set_page_config(
    page_title='Página Inicial do Projeto',
    page_icon='🏠',
    layout='wide'
)

# SESSÃO DA LOGO
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

logo = os.path.join(
    diretorio_atual,
    '..',
    'imagens',
    'logo.png'
)

logo_grande = os.path.join(
    diretorio_atual,
    '..',
    'imagens',
    'logogrande.png'
)

st.logo(
    logo_grande,
    icon_image=logo,
    size='Large'
)

# TÍTULO E INFORMAÇÕES
st.markdown(
    body="""
# Análise e Discursão dos Resultados de Diferentes Modelos de Aprendizado de Máquina em uma Única Base de Dados.

## Tópicos que serão discutidos: 
* O que são modelos de aprendizado de máquina.
* Onde são utilizados esses modelos.
* Qual a importância de utilizar esses algoritmos.
* Por que diferentes modelos tem diferentes resultados.
* Como aplicar esses algoritmos na minha base de dados.
"""
)
