import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats 
import seaborn as sns
dfgk=pd.read_csv("path/to/your/data/gk.df.csv")
dfpg=pd.read_csv("path/to/your/data/peng.df.csv")
dfump=pd.read_csv("path/to/your/data/ump.df.csv")
dfupah=pd.read_csv("path/to/your/data/upah.df.csv")
#descriptive statistics for each dataframe 
dfgk.describe()
dfpg.describe() 
dfump.describe()
dfupah.describe()
#checking for missing values in each dataframe
print(dfgk.notnull().sum())
print(dfpg.notnull().sum())
print(dfump.notnull().sum())
print(dfupah.notnull().sum())
#aggregate the data by provinsi and tahun, calculating the mean for garis kemiskinan and pengeluaran per kapita
aggregated_dfgk = dfgk.groupby(['provinsi','tahun'], as_index=False)['gk'].mean()
aggregated_dfpg = dfpg.groupby(['provinsi','tahun'], as_index=False)['peng'].mean()
aggregated_dfgk = aggregated_dfgk.rename(columns={'gk': 'garis kemiskinan'})
aggregated_dfpg = aggregated_dfpg.rename(columns={'peng': 'pengeluaran per kapita'})
dfump = dfump.rename(columns={'ump': 'upah minimum provinsi'})
dfupah = dfupah.rename(columns={'upah': 'upah per kapita'})
#merge the aggregated dataframes on provinsi and tahun
pgUgk=pd.merge(aggregated_dfpg, aggregated_dfgk, on=['provinsi', 'tahun'], how='inner')
pgUgkUump=pd.merge(pgUgk, dfump, on=['provinsi', 'tahun'], how='inner')
all_data=pd.merge(pgUgkUump, dfupah, on=['provinsi', 'tahun'], how='inner')
#making a correlation matrix and visualizing it using a heatmap
numerical_columns= ['pengeluaran per kapita', 'garis kemiskinan', 'upah minimum provinsi', 'upah per kapita']
correlation_matrix = all_data[numerical_columns].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Korelasi antara Variabel', fontsize=14)
plt.tight_layout()
plt.show()
#scatter plot for pengeluaran per kapita vs garis kemiskinan
Scatterplot= all_data[numerical_columns]
plt.figure(figsize=(8, 6))
sns.scatterplot(data=Scatterplot, x='pengeluaran per kapita', y='garis kemiskinan')
plt.title('Scatter Plot: Pengeluaran Per Kapita vs Garis Kemiskinan', fontsize=14)
plt.xlabel('Pengeluaran Per Kapita', fontsize=12)
plt.ylabel('Garis Kemiskinan', fontsize=12) 
plt.tight_layout()
plt.show()
#--conclusion-- 
# 1. the highest correlation is between pengeluaran per kapita and upah per kapita, with a correlation coefficient of 0.80, indicating a strong positive relationship. 
#    This suggests that as pengeluaran per kapita increas, upah per kapita also tends to increase. 

# 2. The lowest correlation is between garis kemiskinan and upah minimum provinsi, with a correlation coefficient of 0.63, even though it is still a positive correlation, 
#    this is weaker compared to the other variables. This indicates that while there is some relationship between garis kemiskinan and upah minimum provinsi,
#    it is not as strong as the relationship between pengeluaran per kapita and upah per kapita.

# 3. Important to note that correlation does not imply causation. While there are relationships between these variables, 
#    it does not mean that one variable causes changes in another. Further analysis would be needed to explore potential causal relationships.