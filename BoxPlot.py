import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("df_idh_filtrado.xlsx")


idh_2021 = df[["iso3", "country", "hdi_2021"]]

idh_2021_sorted = idh_2021.sort_values(by="hdi_2021", ascending=False)

print(idh_2021_sorted)


####################################### TOP 20 ############################################
top_20_idh = idh_2021_sorted.head(20)

print("Paises do Top 20:")
print(top_20_idh)

####################################### G20 ############################################
g20_countries = [
    "ARG",
    "AUS",
    "BRA",
    "CAN",
    "CHN",
    "FRA",
    "DEU",
    "IND",
    "IDN",
    "ITA",
    "JPN",
    "MEX",
    "RUS",
    "SAU",
    "ZAF",
    "KOR",
    "TUR",
    "GBR",
    "USA",
]
g20_df = idh_2021[idh_2021["iso3"].isin(g20_countries)]

print("Paises do G20:")
print(g20_df)


########################################## BOX PLOT G20 VS TOP 20 ############################################

# plt.figure(figsize=(12, 6))

# positions = [1, 2]

# medians_g20 = g20_df['hdi_2021'].median()
# medians_top_20 = top_20_idh['hdi_2021'].median()

# plt.boxplot([g20_df['hdi_2021'], top_20_idh['hdi_2021']], positions=positions, widths=0.6, labels=['G20', 'Top 20'])

# plt.title('Box Plots do IDH dos Países do G20 e Top 20 em 2021')
# plt.ylabel('IDH (Índice de Desenvolvimento Humano)')

# plt.tight_layout()

# plt.show()

######################################## BOX PLOT G20 VS TOP 20 VS MUNDO ############################################

plt.figure(figsize=(12, 6))

positions = [1, 2, 3]

medians_g20 = g20_df['hdi_2021'].median()
medians_top_20 = top_20_idh['hdi_2021'].median()
medians_sorted = idh_2021_sorted['hdi_2021'].median()

plt.boxplot([g20_df['hdi_2021'], top_20_idh['hdi_2021'], idh_2021_sorted['hdi_2021']], positions=positions, widths=0.6, labels=['G20', 'Top 20', 'MUNDO'])

plt.title('Box Plots do IDH dos Países do G20, Top 20 e Mundo em 2021')
plt.ylabel('IDH (Índice de Desenvolvimento Humano)')

plt.tight_layout()

plt.show()