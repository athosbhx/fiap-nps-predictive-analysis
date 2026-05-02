# 📊 Tech Challenge Fase 1 — NPS Preditivo em E-commerce

---

## 🎯 Objetivo

Identificar os principais fatores operacionais que influenciam a satisfação do cliente (NPS) em um e-commerce e propor uma abordagem analítica/preditiva para antecipar o nível de satisfação antes da coleta oficial.

---

## 👥 Equipe

* Athos Chagas — RM371204
* Luca Prado — RM370843
* Pedro Olyntho — RM373821
* Higor Vieira — RM371392

---

## 📊 Base de Dados

O dataset contém informações históricas sobre pedidos, logística e atendimento ao cliente.

### Principais variáveis:

* **Cliente:** idade, região, tempo de relacionamento
* **Pedido:** valor, quantidade de itens, desconto, forma de pagamento
* **Logística:** tempo de entrega, atraso, tentativas de entrega
* **Atendimento:** contatos, tempo de resolução, reclamações
* **Indicadores internos:** CSAT, recompra
* **Target:** `nps_score` (0 a 10)

> 📁 O arquivo de dados deve ser colocado em:

```
data/raw/nps_dataset.csv
```

---

## 🧠 Metodologia

O projeto foi estruturado nas seguintes etapas:

### 1. Entendimento do negócio

* Contextualização do problema
* Importância do NPS no e-commerce

### 2. Definição da variável target

* Utilização do `nps_score`
* Criação da variável derivada `nps_class`:

  * 0–6 → Detrator
  * 7–8 → Neutro
  * 9–10 → Promotor

### 3. Análise Exploratória de Dados (EDA)

* Identificação de padrões e correlações
* Principais fatores que impactam o NPS
* Análise de detratores e pontos de ruptura

### 4. Feature Engineering

* Criação de variáveis derivadas
* Preparação dos dados para modelagem

---

## 📁 Estrutura do Projeto

```
nps-predictive-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│   
├── notebooks/
│   ├── 01_EDA_NPS.ipynb
│   └── 02_Tratamento_Dados_NPS.ipynb
│   
│
├── src/
|   ├── utils
│   └── init
│
├── reports/
│   └── figures
|
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔍 Principais Insights

* Atrasos na entrega possuem forte impacto negativo no NPS
* Alto número de contatos com suporte está associado a detratores
* Tempo elevado de resolução reduz significativamente a satisfação
* Clientes com maior tempo de relacionamento tendem a maior NPS

---

## ⚙️ Como reproduzir o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/athosbhx/fiap-nps-predictive-analysis.git
cd fiap-nps-predictive-analysis
```

---

### 2. Criar e ativar ambiente virtual

```bash
python -m venv .venv
```

#### Windows:

```bash
.venv\Scripts\activate
```

#### Linux/Mac:

```bash
source .venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar os notebooks

```bash
jupyter lab
```

Ou abra diretamente no VSCode.

---

### 5. Ordem de execução

1. `notebooks/01_EDA_NPS.ipynb`
2. `notebooks/02_Tratamento_Dados_NPS.ipynb`


---

## ⚠️ Observações importantes

* Os notebooks devem ser executados em ordem
* Os caminhos utilizados são relativos (`../data/...`)
* Certifique-se de que o dataset está na pasta correta antes de executar

---

## 📊 Aplicação no Negócio

Os resultados permitem:

* Antecipar clientes com alto risco de insatisfação
* Priorizar ações de atendimento e retenção
* Identificar gargalos operacionais (logística e suporte)
* Apoiar decisões estratégicas para melhoria da experiência

---


## 🛠️ Stack Tecnológica

* Python 
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
* Nem todos os fatores de satisfação são observáveis

---

## 🔁 Próximos Passos

* Evoluir o modelo preditivo
* Testar novos algoritmos
* Implementar pipeline automatizada
* Integrar com sistemas de decisão em tempo real
