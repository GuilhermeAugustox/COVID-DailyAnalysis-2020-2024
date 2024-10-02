# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df = pd.read_csv('WHO-COVID-19-global-table-data.csv', sep=',')

st.markdown("<h1 style='text-align': center;'> Dados Globais de COVID-19<h1>", unsafe_allow_html=True )

total_casos_mortes_sorted = df.sort_values(by = 'Cases - cumulative total', ascending=False)
top_10 = total_casos_mortes_sorted.iloc[1:11]

#def plot_barras(top_10):
    #casos = top_10['Cases - cumulative total']
    #mortes = top_10['Deaths - cumulative total']
    #paises = top_10['Name']

    #bar_width = 0.35
    #indice = np.arange(len(paises))

    #fig, ax = plt.subplots(figsize = (10,6))
    #ax.bar(indice, casos, bar_width, label = 'Mortes', color = 'red')

    #ax.set_xlabel('Países')
    #ax.set_ylabel('Total')
    #ax.set_title('Relação entre Casos X Mortes por País')
    #ax.set_xticks(indice + bar_width / 2)
    #ax.set_xticklabels(paises, rotation = 90)

    #ax.legend()
    #st.pyplot(fig)

fig_casos = px.bar(top_10, x = 'Name', y = ['Cases - cumulative total'],title = 'Número de Casos por País', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo'}, height = 400)

fig_mortes = px.bar(top_10, x = 'Name', y = ['Deaths - cumulative total'],title = 'Número de Mortes por País', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo'}, height = 400)

fig_casos_mortes = px.bar(top_10, x = 'Name', y = ['Cases - cumulative total', 'Deaths - cumulative total'],title = 'Número de Casos e Mortes por País', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo'}, height = 400)

#st.write('Gráfico: Casos e Mortes por País')
#plot_barras(top_10)

st.write('Gráfico Interativo: Casos por País')
st.plotly_chart(fig_casos)

st.write('Gráfico Interativo: Mortes por País')
st.plotly_chart(fig_mortes)

st.write('Gráfico Interativo: Casos e Mortes por País')
st.plotly_chart(fig_casos_mortes)

st.write('Tabela dos Dados:')
st.dataframe(top_10)