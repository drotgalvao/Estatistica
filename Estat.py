import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry

# pd.set_option('display.max_rows', None)
df_idh = pd.read_csv("HDR21-22_Composite_indices_complete_time_series.csv") # lendo o data frame idh
# df_ef = pd.read_csv('economicdata1990-2020.csv', skiprows=5)
df_ef = pd.read_excel("IEFtratado.xlsx") # lendo o data frame economic freedom

df2_ef = pd.read_excel("freedom-scores.xlsx") # lendo o data frame economic freedom da heritage
# print(df2_ef)




colunas_desejadas_idh = ['iso3', 'country', 'hdi_2020'] # selecao das colunas do data frame idh
df_idh_selecionado = df_idh[colunas_desejadas_idh] # selecionando as colunas

# print(df_idh_selecionado)

df_idh_classificado = df_idh_selecionado.sort_values(by="hdi_2020", ascending=False).dropna() # classificando o data frame idh em ordem decrescente e excluindo os valores nulos colunas[iso3, country, hdi_2020]

colunas_desejadas_ef = ["ISO_Code", "Year", "Economic Freedom Summary Index"] # selecao das colunas do data frame economic freedom
df_ef_selecionado = df_ef[colunas_desejadas_ef] # selecionando as colunas
tabela_unificada = df_idh_classificado.merge(df_ef_selecionado, left_on='iso3', right_on='ISO_Code') # unificando os data frames pelas colunas que possuem iso3 == ISO_Code

tabela_unificada['Ranking HDI'] = tabela_unificada['hdi_2020'].rank(ascending=False, method='min') # criando a coluna Ranking HDI atraves da coluna hdi_2020 em ordem decrescente

tabela_unificada['Ranking Economic Freedom'] = tabela_unificada['Economic Freedom Summary Index'].rank(ascending=False, method='min') # criando a coluna Ranking Economic Freedom atraves da coluna Economic Freedom Summary Index em ordem decrescente

tabela_unificada.sort_values(by='Ranking HDI', inplace=True) # ordenando a tabela de acordo com o Ranking HDI

# print(tabela_unificada[['country', 'hdi_2020', 'Ranking HDI', 'Economic Freedom Summary Index', 'Ranking Economic Freedom']]) # mostrando a tabela

correlacao_ranking = tabela_unificada[['Ranking HDI', 'Ranking Economic Freedom']].corr(method='pearson') # calculando a correlacao entre ranking de indices
# print(f"Correlacao entre ranking de indices: {correlacao_ranking}")

correlacao_index = tabela_unificada[['hdi_2020', 'Economic Freedom Summary Index']].corr(method='pearson') # calculando a correlacao entre indices
# print(f"Correlacao entre indices: {correlacao_index}")

# pd.set_option('display.max_columns', None) # mostrar todas as colunas do data frame
# print(df_ef)

# cols_to_remove = ['Year', 'ISO_Code', 'Countries', 'Rank', 'Quartile'] + [col for col in df_ef.columns if col.startswith('data')] # removendo colunas que nao serão usadas
# df_ef = df_ef.drop(cols_to_remove, axis=1) # removendo colunas
# print(df_ef.corr(method='pearson'))


# corr_matrix = df_ef.corr(method='pearson') # matriz de correlação

# plt.figure(figsize=(12, 8))  # tamanho do gráfico


# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5) # heatmap 


# plt.title('Mapa de Calor da Matriz de Correlação') # titulo

# plt.show() # mostrar o mapa

def iso2_to_iso3(iso2):
    try:
        country = pycountry.countries.get(alpha_2=iso2)
        if country:
            return country.alpha_3
        else:
            return None
    except (LookupError, KeyError):
        return None



df_2020 = df2_ef[df2_ef['Index Year'] == 2020]
df_2020 = df_2020.dropna(subset=['Overall Score'])
df_2020 = df_2020.sort_values(by='Overall Score', ascending=False)
colunas_desejadas_ef2 = ['Name', 'Short Name', 'ISO Code', 'ISO3', 'Index Year', 'Overall Score', 'Ranking EF']

df_2020['ISO3'] = df_2020['ISO Code'].apply(iso2_to_iso3)

df_2020['Ranking EF'] = df_2020['Overall Score'].rank(ascending=False, method='min')

df_2020 = df_2020.sort_values(by='Ranking EF')

# print (df_2020 [ colunas_desejadas_ef2 ])




df_idh_drop = df_idh.dropna(subset=['hdi_rank_2021'])
df_idh_drop['Ranking HDI 2020'] = df_idh_drop['hdi_2020'].rank(ascending=False, method='min')
colunas_desejadas_idh2 = ['iso3', 'country', 'hdi_2020', 'Ranking HDI 2020'] 
df_idh_selecionado2 = df_idh_drop[colunas_desejadas_idh2]

df_idh_selecionado2 = df_idh_selecionado2.sort_values(by='Ranking HDI 2020')




df_merged = df_2020.merge(df_idh_selecionado2, left_on='ISO3', right_on='iso3', how='inner')


colunas_selecionadas_final = ['Name', 'ISO3', 'Index Year', 'Overall Score', 'Ranking EF', 'hdi_2020', 'Ranking HDI 2020']
df_selecionado = df_merged[colunas_selecionadas_final]

correlation_rankings = df_selecionado[['Ranking EF', 'Ranking HDI 2020']].corr(method='pearson')
correlation_overall_hdi = df_selecionado[['Overall Score', 'hdi_2020']].corr(method='pearson')

print("Correlação entre os rankings:")
print(correlation_rankings)

print("\nCorrelação entre Overall Score e HDI 2020:")
print(correlation_overall_hdi)

