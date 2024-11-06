# Objetivo
Este projeto consistem em um painel interativo desenvolvido utilizando a biblioteca Streamlit, onde é exibido os dados globais de COVID-19 compilados pela Organização Mundial de Saúde(OMS). Possuíndo como principal objetivo proporcionar uma análise visual da pandemia durante o período de 2020 a 2024, contendo gráficos e mapas informativos que possibilitam uma compreensão mais detalhada do impacto da COVID-19 em diferentes países.

# Dataset
- Fonte: Daily COVID-19 Data(2020-2024)
- Descrição: Daily COVID-19 Cases and Deaths World Wide(WHO-Reporting)-(2020-2024)
- Link Dataser: [Daily COVID-19 Data(2020-2024)](https://www.kaggle.com/datasets/abdoomoh/daily-covid-19-data-2020-2024)

# Metodologia
- Limpeza dos Dados: Após o carregamento do dataset, foi realizada a remoção de algumas colunas presentes no dataset original que não irão ser utilizadas no processo de análise
- Análise Exploratória (EDA): Durante a EDA foi realizado várias relações e comparações dentre elas: total de casos e mortes por regiões, total e relação de casos e mortes por país. 

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

# Para Rodar o Projeto no Streamlit
A Visualização deste projeto foi desenvolvido com o Streamlit, possibilitando a execução do projeto localmente para a exploração dos dados interativamente. Siga os dados abaixo:

1. Certifique-se de possuir a versão Python 3.7+
2. Instale as Dependências <br/>
Clone o repositório para sua máquina e isntale as dependências necessárias
3. Execute a visualização com Streamlit<br/>
Inicie a aplicação utilizando o comando:
streamlit run nome_do_arquivo.py
Lembre-se de substituir "nome_do_arquivo" pelo nome do arquivo principal do projeto (o arquivo Python que está o código do Streamlit)
4. Acesse a Visualização<br/>
Após a execução do comando, o Streamlit iniciará um servidor local e exibirá o endereço onde a visualização está operando. Geralmente, o endereço padrão é: http://localhost:8501
Acesse esse endereço em seu navegador para visualizar a análise e explorar os dados.

# Licença
Esse projeto é licenciado sob a liderança MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.