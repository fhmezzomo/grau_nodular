import streamlit as st
from PIL import Image
import inteligencia

# Configuração da página
st.set_page_config(layout='wide')
st.title("GRAU DE NODULARIZAÇÃO")
st.subheader("Cálculo estimativo do grau de nodularização à partir da imagem de uma metalografia")

chave = st.secrets["GEMINI_CHAVE"]

# Upload da imagem
st.header("Faça o upload da metalografia")
arquivo_foto = st.file_uploader("Selecione uma metalografia", type=["jpg", "jpeg", "png"])
if arquivo_foto is not None:
    imagem = Image.open(arquivo_foto)
    st.image(imagem, caption="Metalografia carregada", width=200) # limita ampliação de imagem para evitar distorções

    if st.button("Estimar Grau de Nodularização"):
        with st.spinner("Estimando..."):
            try:
                nodularizacao = inteligencia.grau_nodular(chave, imagem)
                st.session_state.nodularizacao = nodularizacao
                st.success("Estimativa concluída!")
                st.write(f"**Resultado:** {nodularizacao}")
            except Exception as e:
                st.error(f"Erro ao estimar o grau de nodularização: {e}")