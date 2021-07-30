import math
from datetime import datetime
import pandas as pd

#current_month = datetime.now().strftime('%h')
current_month = 'Okt'

df = pd.read_excel('Application_Form.xlsx')
df = df.loc[:, ['Full name', 'Grade', 'Parent\'s name', 'Parent\'s phone number']]
m_agus = pd.read_excel('Eudaimonia.xlsx', skiprows=1, sheet_name='Agus ('+str(current_month)+')')
m_anton = pd.read_excel('Eudaimonia.xlsx', skiprows=1, sheet_name='Anton ('+str(current_month)+')')
m_yohanes = pd.read_excel('Eudaimonia.xlsx', skiprows=1, sheet_name='Yohanes ('+str(current_month)+')')

#making empty columns
n = len(df)
tem = [float('nan') for i in range(n)]
n = len(df.columns)
for i in range(60,0,-1):
    df.insert(n, str(i), tem)
n = len(df.columns)
df.insert(n, 'Total_Pertemuan_yohanes', tem)
df.insert(n, 'Total_Pertemuan_Anton', tem)
df.insert(n, 'Total_Pertemuan_Agus', tem)

"""
*note: 
1-20 = agus
21-40 = anton
41-60 = yohanes        
"""

# #bagian agus
# len_df = len(df)
# len_m = len(m_agus)
# for i in range(len_m):
#     for j in range(len_df):
#         if m_agus.Nama[i] == df['Full name'][j]:
#             for k in range(1,int(m_agus.Total[i])+1):
#                 df[str(k)][j] = m_agus[k][i]
#             df.Total_Pertemuan[j] = m_agus.Total[i]

#---------------------------------------------logic starts here---------------------------------------------------------
#bagian agus
guru = 'Agus'
m = m_agus
len_df = len(df)
len_m = len(m)
for i in range(len_m):
    for j in range(len_df):
        if m.Nama[i] == df['Full name'][j]:
            for k in range(1,int(m.Total[i])+1):
                df[str(k)][j] = m[k][i]
            df['Total_Pertemuan_'+guru][j] = m.Total[i]

#bagian anton
guru = 'Anton'
m = m_anton
len_df = len(df)
len_m = len(m)
for i in range(len_m):
    for j in range(len_df):
        if m.Nama[i] == df['Full name'][j]:
            for k in range(21,int(21+m.Total[i])):
                df[str(k)][j] = m[k][i]
            df['Total_Pertemuan_'+guru][j] = m.Total[i]

#bagian yohanes
guru = 'yohanes'
m = m_yohanes
len_df = len(df)
len_m = len(m)
for i in range(len_m):
    for j in range(len_df):
        if m.Nama[i] == df['Full name'][j]:
            for k in range(41,int(41+m.Total[i])):
                df[str(k)][j] = m[k][i]
            df['Total_Pertemuan_'+guru][j] = m.Total[i]

df.to_csv('tuman.csv')
