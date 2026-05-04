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
fiap-nps-predictive-analysis/
│
├── data/
│   ├── raw/
│   │   └── desafio_nps_fase_1.csv          # base original
│   └── processed/
│       └── Base NPS Tratada.csv            # base com a coluna categoria_nps
│
├── notebooks/
│   ├── 01_EDA_NPS.ipynb                    # análise exploratória + categorização
│   └── 02_Tratamento_de_dados_NPS+Modelagem_Regressao_Linear.ipynb       # split treino/teste estratificado
│
├── reports/
│   └── figures/                            # gráficos exportados da EDA
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

### ✅ Pré-requisitos

Este projeto usa versões fixadas de `pandas==2.2.2` e `numpy==1.26.4`, que possuem wheels (binários pré-compilados) apenas para **Python 3.9 a 3.12**.

> ⚠️ **É obrigatório usar Python 3.12.x.**
> Em Python 3.13 ou superior, o `pip install` tentará compilar `numpy`/`pandas` do zero e falhará — o erro normalmente aparece durante a build do pandas.

* **Versão recomendada:** Python 3.12.x ([download oficial](https://www.python.org/downloads/release/python-3120/))
* Git instalado

---

### 1. Clonar o repositório

```bash
git clone https://github.com/athosbhx/fiap-nps-predictive-analysis.git
cd fiap-nps-predictive-analysis
```

---

### 2. Criar e ativar o ambiente virtual com Python 3.12

> 💡 Se você tiver mais de uma versão do Python instalada, é importante criar a venv apontando explicitamente para a 3.12. Os comandos abaixo fazem exatamente isso.

#### Windows (PowerShell ou CMD):

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

#### Verificar se a venv está usando Python 3.12

Após ativar, execute:

```bash
python --version
```

A saída deve ser algo como `Python 3.12.x`. Se aparecer outra versão, **não prossiga** — recrie a venv apontando para o Python 3.12 conforme acima.

---

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Executar os notebooks

```bash
jupyter lab
```

Ou abra diretamente no VSCode (lembre-se de selecionar o kernel da venv `.venv`).

---

### 5. Ordem de execução

1. `notebooks/01_EDA_NPS.ipynb`
2. `notebooks/02_Tratamento_Dados_NPS.ipynb`


---

## ⚠️ Observações importantes

* Os notebooks devem ser executados em ordem
* Os caminhos utilizados são relativos (`../data/...`)
* Certifique-se de que o dataset está na pasta correta antes de executar
* Sempre ative a venv antes de rodar os notebooks (`.venv\Scripts\activate` no Windows ou `source .venv/bin/activate` no Linux/macOS)

---

## 🛟 Troubleshooting

### "Erro durante a instalação do pandas / numpy"

Sintoma típico durante o `pip install -r requirements.txt`: erro de build envolvendo `pandas`, `numpy`, `meson`, `Cython` ou `Microsoft Visual C++`.

**Causa:** sua venv está usando uma versão de Python **diferente da 3.12** (provavelmente 3.13+). As versões fixadas no `requirements.txt` não possuem wheels para essas versões.

**Solução:**

1. Confirme a versão do Python da venv ativa:
   ```bash
   python --version
   ```
2. Se não for `3.12.x`, desative e remova a venv:
   ```bash
   deactivate
   # Windows
   rmdir /S /Q .venv
   # Linux/macOS
   rm -rf .venv
   ```
3. Recrie usando explicitamente o Python 3.12 (`py -3.12` no Windows ou `python3.12` no Linux/macOS) conforme o passo 2 acima.

### "py não é reconhecido" (Windows)

Reinstale o Python 3.12 marcando a opção **"Add Python to PATH"** e **"Install py launcher"**.

### "python3.12: command not found" (Linux/macOS)

Instale a versão 3.12 antes de continuar:

* **Ubuntu/Debian:** `sudo apt install python3.12 python3.12-venv`
* **macOS (Homebrew):** `brew install python@3.12`

---

## 📊 Aplicação no Negócio

Os resultados permitem:

* Antecipar clientes com alto risco de insatisfação
* Priorizar ações de atendimento e retenção
* Identificar gargalos operacionais (logística e suporte)
* Apoiar decisões estratégicas para melhoria da experiência

---


## 🛠️ Stack Tecnológica

* **Python 3.12.x** (obrigatório — ver seção de pré-requisitos)
* pandas 2.2.2
* numpy 1.26.4
* scikit-learn 1.5.0
* matplotlib 3.9.0
* seaborn 0.13.2
* jupyter / notebook

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
