# Projeto de Predição de Churn de Clientes

Este projeto tem como objetivo prever quais clientes de uma empresa de telecomunicações têm alta probabilidade de cancelar seus serviços (churn). O modelo de Machine Learning foi desenvolvido usando Python e o ecossistema Scikit-learn, e é servido através de uma API REST simples construída com Flask.

## Estrutura do Projeto

- `churn_model.ipynb`: Notebook Jupyter que contém a análise exploratória de dados (EDA), o pré-processamento, o treinamento, a avaliação e o salvamento do modelo de machine learning.
- `main.py`: 
- `model/`: Pasta que armazena o modelo de machine learning serializado (`.pkl`).

## Como Rodar o Projeto

### 1. Preparação
Certifique-se de que você tem o Python instalado. Recomenda-se criar um ambiente virtual.

```bash

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
