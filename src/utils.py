"""
utils.py — Funções auxiliares reutilizáveis para o projeto NPS Preditivo
FIAP PosTech — Tech Challenge Fase 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


# ──────────────────────────────────────────────────────────────────────────────
# Funções de preparação de dados
# ──────────────────────────────────────────────────────────────────────────────

def carregar_dados(caminho: str) -> pd.DataFrame:
    """
    Carrega o CSV de NPS e ajusta os tipos das colunas de ID.

    Args:
        caminho: Caminho relativo ou absoluto para o arquivo CSV.

    Returns:
        DataFrame com os dados carregados e tipos corrigidos.
    """
    df = pd.read_csv(caminho)
    df['customer_id'] = df['customer_id'].astype('str')
    df['order_id'] = df['order_id'].astype('str')
    return df


def categorizar_nps(score: float) -> str:
    """
    Classifica uma nota de NPS em Detrator, Neutro ou Promotor.

    Args:
        score: Nota NPS entre 0 e 10.

    Returns:
        String com a categoria do cliente.
    """
    if score < 7:
        return 'Detrator'
    elif score < 9:
        return 'Neutro'
    else:
        return 'Promotor'


def adicionar_categoria_nps(df: pd.DataFrame, coluna_nps: str = 'nps_score') -> pd.DataFrame:
    """
    Adiciona a coluna 'categoria_nps' ao DataFrame.

    Args:
        df: DataFrame com a coluna de NPS.
        coluna_nps: Nome da coluna com a nota de NPS.

    Returns:
        DataFrame com a nova coluna 'categoria_nps'.
    """
    df = df.copy()
    df['categoria_nps'] = df[coluna_nps].apply(categorizar_nps)
    return df


# ──────────────────────────────────────────────────────────────────────────────
# Funções de visualização
# ──────────────────────────────────────────────────────────────────────────────

PALETA_NPS = {
    'Detrator': '#e74c3c',
    'Neutro': '#f1c40f',
    'Promotor': '#2ecc71'
}


def plotar_distribuicao_nps(df: pd.DataFrame, salvar_em: str = None):
    """
    Plota o histograma da distribuição de NPS com cores por categoria.

    Args:
        df: DataFrame com colunas 'nps_score' e 'categoria_nps'.
        salvar_em: Caminho para salvar a imagem (opcional).
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=df, x='nps_score', hue='categoria_nps',
                 multiple='stack', palette=PALETA_NPS, ax=ax)
    ax.set_title('Distribuição do NPS Score', fontsize=14)
    ax.set_xlabel('NPS Score')
    ax.set_ylabel('Frequência')
    plt.tight_layout()
    if salvar_em:
        plt.savefig(salvar_em, dpi=150, bbox_inches='tight')
    plt.show()


def plotar_correlacao_nps(df: pd.DataFrame, salvar_em: str = None):
    """
    Plota a correlação de Spearman de todas as variáveis numéricas com o NPS.

    Args:
        df: DataFrame numérico com coluna 'nps_score'.
        salvar_em: Caminho para salvar a imagem (opcional).
    """
    df_num = df.select_dtypes(include=['number'])
    corr = df_num.corr(method='spearman')['nps_score'].sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 10))
    sns.heatmap(corr.to_frame(), annot=True, cmap='Spectral', center=0,
                fmt='.2f', ax=ax)
    ax.set_title('Correlação com NPS (Spearman)', fontsize=14)
    plt.tight_layout()
    if salvar_em:
        plt.savefig(salvar_em, dpi=150, bbox_inches='tight')
    plt.show()


def plotar_matriz_confusao(y_true, y_pred, labels: list, salvar_em: str = None):
    """
    Plota a matriz de confusão do modelo.

    Args:
        y_true: Valores reais.
        y_pred: Valores preditos.
        labels: Lista de rótulos das classes.
        salvar_em: Caminho para salvar a imagem (opcional).
    """
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(7, 5))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(ax=ax, cmap='Blues', colorbar=False)
    ax.set_title('Matriz de Confusão', fontsize=14, pad=12)
    plt.tight_layout()
    if salvar_em:
        plt.savefig(salvar_em, dpi=150, bbox_inches='tight')
    plt.show()


def plotar_feature_importance(modelo, feature_names: list, salvar_em: str = None):
    """
    Plota a importância das variáveis do modelo.

    Args:
        modelo: Modelo treinado com atributo feature_importances_.
        feature_names: Lista com nomes das features.
        salvar_em: Caminho para salvar a imagem (opcional).
    """
    importancias = pd.Series(modelo.feature_importances_, index=feature_names).sort_values()
    mediana = importancias.median()
    cores = ['#e74c3c' if v > mediana else '#85c1e9' for v in importancias]

    fig, ax = plt.subplots(figsize=(9, 6))
    importancias.plot(kind='barh', ax=ax, color=cores)
    ax.axvline(mediana, color='gray', linestyle='--', linewidth=1, label='Mediana')
    ax.set_title('Importância das Variáveis', fontsize=14)
    ax.set_xlabel('Importância relativa')
    ax.legend()
    plt.tight_layout()
    if salvar_em:
        plt.savefig(salvar_em, dpi=150, bbox_inches='tight')
    plt.show()


# ──────────────────────────────────────────────────────────────────────────────
# Funções de avaliação
# ──────────────────────────────────────────────────────────────────────────────

def avaliar_modelo(y_true, y_pred, nome_modelo: str = 'Modelo'):
    """
    Exibe o relatório de classificação completo.

    Args:
        y_true: Valores reais.
        y_pred: Valores preditos.
        nome_modelo: Nome do modelo para exibição.
    """
    print(f'══════════════════════════════════════')
    print(f'  Avaliação: {nome_modelo}')
    print(f'══════════════════════════════════════')
    print(classification_report(y_true, y_pred))
