#!/usr/bin/env python
# coding: utf-8

# ## Football Data
# 

# In[30]:


import numpy as np
import pandas as pd


# In[31]:


football_df=pd.read_excel(r'C:\Users\Shashi Shekhar\Desktop\python\upwork tasks\date 09.10.2024\Football Data Test Task.xlsx', sheet_name = 0)
football_df


# In[32]:


football_df.columns


# In[33]:


football_df.head()


# In[36]:


# for home team and away team
football_df['HW'] = football_df['FTR'].apply(lambda x: 1 if x == 'H' else 0)
football_df['AW'] = football_df['FTR'].apply(lambda x: 1 if x == 'A' else 0)
football_df['HL'] = football_df['FTR'].apply(lambda x: 1 if x == 'A' else 0)
football_df['AL'] = football_df['FTR'].apply(lambda x: 1 if x == 'H' else 0)
football_df['HD'] = football_df['FTR'].apply(lambda x: 1 if x == 'D' else 0)
football_df['AD'] = football_df['FTR'].apply(lambda x: 1 if x == 'D' else 0)
football_df


# In[37]:


# Grouping by home team and away team Calculating the last 5, 15, 38 matches stats
football_df['FTHG_L5'] = football_df.groupby('HomeTeam')['FTHG'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['FTHG_L15'] = football_df.groupby('HomeTeam')['FTHG'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['FTHG_L38'] = football_df.groupby('HomeTeam')['FTHG'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['FTAG_L5'] = football_df.groupby('AwayTeam')['FTAG'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['FTAG_L15'] = football_df.groupby('AwayTeam')['FTAG'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['FTAG_L38'] = football_df.groupby('AwayTeam')['FTAG'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HS_L5'] = football_df.groupby('HomeTeam')['HS'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HS_L15'] = football_df.groupby('HomeTeam')['HS'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HS_L38'] = football_df.groupby('HomeTeam')['HS'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AS_L5'] = football_df.groupby('AwayTeam')['AS'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AS_L15'] = football_df.groupby('AwayTeam')['AS'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AS_L38'] = football_df.groupby('AwayTeam')['AS'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HST_L5'] = football_df.groupby('HomeTeam')['HST'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HST_L15'] = football_df.groupby('HomeTeam')['HST'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HST_L38'] = football_df.groupby('HomeTeam')['HST'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AST_L5'] = football_df.groupby('AwayTeam')['AST'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AST_L15'] = football_df.groupby('AwayTeam')['AST'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AST_L38'] = football_df.groupby('AwayTeam')['AST'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HF_L5'] = football_df.groupby('HomeTeam')['HF'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HF_L15'] = football_df.groupby('HomeTeam')['HF'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HF_L38'] = football_df.groupby('HomeTeam')['HF'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AF_L5'] = football_df.groupby('AwayTeam')['AF'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AF_L15'] = football_df.groupby('AwayTeam')['AF'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AF_L38'] = football_df.groupby('AwayTeam')['AF'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HC_L5'] = football_df.groupby('HomeTeam')['HC'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HC_L15'] = football_df.groupby('HomeTeam')['HC'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HC_L38'] = football_df.groupby('HomeTeam')['HC'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AC_L5'] = football_df.groupby('AwayTeam')['AC'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AC_L15'] = football_df.groupby('AwayTeam')['AC'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AC_L38'] = football_df.groupby('AwayTeam')['AC'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HY_L5'] = football_df.groupby('HomeTeam')['HY'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HY_L15'] = football_df.groupby('HomeTeam')['HY'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HY_L38'] = football_df.groupby('HomeTeam')['HY'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AY_L5'] = football_df.groupby('AwayTeam')['AY'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AY_L15'] = football_df.groupby('AwayTeam')['AY'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AY_L38'] = football_df.groupby('AwayTeam')['AY'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HR_L5'] = football_df.groupby('HomeTeam')['HR'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HR_L15'] = football_df.groupby('HomeTeam')['HR'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HR_L38'] = football_df.groupby('HomeTeam')['HR'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AR_L5'] = football_df.groupby('AwayTeam')['AR'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AR_L15'] = football_df.groupby('AwayTeam')['AR'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AR_L38'] = football_df.groupby('AwayTeam')['AR'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HW_L5'] = football_df.groupby('HomeTeam')['HW'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HW_L15'] = football_df.groupby('HomeTeam')['HW'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HW_L38'] = football_df.groupby('HomeTeam')['HW'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HL_L5'] = football_df.groupby('HomeTeam')['HL'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HL_L15'] = football_df.groupby('HomeTeam')['HL'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HL_L38'] = football_df.groupby('HomeTeam')['HL'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['HD_L5'] = football_df.groupby('HomeTeam')['HD'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['HD_L15'] = football_df.groupby('HomeTeam')['HD'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['HD_L38'] = football_df.groupby('HomeTeam')['HD'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AW_L5'] = football_df.groupby('AwayTeam')['AW'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AW_L15'] = football_df.groupby('AwayTeam')['AW'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AW_L38'] = football_df.groupby('AwayTeam')['AW'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AL_L5'] = football_df.groupby('AwayTeam')['AL'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AL_L15'] = football_df.groupby('AwayTeam')['AL'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AL_L38'] = football_df.groupby('AwayTeam')['AL'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df['AD_L5'] = football_df.groupby('AwayTeam')['AD'].rolling(window=5, min_periods=1).sum().reset_index(drop=True)
football_df['AD_L15'] = football_df.groupby('AwayTeam')['AD'].rolling(window=15, min_periods=1).sum().reset_index(drop=True)
football_df['AD_L38'] = football_df.groupby('AwayTeam')['AD'].rolling(window=38, min_periods=1).sum().reset_index(drop=True)
football_df


# In[38]:


# Convert the date column to datetime format
football_df['Date'] = pd.to_datetime(football_df['Date'], errors='coerce')

# Define the date range
start_date = pd.to_datetime('2006-08-19 00:00:00')
end_date = pd.to_datetime('2024-09-01 00:00:00')

# Filter the dataset within the date range
football_df = football_df[(football_df['Date'] >= start_date) & (football_df['Date'] <= end_date)]
football_df


# In[40]:


football_df = football_df.drop(columns=['HW', 'AW', 'HD', 'AD', 'HL', 'AL'])
football_df
                                        


# In[41]:


# Save to Excel
football_df.to_excel(r'C:\Users\Shashi Shekhar\Desktop\python\upwork tasks\date 09.10.2024\manipulated_football_data.xlsx', index=False)


# In[ ]:




