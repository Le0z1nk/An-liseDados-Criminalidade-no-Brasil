import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

st.set_page_config(
    page_title="Dashboard de Análise de Crimes no Brasil",
    page_icon="📊",
    layout="wide"
)

sns.set_theme(style="whitegrid")

@st.cache_data
def carregar_dados_csv():
    df = pd.read_csv("dados/simulacao_criminalidade_brasil.csv")
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    return df

df = carregar_dados_csv()

st.title("Dashboard de Análise de Crimes no Brasil")
st.write("""
Este dashboard apresenta uma análise de crimes no Brasil.
A proposta é demonstrar um projeto completo de análise de dados, integrando Pandas, visualização
de dados e Streamlit.
""")

#FILTROS--------------------
st.sidebar.header("Filtros")
ano = sorted(df["ano"].dropna().unique())
mes = sorted(df["mes"].dropna().unique())
regiao = sorted(df["regiao"].dropna().unique())
uf = sorted(df["uf"].dropna().unique())
cidade = sorted(df["cidade"].dropna().unique())
tipo_crime = sorted(df["tipo_crime"].dropna().unique())
periodo_dia = sorted(df["periodo_dia"].dropna().unique())
nivel_risco = sorted(df["nivel_risco"].dropna().unique())

ano_sel = st.sidebar.multiselect("Ano", options=ano, default=ano)
mes_sel = st.sidebar.multiselect("Mês", options=mes, default=mes)
regiao_sel = st.sidebar.multiselect("Região", options=regiao, default=regiao)
uf_sel = st.sidebar.multiselect("UF", options=uf, default=uf)
cidade_sel = st.sidebar.multiselect("Cidade", options=cidade, default=cidade)
tipo_crime_sel = st.sidebar.multiselect("Tipo de Crime", options=tipo_crime, default=tipo_crime)
periodo_dia_sel = st.sidebar.multiselect("Período do dia", options=periodo_dia, default=periodo_dia)
nivel_risco_sel = st.sidebar.multiselect("Nível de Risco", options=nivel_risco, default=nivel_risco)

data_min = df["data"].min().date()
data_max = df["data"].max().date()

intervalo_datas = st.sidebar.date_input(
    "Período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max
)

if isinstance(intervalo_datas, tuple) and len(intervalo_datas) == 2:
    inicio, fim = intervalo_datas
else:
    inicio, fim = data_min, data_max

df_filtrado = df[
    (df["ano"].isin(ano_sel)) &
    (df["mes"].isin(mes_sel)) &
    (df["regiao"].isin(regiao_sel)) &
    (df["uf"].isin(uf_sel)) &
    (df["cidade"].isin(cidade_sel)) &
    (df["tipo_crime"].isin(tipo_crime_sel)) &
    (df["periodo_dia"].isin(periodo_dia_sel)) &
    (df["nivel_risco"].isin(nivel_risco_sel)) &
    (df["data"].dt.date >= inicio) &
    (df["data"].dt.date <= fim)
]

if df_filtrado.empty:
    st.warning("Nenhum registro enontrado para os filtros selecionados.")
    st.stop()

#KPIs---------------------------------------------
st.subheader("Indicadores-chave de desempenho")
total_ocorrencias = df_filtrado["ocorrencias"].sum()

cidade_violenta_series = df_filtrado.groupby("cidade")["indice_violencia"].mean().sort_values(ascending=False)
cidade_mais_violenta = cidade_violenta_series.index[0] if not cidade_violenta_series.empty else "N/A"
cidade_violencia_valor = f"{cidade_violenta_series.iloc[0]:.2f}" if not cidade_violenta_series.empty else "N/A"

crime_frequente_series = df_filtrado.groupby("tipo_crime")["ocorrencias"].sum().sort_values(ascending=False)
crime_mais_frequente = crime_frequente_series.index[0] if not crime_frequente_series.empty else "N/A"
crime_frequente_valor = f"{crime_frequente_series.iloc[0]:.0f}" if not crime_frequente_series.empty else "N/A"

total_vitimas = df_filtrado["vitimas"].sum()

media_violencia = df_filtrado["indice_violencia"].mean()

