pip Install streamlit

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Carregar conjunto de dados Iris como exemplo
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Criar modelo de árvore de decisão
model = DecisionTreeClassifier()
model.fit(X, y)

# Página principal do Streamlit
st.title("Aplicativo Streamlit com Árvore de Decisão")

# Sidebar para seleção de parâmetros
st.sidebar.header("Parâmetros do Modelo")
# Você pode adicionar opções para ajustar os parâmetros do modelo aqui, se desejar

# Exibir os dados
st.subheader("Conjunto de Dados Iris")
st.write(X.head())

# Previsões do modelo
st.subheader("Previsões do Modelo")
# Você pode adicionar interatividade aqui para fazer previsões usando o modelo treinado

# Exemplo: Previsão para uma nova entrada
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Substitua isso pelos seus próprios dados
prediction = model.predict(new_data)
st.write(f"Previsão: {iris.target_names[prediction[0]]}")

streamlit run app.py
