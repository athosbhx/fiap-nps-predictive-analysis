# 📊 Tech Challenge Fase 1 — NPS Preditivo em E-commerce

---

## 🎯 Objetivo

Identificar os principais fatores operacionais que influenciam a satisfação do cliente (NPS) em um e-commerce e propor uma abordagem analítica/preditiva para antecipar o nível de satisfação antes da coleta oficial.

---

## 👥 Equipe

* Athos Chagas — RM371204
* Nome 2 — RM XXXX

---

## 📊 Base de Dados

Dataset contendo informações históricas de pedidos, incluindo:

* Dados do cliente (idade, região, tempo de relacionamento)
* Dados do pedido (valor, quantidade, desconto, forma de pagamento)
* Dados logísticos (tempo de entrega, atraso, tentativas de entrega)
* Dados de atendimento (contatos, tempo de resolução, reclamações)
* Indicadores internos (CSAT, recompra)
* Variável alvo: `nps_score` (0 a 10)

---

## 🧠 Metodologia

O projeto foi estruturado em etapas:

1. **Entendimento do negócio**

   * Contextualização do problema
   * Impacto do NPS no e-commerce

2. **Definição da variável target**

   * `nps_score` como indicador de satisfação
   * Criação da variável derivada `nps_class`:

     * 0–6 → Detrator
     * 7–8 → Neutro
     * 9–10 → Promotor

3. **Análise Exploratória de Dados (EDA)**

   * Identificação de padrões e correlações
   * Análise dos principais geradores de detratores
   * Investigação de pontos de ruptura na experiência

4. **Feature Engineering**

   * Criação de variáveis derivadas relevantes
   * Preparação dos dados para modelagem

5. **(Opcional) Modelagem Preditiva**

   * Classificação de clientes (Detrator vs Não-Detrator)
   * Avaliação com métricas de classificação

---

## 📁 Estrutura do Projeto

```bash
nps-predictive-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
│
├── models/
│
├── reports/
│   ├── figures/
│   ├── insights.md
│   └── business_understanding.md
│
├── presentation/
│   └── slides.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔍 Principais Insights

* Atrasos na entrega possuem forte impacto negativo no NPS
* Alto número de contatos com o suporte está associado a clientes detratores
* Tempo elevado de resolução de problemas reduz significativamente a satisfação
* Clientes com maior tempo de relacionamento tendem a apresentar maior NPS

---

## ⚙️ Como reproduzir o projeto

```bash
git clone https://github.com/seu-usuario/nps-predictive-analysis.git
cd nps-predictive-analysis

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
jupyter lab
```

Execute os notebooks na seguinte ordem:

1. `01_eda.ipynb`
2. `02_feature_engineering.ipynb`
3. `03_modeling.ipynb` (opcional)

---

## 📊 Aplicação no Negócio

Os resultados permitem:

* Antecipar clientes com alto risco de insatisfação
* Priorizar ações de atendimento e retenção
* Identificar gargalos operacionais (logística e suporte)
* Apoiar decisões estratégicas para melhoria da experiência

---

## 📺 Apresentação

* Slides: `presentation/slides.pdf`
* Vídeo: [inserir link aqui]

---

## 🛠️ Stack Tecnológica

* Python 3.11
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* jupyter

---

## ⚠️ Limitações

* O NPS é coletado apenas após a experiência
* Possível viés nos dados históricos
* Nem todos os fatores de satisfação são observáveis nos dados