df_crime_critico_filtered = df_filtrado[df_filtrado["nivel_risco"] == 'Crítico']
regiao_critica_count = df_crime_critico_filtered.groupby("regiao")["nivel_risco"].count().sort_values(ascending=False)
regiao_mais_critica = regiao_critica_count.index[0] if not regiao_critica_count.empty else "N/A"

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total de Ocorrências",f"{total_ocorrencias:,.0f}".replace(",", "."))
col2.metric("Cidade Mais Violenta", cidade_mais_violenta, delta=f"Índice: {cidade_violencia_valor}")
col3.metric("Tipo de Crime Mais Frequente", crime_mais_frequente, delta=f"Ocorrências: {crime_frequente_valor}")
col4.metric("Total de Vítimas", f"{total_vitimas:,.0f}".replace(",", "."))
col5.metric("Índice Médio de Violência", f"{media_violencia:,.2f}".replace(".", ","))
col6.metric("Região mais Crítica", regiao_mais_critica)

st.divider()

#TABS---------
tab1, tab2, tab3 = st.tabs([
    "Visâo Geral",
    "Cidades e Tipos de Crime",
    "Dados"
])

with tab1:
  st.subheader("Evolução da Criminalidade")
  serie_mensal = (
      df_filtrado.groupby("data")["ocorrencias"].sum().reset_index().sort_values("data")
  )

  fig, ax = plt.subplots(figsize=(12, 5))

  sns.lineplot(data=serie_mensal, x="data", y="ocorrencias", marker="o", label="Ocorrências", ax=ax)
  ax.set_title("Evolução da Criminalidade")
  ax.set_xlabel("Data")
  ax.set_ylabel("Ocorrências")
  ax.tick_params(axis="x", rotation=45)
  st.pyplot(fig)
  st.info("""
    Este gráfico ajuda a identificar a evolução no número de ocorrências de crimes.
    """)
  
with tab2:
      graf_a, graf_b = st.columns(2)

      with graf_a:
          st.subheader("Ocorrências por cidade")
          ocorrencia_cidade = (
              df_filtrado.groupby("cidade")["ocorrencias"].sum().sort_values(ascending=False).reset_index()
          )
          fig, ax = plt.subplots(figsize=(8, 10))

          sns.barplot(data=ocorrencia_cidade, x="ocorrencias", y="cidade", ax=ax)
          ax.set_title("Ocorrências por Cidade")
          ax.set_ylabel("Cidades")
          ax.set_xlabel("Ocorrências")
          st.pyplot(fig)
    
      with graf_b:
          st.subheader("Crimes Mais Frequentes")
          indice_crime = (
               df_filtrado.groupby("tipo_crime")["ocorrencias"].sum().sort_values(ascending=False).reset_index()
          )
          fig, ax = plt.subplots(figsize=(8, 5))

          sns.barplot(data=indice_crime, x="tipo_crime", y="ocorrencias", ax=ax)
          ax.set_title("Crimes mais frequentes")
          ax.set_ylabel("Índice de violência")
          ax.set_xlabel("Tipo de crime")
          ax.tick_params(axis="x", rotation=30)
          st.pyplot(fig)
      
      graf_c, graf_d = st.columns(2)
      with graf_c:
         st.subheader("Heatmap de Horários Críticos")
         df_crime_critico = df_filtrado[df_filtrado['nivel_risco'] == 'Crítico']
         filtro = df_crime_critico.groupby('periodo_dia')['nivel_risco'].count().sort_values(ascending=False).to_frame()
         fig, ax = plt.subplots(figsize=(8, 5))
         sns.heatmap(data=filtro)
         ax.set_xlabel("Nível Crítico")
         ax.set_ylabel("Período do dia")
         st.pyplot(fig)

      with graf_d:
         st.subheader("Comparação renda X Violência")
         renda_violencia = (
             df[['renda_media', 'indice_violencia']]
         )
         fig, ax = plt.subplots(figsize=(8, 5))
         sns.scatterplot(data=renda_violencia, x='renda_media', y='indice_violencia')
         ax.set_xlabel("Renda Média")
         ax.set_ylabel("Índice de Violênca")
         st.pyplot(fig)

    
with tab3:
      st.subheader("Base Filtrada")
      st.dataframe(df_filtrado, use_container_width=True)

st.divider()

st.subheader("Conclusão executiva")
st.write("""
A análise permite identificar quais são as cidades mais críticas e quais são os tipos de crime mais violentos. O dashboard transforma a base de criminaliade em uma ferramenta de apoio à decisão,
permitindo que gestores explorem filtros e encontrem rapidamente oportunidades de redução de criminalidade
e diferenças regionais de ocorrências.
""")
      