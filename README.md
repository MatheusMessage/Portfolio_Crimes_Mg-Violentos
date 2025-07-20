# 🔍 Análise e Previsão de Crimes Violentos em Minas Gerais (2012–2025)

Este projeto realiza uma análise exploratória detalhada e modelagem preditiva sobre os registros de crimes violentos em Minas Gerais, com foco especial na cidade de Uberlândia. O trabalho utiliza dados oficiais disponibilizados pelo governo de Minas Gerais e pelo IBGE, abrangendo o período de 2012 a 2024, com previsão para o ano de 2025.

## 📁 Estrutura do Projeto

````
Crimes_Violentos_MG/
├── data/
│ ├── raw/ # Dados originais
│ ├── processed/ # Dados tratados e unificados
│ └── database/ # Bancos de dados SQLite
├── docs/ # Documentos auxiliares (IBGE, imagens, etc.)
├── notebooks/
│ ├── 01_exploracao_dados.ipynb
│ ├── 02_limpeza_tratamento.ipynb
│ ├── 03_conversao_ajustes_sql.ipynb
│ ├── 04_visualizacoes.ipynb
│ └── 05_conclusao.ipynb
├── src/ # Scripts auxiliares (.py)
├── dashboard/ # Dashboard interativo com Dash (em desenvolvimento)
├── .gitignore
├── README.md
└── requirements.txt
````

## 🧪 Tecnologias Utilizadas

- Python 3.10+
- Pandas, NumPy, SQLite3
- Plotly, Seaborn, Matplotlib
- Scikit-learn, Statsmodels (ARIMA)
- Jupyter Notebooks

## 📊 Etapas Realizadas

- **Importação e limpeza de dados** dos crimes violentos e municípios IBGE.
- **Unificação e normalização** com base em códigos oficiais dos municípios.
- Criação de **bancos SQLite** para facilitar a consulta e reuso.
- Análises exploratórias por ano, município e natureza do crime.
- Previsões com **Regressão Linear, ARIMA e Random Forest**.
- Geração de **indicadores ajustados por população** (crimes por 100 mil habitantes).
- Visualizações interativas com **Plotly** e gráficos explicativos.

## 🔮 Resultados Previstos para 2025

- **Total de crimes estimado:** ~32.396 (modelo ARIMA)
- **Intervalo de confiança (95%):** entre ~4.604 e ~60.188
- **Ranking das naturezas mais recorrentes (previsão 2025):**

| Natureza                               | Previsão 2025 | Crimes 2024 | Variação (%) |
|----------------------------------------|---------------|-------------|--------------|
| Roubo Consumado                        | 18.647        | 18.595      | +0.28%       |
| Estupro de Vulnerável Consumado        | 3.657         | 3.600       | +1.59%       |
| Homicídio Tentado                      | 3.383         | 3.009       | +12.44%      |
| Homicídio Consumado                    | 2.708         | 2.635       | +2.81%       |
| Roubo Tentado                          | 1.437         | 1.171       | +22.74%      |
| Estupro Consumado                      | 1.436         | 1.309       | +9.71%       |

> ⚠️ **Aviso:** Os resultados são fruto de modelagens estatísticas com base em dados históricos e não devem ser interpretados como previsões absolutas. O objetivo é exclusivamente educacional e informativo.

## 🧠 Aprendizados Técnicos

-Gerenciamento eficiente de dados com SQLite: Estruturei e utilizei bancos de dados SQLite para armazenar, consultar e integrar grandes volumes de dados brutos e tratados, garantindo reuso, consistência e escalabilidade durante todas as fases da análise.

-Tratamento e limpeza avançada de dados: Desenvolvi rotinas para padronização textual, remoção de acentuação, normalização de nomes de municípios e integração de bases heterogêneas (dados de crimes e IBGE), o que foi fundamental para evitar inconsistências e duplicações.

-Modelagem preditiva com múltiplas técnicas: Implementei três abordagens de previsão — Regressão Linear, ARIMA e Random Forest — e realizei backtesting para validar e comparar seus desempenhos, garantindo uma escolha informada do melhor modelo para previsão de crimes em Minas Gerais.

-Análise de séries temporais e previsão com intervalos de confiança: Aprofundei o uso de modelos ARIMA para séries temporais e aprendi a interpretar e apresentar previsões junto com seus intervalos de confiança, evidenciando a incerteza inerente às previsões estatísticas.

-Visualizações interativas e informativas com Plotly e Matplotlib: Criei gráficos dinâmicos e visualmente atraentes, com anotações claras, legendas e uso de cores adequadas para facilitar a interpretação dos dados por diferentes públicos.

-Documentação e comunicação clara: Além da análise técnica, pratiquei a elaboração de narrativas coerentes para apresentar resultados, riscos e limitações, assegurando que os insights fossem acessíveis e contextualizados para tomadas de decisão.

## 🛡️ Ética e Responsabilidade

> As análises realizadas neste projeto envolvem dados sensíveis. Todo o tratamento foi feito com foco técnico, sem juízo de valor ou generalizações. A interpretação dos dados deve considerar o contexto regional, social e econômico. Este trabalho é **educacional** e não tem caráter preditivo oficial.

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/Portfolio_Crimes_Mg-Violentos.git

Instale as dependências:
pip install -r requirements.txt

Execute os notebooks na pasta /notebooks/ seguindo a ordem.
