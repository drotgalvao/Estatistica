import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry

import pycountry

def iso2_to_iso3(iso2):
    try:
        # Primeiro, tente encontrar uma correspondência exata pelo código ISO 2
        country = pycountry.countries.get(alpha_2=iso2)

        # Se não houver correspondência exata, tente encontrar correspondência por correspondência parcial no nome
        if not country:
            country = next((c for c in pycountry.countries if iso2.lower() in c.name.lower()), None)

        if country:
            return country.alpha_3
        else:
            return None
    except (LookupError, KeyError):
        return None



df_idh_undp = pd.read_csv("HDR21-22_Composite_indices_complete_time_series.csv") # lendo o data frame idh
# df_ef_heritage = pd.read_csv("freedom-scores.csv") # lendo o data frame economic freedom da heritage foundation

# # print(df_ef_heritage)

# select_column_heritage = ["ISO Code", "Name", "Index Year", "Overall Score"] # selecao das colunas do data frame economic freedom
# df_ef_heritage = df_ef_heritage[select_column_heritage]
# df_ef_heritage = df_ef_heritage.dropna(subset=['Overall Score'])
# df_ef_heritage['iso3'] = df_ef_heritage['ISO Code'].apply(iso2_to_iso3)	

# df_ef_heritage.loc[df_ef_heritage['Name'] == 'Namibia', 'ISO Code'] = 'NA'
# df_ef_heritage.loc[df_ef_heritage['Name'] == 'Namibia', 'iso3'] = 'NAM'

# df_ef_heritage.loc[df_ef_heritage['Name'] == 'Kosovo', 'ISO Code'] = 'XK'
# df_ef_heritage.loc[df_ef_heritage['Name'] == 'Kosovo', 'iso3'] = 'XKX'


# df = pd.DataFrame(df_ef_heritage)

# # Crie um novo DataFrame com as colunas iniciais
# df_new = df[['iso3', 'Name']].copy()

# # Itere pelos dados e crie colunas para cada ano
# for index, row in df.iterrows():
#     year_column_name = f'ef_{row["Index Year"]}'
#     df_new.loc[df_new['iso3'] == row['iso3'], year_column_name] = row['Overall Score']

# # Preencha valores NaN com 0
# df_new = df_new.fillna(0)



# df = pd.DataFrame(df_new)

# # Lista para controlar os ISO3 já vistos
# iso3_seen = []

# # DataFrame para armazenar as linhas únicas
# df_unique = pd.DataFrame(columns=df.columns)

# for index, row in df.iterrows():
#     iso3 = row['iso3']
#     if iso3 not in iso3_seen:
#         iso3_seen.append(iso3)
#         df_unique = df_unique.append(row, ignore_index=True)

# print(df_unique)



# caminho_saida_excel = 'C:\Programação\Python\Estatistica\df_ef_heritage_filtragem2.xlsx'
# df_unique.to_excel(caminho_saida_excel, index=False)
# print(f'Dados exportados para {caminho_saida_excel}')




# caminho_saida_excel = 'C:\Programação\Python\Estatistica\df_ef_heritage_filtragem.xlsx'

# # Use o método to_excel() para exportar o DataFrame para um arquivo Excel
# df_ef_heritage.to_excel(caminho_saida_excel, index=False)

# print(f'Dados exportados para {caminho_saida_excel}')













df_idh_undp = df_idh_undp.dropna(subset=['hdi_rank_2021'])
colunas_selecionadas = ['iso3', 'country'] + [f'hdi_{ano}' for ano in range(1990, 2022)]
df_idh_undp = df_idh_undp[colunas_selecionadas]


print(df_idh_undp)

caminho_saida_excel = 'C:\Programação\Python\Estatistica\df_idh_filtrado.xlsx'
df_idh_undp.to_excel(caminho_saida_excel, index=False)
print(f'Dados exportados para {caminho_saida_excel}')