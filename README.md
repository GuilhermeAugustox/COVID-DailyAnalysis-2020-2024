# Objetivo
Este projeto consistem em um painel interativo desenvolvido utilizando a biblioteca Streamlit, onde é exibido os dados globais de COVID-19 compilados pela Organização Mundial de Saúde(OMS). Possuíndo como principal objetivo proporcionar uma análise visual da pandemia durante o período de 2020 a 2024, contendo gráficos e mapas informativos que possibilitam uma compreensão mais detalhada do impacto da COVID-19 em diferentes países.

# Dataset
- Fonte: Daily COVID-19 Data(2020-2024)
- Descrição: Daily COVID-19 Cases and Deaths World Wide(WHO-Reporting)-(2020-2024)
- Link Dataser: [Daily COVID-19 Data(2020-2024)](https://www.kaggle.com/datasets/abdoomoh/daily-covid-19-data-2020-2024)

# Metodologia

# Tecnologias e Bibliotecas
- Linguagem: Python
- Bibliotecas: Pandas, Numpy, Matplotlib, Ploty Express e Streamlit

# Gráficos disponíveis
1. Gráficos de Barras:
    - Top 10 Países com mais casos: Gráfico de barras que exibe os 10 países que possuiram a maior quantidades de casos cumulativos.
    - Top 10 Países com mais mortes: Gráficos de barras que exibe os 10 países que masi ocorreram mortes cumulativas.
    - Relação Casos x Mortes: Comparação entre a quantidade de casos e o número de mortes nos 10 países mais afetados.

2. Análise Global por País:
    - Casos Cumulativos por País: Visualização em barras do total de casos por cada país.
    - Mortes Cumulativas por País: Visualização em barras do total de morte por cada país.
    - Comparação Casos x Mortes Global: Comparaçãp entre a quantidade total de casos e mortes para cada país

3. Mapas Mundiais:
    - Mapa de Casos: Mapa coroplético que representa a quantidade total de casos de COVID-19 em cada país
    - Mapa de Mortes: Mapa coroplético que representa a quantidade total de mortes de COVID-19 em cada país

4. Tabela de Dados:
    - Exibição dos dados da OMS em uma tabela interativa, possibilitando a filtragem e a pesquisa para análises mais detalhadas