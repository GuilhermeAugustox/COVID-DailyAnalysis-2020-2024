# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
''''''
df = pd.read_csv('WHO-COVID-19-global-table-data.csv', sep=',')
df_total = df.drop(columns=['Cases - cumulative total per 100000 population', 'Cases - newly reported in last 7 days', 'Cases - newly reported in last 7 days per 100000 population', 'Cases - newly reported in last 24 hours', 'Deaths - cumulative total per 100000 population', 'Deaths - newly reported in last 7 days', 'Deaths - newly reported in last 7 days per 100000 population', 'Deaths - newly reported in last 24 hours'])

st.markdown("<h1 style='text-align: center;'> DashBoard sobre dados da COVID-19 (2020-2024) <h1>", unsafe_allow_html=True )

df_sorted = df_total.sort_values(by = 'Name', ascending=True)
total_casos_mortes_sorted = df_total.sort_values(by = 'Cases - cumulative total', ascending=False)
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

fig_casos_10 = px.bar(top_10, x = 'Name', y = ['Cases - cumulative total'],title = '10 Países com mais Casos', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo', 'Name': 'País'}, height = 700, width = 800)

fig_mortes_10 = px.bar(top_10, x = 'Name', y = ['Deaths - cumulative total'],title = '10 Países com mais Mortes', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo', 'Name': 'País'}, height = 700, width = 800)

fig_casos_mortes_10 = px.bar(top_10, x = 'Name', y = ['Cases - cumulative total', 'Deaths - cumulative total'],title = 'Relação de Casos X Mortes dos 10 Maiores', barmode = 'group', labels = {'value': 'Total', 'variable': 'Tipo', 'Name': 'País'}, height = 700, width = 800)



fig_casos = px.bar(df_sorted, x = 'Name', y = 'Cases - cumulative total',title = 'Número de Casos por País', barmode = 'group', labels = {'Cases - cumulative total': 'Total de Casos', 'Name': 'País'}, height = 700, width = 800)
fig_mortes = px.bar(df_sorted, x = 'Name', y = 'Deaths - cumulative total',title = 'Número de Mortes por País', barmode = 'group', labels = {'Deaths - cumulative total': 'Total de Mortes', 'Name': 'País'}, height = 700, width = 800)
fig_casos_mortes = px.bar(df_sorted, x = 'Name', y = ['Cases - cumulative total', 'Deaths - cumulative total'], barmode = 'group', labels = {'Cases - cumulative total': 'Total de Casos', 'Name': 'País'}, height = 700, width = 800)

fig_casos_10.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)
fig_mortes_10.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)
fig_casos_mortes_10.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)
fig_casos.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)
fig_mortes.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)
fig_casos_mortes.update_layout(xaxis = {'categoryorder': 'total descending'}, xaxis_tickangle = -45)

#st.write('Gráfico: Casos e Mortes por País')
#plot_barras(top_10)

st.markdown("<h2 style='text-align: center;'> 10 Maiores Registros <h2>", unsafe_allow_html=True )

st.write('Gráfico Interativo: Casos por País')
st.plotly_chart(fig_casos_10)

st.write('Gráfico Interativo: Mortes por País')
st.plotly_chart(fig_mortes_10)

st.write('Gráfico Interativo: Casos e Mortes por País')
st.plotly_chart(fig_casos_mortes_10)


st.markdown("<h3 style='text-align: center;'> Registros Globais <h3>", unsafe_allow_html=True )

st.write('Gráfico Interativo: Casos por País')
st.plotly_chart(fig_casos)


st.write('Gráfico Interativo: Mortes por País')
st.plotly_chart(fig_mortes)


st.write('Gráfico Interativo: Casos e Mortes por País')
st.plotly_chart(fig_casos_mortes)


st.write('Tabela dos Dados:')
st.dataframe(df_sorted)