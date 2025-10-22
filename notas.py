
import streamlit as st
import pandas as pd
import altair as alt



medias = pd.read_csv('medias_das_disciplinas.csv')

st.set_page_config(
    page_title="Faminas Virtual",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",   
)



st.write("# Faminas Virtual ")
st.write('## Relatório da 1ª Etapa do segundo semestre de 2025')
st.write('---')

col1, col2 = st.columns(2)

with col1:
    st.write('### Médias')
    st.write(f'- #### Média Geral das disciplinas: **{medias["Média"].mean():.2f}**/50')
    st.write(f'- #### Média Geral da Avaliação: **{medias["Avaliação 1ª Etapa"].mean():.2f}**/30')
    st.write(f'- #### Média Geral do Videoprojeto: **{medias["Videoprojeto"].mean():.2f}**/10')
    st.write(f'- #### Média Geral do Percurso de Aprendizagem: **{medias["Percurso de Aprendizagem 1ª Etapa"].mean():.2f}**/10')

with col2:
    st.write('### Dispersão das médias de notas das disciplinas')
    medias.rename(columns={'Média':'Total'}, inplace=True)
    st.scatter_chart(
        medias,
        x=None,
        y=['Total', 'Avaliação 1ª Etapa', 'Videoprojeto', 'Percurso de Aprendizagem 1ª Etapa'],
        x_label='Notas',
        y_label='Total de pontos'
    )

st.write('---')

col1,col2 = st.columns(2)

with col1:
    st.write('### Protocolos recebidos')
    protocolos = pd.DataFrame({'Protocolos': ['Prova','PA'], 'Quantidade': [101,11]})
    protocolo_fig = alt.Chart(protocolos).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Quantidade", type="quantitative", aggregate='sum', stack=True),
        color=alt.Color(field="Protocolos", type="nominal"),
        text=alt.Text(field="Quantidade", type="quantitative", aggregate='sum'),
        tooltip=[alt.Tooltip(field="Protocolos", type="nominal"),
                 alt.Tooltip(field="Quantidade", type="quantitative", aggregate='sum', title='Quantidade')]
    ).properties(
        title='Distribuição dos Protocolos Recebidos',        
    )
    text = protocolo_fig.mark_text(radius=100, size=20, fontWeight='bold').encode(
        text='Quantidade:Q',
        color=alt.value("#050003"),
    )

    st.altair_chart(protocolo_fig + text, use_container_width=True)
with col2:
    st.write('### Questões anuladas')
    anuladas = pd.DataFrame({'Anulado': ['Prova Questão anulada','Prova Gabarito alterado','PA Questão anulada'], 'Quantidade': [10,2,3]})
    anuladas_fig = alt.Chart(anuladas).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Quantidade", type="quantitative", aggregate='sum', stack=True),
        color=alt.Color(field="Anulado", type="nominal"),
        text=alt.Text(field="Quantidade", type="quantitative", aggregate='sum'),
        tooltip=[alt.Tooltip(field="Anulado", type="nominal"),
                 alt.Tooltip(field="Quantidade", type="quantitative", aggregate='sum', title='Quantidade')]
    ).properties(
        title='Distribuição das Questões Anuladas',        
    )

    text = anuladas_fig.mark_text(radius=100, size=20, fontWeight='bold').encode(
        text='Quantidade:Q',
        color=alt.value("#050003"),
    )

    st.altair_chart(anuladas_fig + text, use_container_width=True)

    st.write('Total de questões anuladas das provas: **12 de 576** - 2.01%')
    st.write('Total de questões anuladas dos percursos de aprendizagem: **3 de 310** - 0.97%')



st.write('---')
