# MVP: Análise de Taxa de Desistência - Escola Estadual

### Este projeto é um MVP para aplicar conteúdos de regressão linear e análise de séries temporais em uma atividade de extensão

Arquivos gerados:
- data/dropout_school.csv  => Dados (históricos 2013-2022)
- analyze_dropout.py       => Script principal para rodar a análise e gerar gráfico
- plot_dropout.png         => Gráfico gerado
- report.pdf               => Relatório detalhado (em português) com metodologia e evidências
- requirements.txt         => Dependências Python

Como executar (localmente):
1. Crie um ambiente virtual (recomendado)
2. Instale dependências: `pip install -r requirements.txt`
3. Execute: `python analyze_dropout.py`

-------------------------------------------------

#### 1) clonar ou copiar os arquivos para uma pasta local
#### 2) criar e ativar virtualenv (opcional mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

#### 3) instalar dependências
pip install -r /mnt/data/dropout_mvp/requirements.txt

#### 4) executar a análise
cd /mnt/data/dropout_mvp
python analyze_dropout.py


Obs: o arquivo report.pdf já foi gerado automaticamente e inclui diagnósticos, plano de trabalho,
metodologia, avaliação e instruções sobre como coletar evidências (fotos, listas, etc.).

Sugestão de atividade presencial para cumprir os requisitos:
- Realizar uma oficina de 3 horas com coordenação e professores da escola para apresentar o relatório,
  demonstrar o script em Python e ensinar como atualizar a planilha de evasão.


  ## Como adaptar para a escola real (passos práticos)

Solicite à secretaria escolar os registros anuais: número de matriculados e número de desistências por ano (colunas enrolled e dropouts)

Gere/atualize o CSV data/dropout_school.csv mantendo as colunas: year,enrolled,dropouts,dropout_rate_pct (ou deixe o script calcular dropout_rate_pct = dropouts/enrolled*100).

Rode python analyze_dropout.py para obter nova projeção e plot.

