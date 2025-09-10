#!/usr/bin/env python3
"""aplicação para analisar a taxa de desistência (evasão) do Ensino Médio

Como usar:
 - Instale dependências: pip install -r requirements.txt
 - Execute: python analyze_dropout.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

CSV = 'dropout_school.csv'


def run_analysis():
    df = pd.read_csv(CSV)
    years = df['year'].values
    rates = df['dropout_rate_pct'].values
    coeffs = np.polyfit(years, rates, 1)
    poly = np.poly1d(coeffs)
    years_all = np.arange(2013, 2028)
    pred = poly(years_all)
    # Save a simple plot
    plt.figure(figsize=(10,5))
    plt.scatter(years, rates, label='Observado (2013-2022)')
    plt.plot(years_all, pred, label='Regressão linear (proj. 2013-2027)')
    plt.axvline(2022.5, linestyle='--', linewidth=0.8)
    plt.xlabel('Ano')
    plt.ylabel('Taxa de desistência (%)')
    plt.title('Taxa de desistência anual - Escola Estadual Modelo')
    plt.grid(True, linestyle=':', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig('plot_dropout.png')
    plt.close()
    # Print summary
    print('Coeficientes (slope, intercept):', coeffs)
    print('\nObservado:')
    print(df.to_string(index=False))
    print('\nProjeção 2023-2027:')
    for y, r in zip(years_all, pred):
        if y >= 2023:
            print(y, round(r,2))

if __name__ == '__main__':
    run_analysis()
