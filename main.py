import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy import special
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score

df = pd.read_csv(r'C:\Users\Joao\Desktop\Projetos\Projetos Ciencia de Dados\1. Predição de Churn de Clientes\WA_Fn-UseC_-Telco-Customer-Churn.xls')

