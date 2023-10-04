import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_excel("df_merged.xlsx")  #
print(df)

correlations = []

print("##########################")
for year in range(1995, 2021):
    hdi = f'hdi_{year}'
    ef = f'ef_{year}'

    select_columns = ['iso3', 'country', hdi, ef]
    df_year = df[select_columns].dropna()

    # Cálculo dos rankings
    df_year[f'{hdi}_rank'] = df_year[hdi].rank(ascending=False)
    df_year[f'{ef}_rank'] = df_year[ef].rank(ascending=False)

    # Ordena o DataFrame pelos rankings
    df_year = df_year.sort_values(by=[f'{hdi}_rank', f'{ef}_rank'])

    # Exibe o DataFrame
    print(f'DataFrame para o ano {year}:')
    print(df_year)

    # Cálculo da correlação
    correlation = df_year[[f'{hdi}_rank', f'{ef}_rank']].corr(method='pearson')
    print(f'Correlação para o ano {year}:')
    print(correlation)
    print('-' * 50)
    correlations.append(correlation.iloc[0, 1])


years = list(range(1995, 2021))
plt.figure(figsize=(12, 6))
plt.bar(years, correlations, color='skyblue')
plt.xlabel('Ano')
plt.ylabel('Correlação')
plt.title('Correlações ao Longo dos Anos')
plt.xticks(years, rotation=45)
plt.ylim(-1, 1)
plt.tight_layout()
plt.show()

### DEFINICAO DE QUADRANTE 1-46, 47-92, 98-138, 139-184
### BONS EXEMPLOS DE CORRELACAO: VEN, USA, JPN, SGP, HKG, NOR, SWE, YEM, IRL, EST, IND, CHN
### EXEMPLO MAIS NEUTROS: BRA, ITA,
### MAUS EXEMPLOS DE CORRELACAO:


iso3 = "USA"
filter = df["iso3"] == iso3

hdi_ranks = []
ef_ranks = []
years = []

# print(df[us_filter])




years = range(1996, 2022)

for year in years:
    hdi_col = f"hdi_{year}"
    ef_col = f"ef_{year}"
    hdi_rank_col = f"hdi_{year}_rank"
    ef_rank_col = f"ef_{year}_rank"

    df[hdi_rank_col] = df[hdi_col].rank(ascending=False)
    df[ef_rank_col] = df[ef_col].rank(ascending=False)

df_filter = df[filter]

years = list(range(1996, 2022))
ef_ranks = df_filter[["ef_" + str(year) + "_rank" for year in years]].values.flatten()
hdi_ranks = df_filter[["hdi_" + str(year) + "_rank" for year in years]].values.flatten()

# Cria o gráfico
plt.figure(figsize=(12, 6))
plt.plot(years, ef_ranks, label="EF Rank", marker="o")
plt.plot(years, hdi_ranks, label="HDI Rank", marker="s")

plt.axhline(y=46, color="r", linestyle="--", label="Limite Quadrante 1")
plt.axhline(y=92, color="g", linestyle="--", label="Limite Quadrante 2")
plt.axhline(y=138, color="b", linestyle="--", label="Limite Quadrante 3")
plt.axhline(y=184, color="y", linestyle="--", label="Limite Quadrante 4")

plt.xlabel("Ano")
plt.ylabel("Ranking")
plt.title(f'Ranking de EF e HDI no(a) {df_filter["country"].values[0]} (1996-2021)')
plt.gca().invert_yaxis()
plt.legend()
plt.grid(True)
plt.show()

print(df_filter)
# caminho_saida_excel = 'C:\Programação\Python\Estatistica\\ranking_todos_anos.xlsx'
# df.to_excel(caminho_saida_excel, index=False)
# print(f'Dados exportados para {caminho_saida_excel}')


# correlation = df[hdi].corr(df[ef], method='pearson')
# print(correlation)

# correlation_rankings_heritage = merged_df_heritage[['Ranking HDI 2020', 'Ranking Economic Freedom']].corr(method='pearson')


# hdi_columns = [f'hdi_{year}' for year in range(1995, 2024)]
# ef_columns = [f'ef_{year}' for year in range(1995, 2024)]

# # Calcular a matriz de correlação
# correlation_matrix = df[["hdi_columns", "ef_columns"]].corr(method='pearson')
# print(df[correlation_matrix])


# Exibir a matriz de correlação
# print(correlation_matrix)

# sns.set(style="white")

# # Crie um mapa de calor (heatmap) da matriz de correlação
# plt.figure(figsize=(12, 10))  # Ajuste o tamanho da figura conforme necessário
# annot_kws = {"size": 5}  # Ajuste o tamanho da fonte conforme necessário

# sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", annot_kws=annot_kws)


# # Defina os rótulos dos eixos e o título
# plt.xlabel("Ano HDI")
# plt.ylabel("Ano EF")
# plt.title("Matriz de Correlação entre HDI e EF")

# # Exiba o plot
# plt.show()



############################ REGRESSAO LINEAR ##############################################

# Dados de entrada para a regressão
X = [[year] for year in years]  # Anos como entrada
y_ef = ef_ranks  # Rankings do EF como saída
y_hdi = hdi_ranks  # Rankings do HDI como saída

# Realize a regressão linear para o EF Rank
reg_ef = LinearRegression().fit(X, y_ef)

# Realize a regressão linear para o HDI Rank
reg_hdi = LinearRegression().fit(X, y_hdi)

# Predições dos rankings para os anos seguintes
years_pred = [[year] for year in range(2022, 2030)]  # Anos futuros
ef_rank_pred = reg_ef.predict(years_pred)
hdi_rank_pred = reg_hdi.predict(years_pred)

# Cria o gráfico
plt.figure(figsize=(12, 6))
plt.plot(years, ef_ranks, label="EF Rank (1996-2021)", marker="o")
plt.plot(years, hdi_ranks, label="HDI Rank (1996-2021)", marker="s")
plt.plot(years_pred, ef_rank_pred, label="EF Rank Predito (2022-2029)", linestyle="--", marker="o")
plt.plot(years_pred, hdi_rank_pred, label="HDI Rank Predito (2022-2029)", linestyle="--", marker="s")

# Linhas dos quadrantes com cores diferentes
plt.axhline(y=46, color="r", linestyle="--", label="Limite Quadrante 1")
plt.axhline(y=92, color="g", linestyle="--", label="Limite Quadrante 2")
plt.axhline(y=138, color="b", linestyle="--", label="Limite Quadrante 3")
plt.axhline(y=184, color="y", linestyle="--", label="Limite Quadrante 4")

plt.xlabel("Ano")
plt.ylabel("Ranking")
plt.title(f'Ranking de EF e HDI no(a) {df_filter["country"].values[0]} (1996-2029)')
plt.gca().invert_yaxis()
plt.legend()
plt.grid(True)
plt.show()