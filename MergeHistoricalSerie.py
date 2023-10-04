import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry

df_idh = pd.read_excel("df_idh_filtrado.xlsx") # 
df_ef_heritage = pd.read_excel("df_ef_heritage_filtragem2.xlsx") # 

# print(df_idh)
# print(df_ef_heritage)

df_idh.set_index('iso3', inplace=True)
df_ef_heritage.set_index('iso3', inplace=True)

df_merged = df_idh.join(df_ef_heritage, how='right')

df_merged.reset_index(inplace=True)


print(df_merged)

caminho_saida_excel = 'C:\Programação\Python\Estatistica\df_merged.xlsx'
df_merged.to_excel(caminho_saida_excel, index=False)
print(f'Dados exportados para {caminho_saida_excel}')