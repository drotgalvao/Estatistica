import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry

df_idh_undp = pd.read_csv("HDR21-22_Composite_indices_complete_time_series.csv") # lendo o data frame idh
df_ef_fraser = pd.read_excel("IEFtratado.xlsx") # lendo o data frame economic freedom da fraser
df_ef_heritage = pd.read_excel("freedom-scores.xlsx") # lendo o data frame economic freedom da heritage foundation

def iso2_to_iso3(iso2): # função para converter iso2 para iso3 dos paises
    try:
        country = pycountry.countries.get(alpha_2=iso2)
        if country:
            return country.alpha_3
        else:
            return None
    except (LookupError, KeyError):
        return None
    

# TRATAMENTO DO DATAFRAME IDH ############################################################################################################
# print(df_idh_undp) # [206 rows x 1008 columns]
 #colunas
 #iso3,country,hdicode,region
 # ,hdi_rank_2021
 # ,hdi_1990,hdi_1991,hdi_1992,hdi_1993,hdi_1994,hdi_1995,hdi_1996,hdi_1997,hdi_1998,hdi_1999,hdi_2000,hdi_2001,hdi_2002,hdi_2003,hdi_2004,hdi_2005,hdi_2006,hdi_2007,hdi_2008,hdi_2009,hdi_2010,hdi_2011,hdi_2012,hdi_2013,hdi_2014,hdi_2015,hdi_2016,hdi_2017,hdi_2018,hdi_2019,hdi_2020,hdi_2021
 # ,le_1990,le_1991,le_1992,le_1993,le_1994,le_1995,le_1996,le_1997,le_1998,le_1999,le_2000,le_2001,le_2002,le_2003,le_2004,le_2005,le_2006,le_2007,le_2008,le_2009,le_2010,le_2011,le_2012,le_2013,le_2014,le_2015,le_2016,le_2017,le_2018,le_2019,le_2020,le_2021
 # ,eys_1990,eys_1991,eys_1992,eys_1993,eys_1994,eys_1995,eys_1996,eys_1997,eys_1998,eys_1999,eys_2000,eys_2001,eys_2002,eys_2003,eys_2004,eys_2005,eys_2006,eys_2007,eys_2008,eys_2009,eys_2010,eys_2011,eys_2012,eys_2013,eys_2014,eys_2015,eys_2016,eys_2017,eys_2018,eys_2019,eys_2020,eys_2021
 # ,mys_1990,mys_1991,mys_1992,mys_1993,mys_1994,mys_1995,mys_1996,mys_1997,mys_1998,mys_1999,mys_2000,mys_2001,mys_2002,mys_2003,mys_2004,mys_2005,mys_2006,mys_2007,mys_2008,mys_2009,mys_2010,mys_2011,mys_2012,mys_2013,mys_2014,mys_2015,mys_2016,mys_2017,mys_2018,mys_2019,mys_2020,mys_2021
 # ,gnipc_1990,gnipc_1991,gnipc_1992,gnipc_1993,gnipc_1994,gnipc_1995,gnipc_1996,gnipc_1997,gnipc_1998,gnipc_1999,gnipc_2000,gnipc_2001,gnipc_2002,gnipc_2003,gnipc_2004,gnipc_2005,gnipc_2006,gnipc_2007,gnipc_2008,gnipc_2009,gnipc_2010,gnipc_2011,gnipc_2012,gnipc_2013,gnipc_2014,gnipc_2015,gnipc_2016,gnipc_2017,gnipc_2018,gnipc_2019,gnipc_2020,gnipc_2021
 # ,gdi_group_2021
 # ,gdi_1990,gdi_1991,gdi_1992,gdi_1993,gdi_1994,gdi_1995,gdi_1996,gdi_1997,gdi_1998,gdi_1999,gdi_2000,gdi_2001,gdi_2002,gdi_2003,gdi_2004,gdi_2005,gdi_2006,gdi_2007,gdi_2008,gdi_2009,gdi_2010,gdi_2011,gdi_2012,gdi_2013,gdi_2014,gdi_2015,gdi_2016,gdi_2017,gdi_2018,gdi_2019,gdi_2020,gdi_2021
 # ,hdi_f_1990,hdi_f_1991,hdi_f_1992,hdi_f_1993,hdi_f_1994,hdi_f_1995,hdi_f_1996,hdi_f_1997,hdi_f_1998,hdi_f_1999,hdi_f_2000,hdi_f_2001,hdi_f_2002,hdi_f_2003,hdi_f_2004,hdi_f_2005,hdi_f_2006,hdi_f_2007,hdi_f_2008,hdi_f_2009,hdi_f_2010,hdi_f_2011,hdi_f_2012,hdi_f_2013,hdi_f_2014,hdi_f_2015,hdi_f_2016,hdi_f_2017,hdi_f_2018,hdi_f_2019,hdi_f_2020,hdi_f_2021
 # ,le_f_1990,le_f_1991,le_f_1992,le_f_1993,le_f_1994,le_f_1995,le_f_1996,le_f_1997,le_f_1998,le_f_1999,le_f_2000,le_f_2001,le_f_2002,le_f_2003,le_f_2004,le_f_2005,le_f_2006,le_f_2007,le_f_2008,le_f_2009,le_f_2010,le_f_2011,le_f_2012,le_f_2013,le_f_2014,le_f_2015,le_f_2016,le_f_2017,le_f_2018,le_f_2019,le_f_2020,le_f_2021
 # ,eys_f_1990,eys_f_1991,eys_f_1992,eys_f_1993,eys_f_1994,eys_f_1995,eys_f_1996,eys_f_1997,eys_f_1998,eys_f_1999,eys_f_2000,eys_f_2001,eys_f_2002,eys_f_2003,eys_f_2004,eys_f_2005,eys_f_2006,eys_f_2007,eys_f_2008,eys_f_2009,eys_f_2010,eys_f_2011,eys_f_2012,eys_f_2013,eys_f_2014,eys_f_2015,eys_f_2016,eys_f_2017,eys_f_2018,eys_f_2019,eys_f_2020,eys_f_2021
 # ,mys_f_1990,mys_f_1991,mys_f_1992,mys_f_1993,mys_f_1994,mys_f_1995,mys_f_1996,mys_f_1997,mys_f_1998,mys_f_1999,mys_f_2000,mys_f_2001,mys_f_2002,mys_f_2003,mys_f_2004,mys_f_2005,mys_f_2006,mys_f_2007,mys_f_2008,mys_f_2009,mys_f_2010,mys_f_2011,mys_f_2012,mys_f_2013,mys_f_2014,mys_f_2015,mys_f_2016,mys_f_2017,mys_f_2018,mys_f_2019,mys_f_2020,mys_f_2021
 # ,gni_pc_f_1990,gni_pc_f_1991,gni_pc_f_1992,gni_pc_f_1993,gni_pc_f_1994,gni_pc_f_1995,gni_pc_f_1996,gni_pc_f_1997,gni_pc_f_1998,gni_pc_f_1999,gni_pc_f_2000,gni_pc_f_2001,gni_pc_f_2002,gni_pc_f_2003,gni_pc_f_2004,gni_pc_f_2005,gni_pc_f_2006,gni_pc_f_2007,gni_pc_f_2008,gni_pc_f_2009,gni_pc_f_2010,gni_pc_f_2011,gni_pc_f_2012,gni_pc_f_2013,gni_pc_f_2014,gni_pc_f_2015,gni_pc_f_2016,gni_pc_f_2017,gni_pc_f_2018,gni_pc_f_2019,gni_pc_f_2020,gni_pc_f_2021
 # ,hdi_m_1990,hdi_m_1991,hdi_m_1992,hdi_m_1993,hdi_m_1994,hdi_m_1995,hdi_m_1996,hdi_m_1997,hdi_m_1998,hdi_m_1999,hdi_m_2000,hdi_m_2001,hdi_m_2002,hdi_m_2003,hdi_m_2004,hdi_m_2005,hdi_m_2006,hdi_m_2007,hdi_m_2008,hdi_m_2009,hdi_m_2010,hdi_m_2011,hdi_m_2012,hdi_m_2013,hdi_m_2014,hdi_m_2015,hdi_m_2016,hdi_m_2017,hdi_m_2018,hdi_m_2019,hdi_m_2020,hdi_m_2021
 # ,le_m_1990,le_m_1991,le_m_1992,le_m_1993,le_m_1994,le_m_1995,le_m_1996,le_m_1997,le_m_1998,le_m_1999,le_m_2000,le_m_2001,le_m_2002,le_m_2003,le_m_2004,le_m_2005,le_m_2006,le_m_2007,le_m_2008,le_m_2009,le_m_2010,le_m_2011,le_m_2012,le_m_2013,le_m_2014,le_m_2015,le_m_2016,le_m_2017,le_m_2018,le_m_2019,le_m_2020,le_m_2021
 # ,eys_m_1990,eys_m_1991,eys_m_1992,eys_m_1993,eys_m_1994,eys_m_1995,eys_m_1996,eys_m_1997,eys_m_1998,eys_m_1999,eys_m_2000,eys_m_2001,eys_m_2002,eys_m_2003,eys_m_2004,eys_m_2005,eys_m_2006,eys_m_2007,eys_m_2008,eys_m_2009,eys_m_2010,eys_m_2011,eys_m_2012,eys_m_2013,eys_m_2014,eys_m_2015,eys_m_2016,eys_m_2017,eys_m_2018,eys_m_2019,eys_m_2020,eys_m_2021
 # ,mys_m_1990,mys_m_1991,mys_m_1992,mys_m_1993,mys_m_1994,mys_m_1995,mys_m_1996,mys_m_1997,mys_m_1998,mys_m_1999,mys_m_2000,mys_m_2001,mys_m_2002,mys_m_2003,mys_m_2004,mys_m_2005,mys_m_2006,mys_m_2007,mys_m_2008,mys_m_2009,mys_m_2010,mys_m_2011,mys_m_2012,mys_m_2013,mys_m_2014,mys_m_2015,mys_m_2016,mys_m_2017,mys_m_2018,mys_m_2019,mys_m_2020,mys_m_2021
 # ,gni_pc_m_1990,gni_pc_m_1991,gni_pc_m_1992,gni_pc_m_1993,gni_pc_m_1994,gni_pc_m_1995,gni_pc_m_1996,gni_pc_m_1997,gni_pc_m_1998,gni_pc_m_1999,gni_pc_m_2000,gni_pc_m_2001,gni_pc_m_2002,gni_pc_m_2003,gni_pc_m_2004,gni_pc_m_2005,gni_pc_m_2006,gni_pc_m_2007,gni_pc_m_2008,gni_pc_m_2009,gni_pc_m_2010,gni_pc_m_2011,gni_pc_m_2012,gni_pc_m_2013,gni_pc_m_2014,gni_pc_m_2015,gni_pc_m_2016,gni_pc_m_2017,gni_pc_m_2018,gni_pc_m_2019,gni_pc_m_2020,gni_pc_m_2021
 # ,ihdi_2010,ihdi_2011,ihdi_2012,ihdi_2013,ihdi_2014,ihdi_2015,ihdi_2016,ihdi_2017,ihdi_2018,ihdi_2019,ihdi_2020,ihdi_2021
 # ,coef_ineq_2010,coef_ineq_2011,coef_ineq_2012,coef_ineq_2013,coef_ineq_2014,coef_ineq_2015,coef_ineq_2016,coef_ineq_2017,coef_ineq_2018,coef_ineq_2019,coef_ineq_2020,coef_ineq_2021
 # ,loss_2010,loss_2011,loss_2012,loss_2013,loss_2014,loss_2015,loss_2016,loss_2017,loss_2018,loss_2019,loss_2020,loss_2021
 # ,ineq_le_2010,ineq_le_2011,ineq_le_2012,ineq_le_2013,ineq_le_2014,ineq_le_2015,ineq_le_2016,ineq_le_2017,ineq_le_2018,ineq_le_2019,ineq_le_2020,ineq_le_2021
 # ,ineq_edu_2010,ineq_edu_2011,ineq_edu_2012,ineq_edu_2013,ineq_edu_2014,ineq_edu_2015,ineq_edu_2016,ineq_edu_2017,ineq_edu_2018,ineq_edu_2019,ineq_edu_2020,ineq_edu_2021
 # ,ineq_inc_2010,ineq_inc_2011,ineq_inc_2012,ineq_inc_2013,ineq_inc_2014,ineq_inc_2015,ineq_inc_2016,ineq_inc_2017,ineq_inc_2018,ineq_inc_2019,ineq_inc_2020,ineq_inc_2021
 # ,gii_rank_2021,gii_1990,gii_1991,gii_1992,gii_1993,gii_1994,gii_1995,gii_1996,gii_1997,gii_1998,gii_1999,gii_2000,gii_2001,gii_2002,gii_2003,gii_2004,gii_2005,gii_2006,gii_2007,gii_2008,gii_2009,gii_2010,gii_2011,gii_2012,gii_2013,gii_2014,gii_2015,gii_2016,gii_2017,gii_2018,gii_2019,gii_2020,gii_2021
 # ,mmr_1990,mmr_1991,mmr_1992,mmr_1993,mmr_1994,mmr_1995,mmr_1996,mmr_1997,mmr_1998,mmr_1999,mmr_2000,mmr_2001,mmr_2002,mmr_2003,mmr_2004,mmr_2005,mmr_2006,mmr_2007,mmr_2008,mmr_2009,mmr_2010,mmr_2011,mmr_2012,mmr_2013,mmr_2014,mmr_2015,mmr_2016,mmr_2017,mmr_2018,mmr_2019,mmr_2020,mmr_2021
 # ,abr_1990,abr_1991,abr_1992,abr_1993,abr_1994,abr_1995,abr_1996,abr_1997,abr_1998,abr_1999,abr_2000,abr_2001,abr_2002,abr_2003,abr_2004,abr_2005,abr_2006,abr_2007,abr_2008,abr_2009,abr_2010,abr_2011,abr_2012,abr_2013,abr_2014,abr_2015,abr_2016,abr_2017,abr_2018,abr_2019,abr_2020,abr_2021
 # ,se_f_1990,se_f_1991,se_f_1992,se_f_1993,se_f_1994,se_f_1995,se_f_1996,se_f_1997,se_f_1998,se_f_1999,se_f_2000,se_f_2001,se_f_2002,se_f_2003,se_f_2004,se_f_2005,se_f_2006,se_f_2007,se_f_2008,se_f_2009,se_f_2010,se_f_2011,se_f_2012,se_f_2013,se_f_2014,se_f_2015,se_f_2016,se_f_2017,se_f_2018,se_f_2019,se_f_2020,se_f_2021
 # ,se_m_1990,se_m_1991,se_m_1992,se_m_1993,se_m_1994,se_m_1995,se_m_1996,se_m_1997,se_m_1998,se_m_1999,se_m_2000,se_m_2001,se_m_2002,se_m_2003,se_m_2004,se_m_2005,se_m_2006,se_m_2007,se_m_2008,se_m_2009,se_m_2010,se_m_2011,se_m_2012,se_m_2013,se_m_2014,se_m_2015,se_m_2016,se_m_2017,se_m_2018,se_m_2019,se_m_2020,se_m_2021
 # ,pr_f_1990,pr_f_1991,pr_f_1992,pr_f_1993,pr_f_1994,pr_f_1995,pr_f_1996,pr_f_1997,pr_f_1998,pr_f_1999,pr_f_2000,pr_f_2001,pr_f_2002,pr_f_2003,pr_f_2004,pr_f_2005,pr_f_2006,pr_f_2007,pr_f_2008,pr_f_2009,pr_f_2010,pr_f_2011,pr_f_2012,pr_f_2013,pr_f_2014,pr_f_2015,pr_f_2016,pr_f_2017,pr_f_2018,pr_f_2019,pr_f_2020,pr_f_2021
 # ,pr_m_1990,pr_m_1991,pr_m_1992,pr_m_1993,pr_m_1994,pr_m_1995,pr_m_1996,pr_m_1997,pr_m_1998,pr_m_1999,pr_m_2000,pr_m_2001,pr_m_2002,pr_m_2003,pr_m_2004,pr_m_2005,pr_m_2006,pr_m_2007,pr_m_2008,pr_m_2009,pr_m_2010,pr_m_2011,pr_m_2012,pr_m_2013,pr_m_2014,pr_m_2015,pr_m_2016,pr_m_2017,pr_m_2018,pr_m_2019,pr_m_2020,pr_m_2021
 # ,lfpr_f_1990,lfpr_f_1991,lfpr_f_1992,lfpr_f_1993,lfpr_f_1994,lfpr_f_1995,lfpr_f_1996,lfpr_f_1997,lfpr_f_1998,lfpr_f_1999,lfpr_f_2000,lfpr_f_2001,lfpr_f_2002,lfpr_f_2003,lfpr_f_2004,lfpr_f_2005,lfpr_f_2006,lfpr_f_2007,lfpr_f_2008,lfpr_f_2009,lfpr_f_2010,lfpr_f_2011,lfpr_f_2012,lfpr_f_2013,lfpr_f_2014,lfpr_f_2015,lfpr_f_2016,lfpr_f_2017,lfpr_f_2018,lfpr_f_2019,lfpr_f_2020,lfpr_f_2021
 # ,lfpr_m_1990,lfpr_m_1991,lfpr_m_1992,lfpr_m_1993,lfpr_m_1994,lfpr_m_1995,lfpr_m_1996,lfpr_m_1997,lfpr_m_1998,lfpr_m_1999,lfpr_m_2000,lfpr_m_2001,lfpr_m_2002,lfpr_m_2003,lfpr_m_2004,lfpr_m_2005,lfpr_m_2006,lfpr_m_2007,lfpr_m_2008,lfpr_m_2009,lfpr_m_2010,lfpr_m_2011,lfpr_m_2012,lfpr_m_2013,lfpr_m_2014,lfpr_m_2015,lfpr_m_2016,lfpr_m_2017,lfpr_m_2018,lfpr_m_2019,lfpr_m_2020,lfpr_m_2021
 # ,rankdiff_hdi_phdi_2021
 # ,phdi_1990,phdi_1991,phdi_1992,phdi_1993,phdi_1994,phdi_1995,phdi_1996,phdi_1997,phdi_1998,phdi_1999,phdi_2000,phdi_2001,phdi_2002,phdi_2003,phdi_2004,phdi_2005,phdi_2006,phdi_2007,phdi_2008,phdi_2009,phdi_2010,phdi_2011,phdi_2012,phdi_2013,phdi_2014,phdi_2015,phdi_2016,phdi_2017,phdi_2018,phdi_2019,phdi_2020,phdi_2021
 # ,diff_hdi_phdi_1990,diff_hdi_phdi_1991,diff_hdi_phdi_1992,diff_hdi_phdi_1993,diff_hdi_phdi_1994,diff_hdi_phdi_1995,diff_hdi_phdi_1996,diff_hdi_phdi_1997,diff_hdi_phdi_1998,diff_hdi_phdi_1999,diff_hdi_phdi_2000,diff_hdi_phdi_2001,diff_hdi_phdi_2002,diff_hdi_phdi_2003,diff_hdi_phdi_2004,diff_hdi_phdi_2005,diff_hdi_phdi_2006,diff_hdi_phdi_2007,diff_hdi_phdi_2008,diff_hdi_phdi_2009,diff_hdi_phdi_2010,diff_hdi_phdi_2011,diff_hdi_phdi_2012,diff_hdi_phdi_2013,diff_hdi_phdi_2014,diff_hdi_phdi_2015,diff_hdi_phdi_2016,diff_hdi_phdi_2017,diff_hdi_phdi_2018,diff_hdi_phdi_2019,diff_hdi_phdi_2020,diff_hdi_phdi_2021
 # ,co2_prod_1990,co2_prod_1991,co2_prod_1992,co2_prod_1993,co2_prod_1994,co2_prod_1995,co2_prod_1996,co2_prod_1997,co2_prod_1998,co2_prod_1999,co2_prod_2000,co2_prod_2001,co2_prod_2002,co2_prod_2003,co2_prod_2004,co2_prod_2005,co2_prod_2006,co2_prod_2007,co2_prod_2008,co2_prod_2009,co2_prod_2010,co2_prod_2011,co2_prod_2012,co2_prod_2013,co2_prod_2014,co2_prod_2015,co2_prod_2016,co2_prod_2017,co2_prod_2018,co2_prod_2019,co2_prod_2020,co2_prod_2021
 # ,mf_1990,mf_1991,mf_1992,mf_1993,mf_1994,mf_1995,mf_1996,mf_1997,mf_1998,mf_1999,mf_2000,mf_2001,mf_2002,mf_2003,mf_2004,mf_2005,mf_2006,mf_2007,mf_2008,mf_2009,mf_2010,mf_2011,mf_2012,mf_2013,mf_2014,mf_2015,mf_2016,mf_2017,mf_2018,mf_2019,mf_2020,mf_2021
