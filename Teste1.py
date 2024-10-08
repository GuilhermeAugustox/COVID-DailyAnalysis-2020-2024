# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
''''''
df = pd.read_csv('WHO-COVID-19-global-table-data.csv', sep=',')
df_total = df.drop(columns=['Cases - cumulative total per 100000 population', 'Cases - newly reported in last 7 days', 'Cases - newly reported in last 7 days per 100000 population', 'Cases - newly reported in last 24 hours', 'Deaths - cumulative total per 100000 population', 'Deaths - newly reported in last 7 days', 'Deaths - newly reported in last 7 days per 100000 population', 'Deaths - newly reported in last 24 hours'])
df_filtrado = df[df['Name'] != 'Global']


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


st.plotly_chart(fig_casos_10)
st.write('Gráfico 01: Este gráfico apresenta os 10 países com o maior número de casos de COVID-19 resgistrados no período de 2020 a 2024')

st.plotly_chart(fig_mortes_10)
st.write('Gráfico 02: Este gráfico apresenta os 10 países com o maior número de mortes de COVID-19 resgistradas no período de 2020 a 2024')

st.write('Gráfico Interativo: Casos e Mortes por País')
st.plotly_chart(fig_casos_mortes_10)
st.write('Gráfico 03: Gráfico apresenta os 10 países com o maior número de casos de COVID-19 e as respectivas quantidades de mortes no período de 2020 a 2024')

st.markdown("<h3 style='text-align: center;'> Registros Globais <h3>", unsafe_allow_html=True )

st.plotly_chart(fig_casos)
st.write('Gráfico 04: Este gráfico apresenta as quantidades de casos de COVID-19 em todos os países ao redor do mundo, registrados no período de 2020 a 2024')

st.plotly_chart(fig_mortes)
st.write('Gráfico 05: Este gráfico apresenta as quantidades de mortes de COVID-19 em todos os países ao redor do mundo, registrados no período de 2020 a 2024')

st.plotly_chart(fig_casos_mortes)
st.write('Gráfico 06: Este gráfico apresenta as quantidade de casos e morte por COVID-19 em todos os países ao redor do mundo, registradas no período de 2020 a 2024')



df_filtrado  = df_filtrado.rename(columns = {'Name': 'Country'})
fig_mundi_casos = px.choropleth(
    df_filtrado, 
    locations = 'Country',
    locationmode = 'country names',
    color = 'Cases - cumulative total',
    hover_name = 'Country',
    color_continuous_scale = 'greens',
    height = 700,
    width = 700,
    title = 'Mapa Minocromático: Casos de COVID-19 (2020-2024)' 
)


fig_mundi_mortes = px.choropleth(
    df_filtrado, 
    locations = 'Country',
    locationmode = 'country names',
    color = 'Deaths - cumulative total',
    hover_name = 'Country',
    color_continuous_scale = 'reds',
    height = 700,
    width = 700,
    title = 'Mapa Minocromático: Mortes de COVID-19 (2020-2024)' 
)
st.plotly_chart(fig_mundi_casos)
st.write('Gráfico 07: Este gráfico apresenta um mapa-múndi, representando a quantidade total de casos por COVID-19 registrados no período de 2020 a 2024. As áreas em tons de verde mais escuros indicam uma quantidade maior de casos, enquanto os tons mais claros representam uma menor incidência')
st.plotly_chart(fig_mundi_mortes)
st.write('Gráfico 07: Este gráfico apresenta um mapa-múndi, representando a quantidade total de mortes por COVID-19 registrados no período de 2020 a 2024. As áreas em tons de vermelho mais escuros indicam uma quantidade maior de casos, enquanto os tons mais claros representam uma menor incidência')

st.write('Tabela dos Dados:')
st.dataframe(df_sorted)