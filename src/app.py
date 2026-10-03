import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
    page_title="Analisador de Dados",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analisador de Arquivos CSV")
st.markdown("Faça o upload de um arquivo CSV para visualizar dados, estatísticas e gráficos interativos.")

# Componente de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Leitura do CSV com pandas
        df = pd.read_csv(uploaded_file)
        
        st.success("Arquivo carregado com sucesso!")
        
        # Exibição dos dados
        st.subheader("📋 Visualização dos Dados")
        st.dataframe(df)
        
        # Informações gerais
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total de Linhas", df.shape[0])
        with col2:
            st.metric("Total de Colunas", df.shape[1])
            
        # Estatísticas descritivas
        st.subheader("📈 Estatísticas Descritivas")
        st.write(df.describe())
        
        # Gerador de gráficos
        st.subheader("🎨 Gerador de Gráficos")
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        if numeric_columns:
            selected_col = st.selectbox("Selecione uma coluna numérica para gerar o gráfico:", numeric_columns)
            
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.hist(df[selected_col].dropna(), bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribuição da coluna: {selected_col}")
            ax.set_xlabel(selected_col)
            ax.set_ylabel("Frequência")
            
            st.pyplot(fig)
        else:
            st.warning("O arquivo enviado não possui colunas numéricas para geração de gráficos.")

    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")
else:
    st.info("Aguardando upload de um arquivo CSV para iniciar.")