#
#
#
# excluir oque nao tem rank hdi_rank_2021
df_idh_undp_drop_hdi_rank_2021 = df_idh_undp.dropna(subset=['hdi_rank_2021']) # de [206 rows x 1008 columns] para [191 rows x 1008 columns]
# print(df_idh_undp_drop_hdi_rank_2021)
df_idh_undp_rank_hdi_2020 = df_idh_undp_drop_hdi_rank_2021
# rankear hdi_2020, e colocar em ordem
df_idh_undp_rank_hdi_2020['Ranking HDI 2020'] = df_idh_undp_rank_hdi_2020['hdi_2020'].rank(ascending=False, method='min')
df_idh_undp_rank_hdi_2020 = df_idh_undp_rank_hdi_2020.sort_values(by='Ranking HDI 2020')
# print(df_idh_undp_rank_hdi_2020)
# selecionar as colunas de interesse ************************************************** Criar funcao.
select_idh_column = ['iso3', 'country', 'hdi_2020', 'Ranking HDI 2020']
df_idh_undp_selected = df_idh_undp_rank_hdi_2020[select_idh_column]
# print(df_idh_undp_selected)



# TRATAMENTO DO DATAFRAME ECONOMIC FREEDOM FRASER ##########################################################################################################
# print(df_ef_fraser) # [165 rows x 72 columns]

df_ef_fraser['Ranking Economic Freedom'] = df_ef_fraser['Economic Freedom Summary Index'].rank(ascending=False, method='min')
df_ef_fraser = df_ef_fraser.sort_values(by='Ranking Economic Freedom')

select_fraser_column = ['ISO_Code', 'Countries', 'Economic Freedom Summary Index', 'Ranking Economic Freedom']
df_ef_fraser_selected = df_ef_fraser[select_fraser_column]

# print(df_ef_fraser_selected) # [165 rows x 4 columns]


# TRATAMENTO DO DATAFRAME ECONOMIC FREEDOM HERITAGE FOUNDATION ##############################################################################################
# print(df_ef_heritage) # [5339 rows x 18 columns]

# selecionar apenas as linhas que tenham Index Year == 2020
df_ef_heritage_2020 = df_ef_heritage[df_ef_heritage['Index Year'] == 2020]
# print(df_ef_heritage_2020) # [186 rows x 18 columns]

# criar iso3 a partir do iso2 do df_ef_heritage_2020
df_ef_heritage_2020['iso3'] = df_ef_heritage_2020['ISO Code'].apply(iso2_to_iso3)
# print(df_ef_heritage_2020) # [186 rows x 19 columns]

# drop dos Nan em Overall Score
df_ef_heritage_2020 = df_ef_heritage_2020.dropna(subset=['Overall Score'])
# print(df_ef_heritage_2020) # [180 rows x 19 columns]

