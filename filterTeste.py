import streamlit as st

# Filtro por Nicho
nicho_options = ["Moda", "Comédia", "Viagem", "Música", "Fitness", "Arte"]
selected_nicho = st.sidebar.selectbox("Selecione o Nicho:", nicho_options)

# Filtro por Gênero
genero_options = ["Homem", "Mulher"]
selected_genero = st.sidebar.selectbox("Selecione o Gênero:", genero_options)

# Filtro por Idade
idade_options = ["Jovem", "Adulto", "Idoso"]
selected_idade = st.sidebar.selectbox("Selecione a Idade:", idade_options)

# Exibindo os resultados
st.write(f"**Nicho Selecionado:** {selected_nicho}")
st.write(f"**Gênero Selecionado:** {selected_genero}")
st.write(f"**Idade Selecionada:** {selected_idade}")

# Aqui você pode adicionar lógica adicional com base nos filtros selecionados
# para filtrar seus dados ou executar outras ações específicas.
