# Dashboard Executivo de Criminalidade em Grandes Cidades Brasileiras

## 1. Descrição do Projeto

Este projeto apresenta uma análise executiva sobre criminalidade em grandes cidades brasileiras entre os anos de 2015 e 2024.

O objetivo é identificar padrões de violência, regiões críticas, tipos de crime mais frequentes e possíveis relações entre fatores socioeconômicos e índices de criminalidade.

O projeto foi desenvolvido como referência para a avaliação G2 da disciplina **Linguagem de Programação — Análise e Visualização de Dados com Python**.

A proposta é demonstrar um fluxo completo de análise de dados, envolvendo:

1. entendimento do problema;
2. leitura e preparação dos dados;
3. criação de indicadores (KPIs);
4. análise exploratória;
5. visualização de dados;
6. construção de dashboard interativo;
7. publicação em repositório GitHub;
9. disponibilização do dashboard online.

---

## 2. Problema de Negócio

A criminalidade é um dos principais desafios enfrentados pelas grandes cidades brasileiras, impactando diretamente a segurança pública, a qualidade de vida da população e o desenvolvimento econômico.

Este projeto busca responder questões estratégicas como:

* Quais cidades apresentam maior número de ocorrências?
* Quais tipos de crime são mais frequentes?
* Existem horários mais críticos para ocorrência de crimes?
* A criminalidade aumentou ou diminuiu ao longo dos anos?
* Existem diferenças significativas entre regiões do Brasil?
* Há relação entre renda média e criminalidade?
* Quais regiões apresentam maiores índices de violência?

---

## 3. Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* Numpy
* Plotly
* Streamlit
* GitHub

---

## 4. Estrutura do Projeto

```text
projeto-criminalidade/
│
├── app.py
├── requirements.txt
├── README.md
├── site/
|        └── index.html
|        └── style.css
├── dados/
│   └── simulacao_criminalidade_brasil.csv
│
├── notebooks/
│  └── analise_criminalidade.ipynb
```

---

## 5. Como Executar Localmente

### 5.1 Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd projeto-criminalidade
```

### 5.2 Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5.3 Executar o Dashboard

```bash
streamlit run app.py
```

---

## 6. KPIs Utilizados

| KPI                          | Descrição                                    |
| ---------------------------- | -------------------------------------------- |
| Total de Ocorrências         | Soma geral das ocorrências registradas       |
| Cidade Mais Violenta         | Cidade com maior quantidade de ocorrências   |
| Tipo de Crime Mais Frequente | Crime com maior incidência                   |
| Total de Vítimas             | Soma total de vítimas registradas            |
| Índice Médio de Violência    | Média geral do índice de violência           |
| Região Mais Crítica          | Região com maior concentração de ocorrências |

---

## 7. Funcionalidades do Dashboard

O dashboard possui:

* filtros por ano;
* filtros por mês;
* filtros por região;
* filtros por estado (UF);
* filtros por cidade;
* filtros por tipo de crime;
* filtros por nível de risco;
* KPIs dinâmicos;
* gráficos temporais;
* análise regional;
* comparação entre cidades;
* análise por tipo de crime;
* correlação entre renda e violência;
* interpretaçãodos resultados e análise do negócio;

---

## 8. Análises Desenvolvidas

### Evolução Temporal

Análise da evolução da criminalidade ao longo dos anos para identificar tendências de crescimento ou redução.

### Comparação Regional

Comparação entre as regiões brasileiras para identificar áreas mais críticas.

### Comparação entre Cidades

Ranking das cidades com maior número de ocorrências registradas.

### Tipos de Crime

Análise dos crimes mais frequentes e seu impacto nas diferentes localidades.

### Horários Críticos

Identificação dos períodos do dia com maior concentração de ocorrências.

### Relação entre Renda e Criminalidade

Investigação da possível correlação entre renda média regional e índices de violência.

### Áreas de Maior Risco

Identificação de regiões classificadas com níveis de risco Alto ou Crítico.

---



## 9. Insights Alcançados

O projeto permite identificar:

* cidades com maior concentração de ocorrências;
* crimes mais recorrentes;
* horários de maior risco;
* regiões mais vulneráveis;
* comportamento temporal da criminalidade;
* possíveis relações entre fatores socioeconômicos e violência;
* áreas prioritárias para ações de segurança pública.

---

## 10. Dashboard Streamlit

O dashboard foi desenvolvido para fornecer uma visão executiva da criminalidade no Brasil, permitindo que gestores e analistas explorem os dados de forma interativa.

A aplicação contém:

* descrição do problema;
* indicadores estratégicos;
* filtros dinâmicos;
* gráficos interativos;
* interpretações analíticas;
* conclusão executiva.

---

## 11. Notebook de Análise

O notebook contém:

1. Introdução;
2. Contextualização da segurança pública;
3. Descrição da base de dados;
4. Leitura dos dados;
5. Limpeza e preparação;
6. Engenharia de atributos;
7. Criação dos KPIs;
8. Visualizações;
9. Interpretação dos resultados;
10. Conclusão.

---


## 12. Objetivo Pedagógico

Este projeto demonstra como utilizar técnicas de análise e visualização de dados para compreender padrões de criminalidade e apoiar a tomada de decisão baseada em dados.

Mais do que construir gráficos, o objetivo é desenvolver a capacidade de:

* interpretar indicadores de segurança pública;
* identificar padrões de violência;
* compreender fatores sociais relacionados à criminalidade;
* comunicar resultados de forma clara e objetiva;
* construir aplicações analíticas profissionais utilizando Python.