# criar ranking do Overall Score em ordem decrescente e colocar em ordem
df_ef_heritage_2020['Ranking Economic Freedom'] = df_ef_heritage_2020['Overall Score'].rank(ascending=False, method='min')
df_ef_heritage_2020 = df_ef_heritage_2020.sort_values(by='Ranking Economic Freedom')
# pd.set_option('display.max_rows', None)
# print(df_ef_heritage_2020) # [180 rows x 20 columns]

# selecionar as colunas de interesse ************************************************** Criar funcao.
select_heritage_column = ['iso3', 'Name', 'Overall Score', 'Ranking Economic Freedom']
df_ef_heritage_selected = df_ef_heritage_2020[select_heritage_column]
# print(df_ef_heritage_selected)


# Realizar o merge dos data frames
merged_df_fraser = df_idh_undp_selected.merge(df_ef_fraser_selected, left_on='iso3', right_on='ISO_Code', how='inner')
merged_df_heritage = df_idh_undp_selected.merge(df_ef_heritage_selected, left_on='iso3', right_on='iso3', how='inner')
merged_df_fraser_heritage = df_ef_fraser_selected.merge(df_ef_heritage_selected, left_on='ISO_Code', right_on='iso3', how='inner')

print(merged_df_fraser)
# print(merged_df_heritage)
# print(merged_df_fraser_heritage)

######################################### COEFICIENTE DE CORRELACAO DE PEARSON FRASER + IDH ####################################################################
correlation_rankings_fraser = merged_df_fraser[['Ranking HDI 2020', 'Ranking Economic Freedom']].corr(method='pearson')
correlation_hdi_ef_fraser = merged_df_fraser[['hdi_2020', 'Economic Freedom Summary Index']].corr(method='pearson')
print("Fraser Dataframe vs HDI 2020:")
print("Correlation between Rankings:")
print(correlation_rankings_fraser)

print("\nCorrelation between HDI 2020 and Economic Freedom:")
print(correlation_hdi_ef_fraser)

########################################## COEFICIENTE DE CORRELACAO DE PEARSON HERITAGE + IDH ####################################################################
correlation_rankings_heritage = merged_df_heritage[['Ranking HDI 2020', 'Ranking Economic Freedom']].corr(method='pearson')
correlation_hdi_ef_heritage = merged_df_heritage[['hdi_2020', 'Overall Score']].corr(method='pearson')

print("Heritage Dataframe vs HDI 2020:")
print("Correlation between Rankings:")
print(correlation_rankings_heritage)

print("\nCorrelation between HDI 2020 and Economic Freedom:")
print(correlation_hdi_ef_heritage)

############################################# COEFICIENTE DE CORRELACAO DE PEARSON FRASER + HERITAGE ############################################################
correlation_rankings_fraser_heritage = merged_df_fraser_heritage[['Ranking Economic Freedom_x', 'Ranking Economic Freedom_y']].corr(method='pearson')
correlation_index_fraser_heritage = merged_df_fraser_heritage[['Economic Freedom Summary Index', 'Overall Score']].corr(method='pearson')
print("Fraser Dataframe vs Heritage Dataframe:")
print("Correlation between Rankings:")
print(correlation_rankings_fraser_heritage)

print("\nCorrelation between Economic Freedom Summary Index and Overall Score:")
print(correlation_index_fraser_heritage)




######################################################### ANALIZAR PERDA DE DADOS ####################################################################
# ##########################################################################################################################
# # # oque nao esta presente em um data frame
# print("##############################################")
# print("Dados que não estão em IDH mas tem em EF FRASER")
# iso3_not_in_idh = df_ef_fraser_selected[~df_ef_fraser_selected['ISO_Code'].isin(df_idh_undp_selected['iso3'])]

# # Exiba os valores de iso3 que não estão em df_idh_undp_selected
# print(iso3_not_in_idh)
# print("##############################################")
# print("##############################################")
# print("Dados que não estão em EF FRASER mas tem em IDH")
# # Encontre os valores de iso3 em df_idh_undp_selected que não estão em df_ef_fraser_selected
# iso3_not_in_fraser = df_idh_undp_selected[~df_idh_undp_selected['iso3'].isin(df_ef_fraser_selected['ISO_Code'])]

# # Exiba os valores de iso3 que não estão em df_ef_fraser_selected
# print(iso3_not_in_fraser)
# print("##############################################")


# ###########################################################################################################################
# print("##############################################")
# print("Dados que não estão em IDH mas tem em EF HERITAGE")
# iso3_not_in_idh = df_ef_heritage_selected[~df_ef_heritage_selected['iso3'].isin(df_idh_undp_selected['iso3'])]

# # Exiba os valores de iso3 que não estão em df_idh_undp_selected
# print(iso3_not_in_idh)
# print("##############################################")

# print("##############################################")
# print("Dados que não estão em EF HERITAGE mas tem em IDH")
# # Encontre os valores de iso3 em df_idh_undp_selected que não estão em df_ef_heritage_selected
# iso3_not_in_heritage = df_idh_undp_selected[~df_idh_undp_selected['iso3'].isin(df_ef_heritage_selected['iso3'])]

# # Exiba os valores de iso3 que não estão em df_ef_heritage_selected
# print(iso3_not_in_heritage)
# print("##############################################")
