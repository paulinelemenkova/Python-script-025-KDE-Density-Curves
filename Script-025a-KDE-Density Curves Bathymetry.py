#!/usr/bin/env python
# coding: utf-8

# In[20]:


# library and dataset
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
sns.set_style('darkgrid')
#df = dfM.melt(id_vars=['profile'], 
 #             value_vars=['plate_phill', 'plate_pacif', 'plate_maria', 'plate_carol'],
  #            var_name='plates', value_name='Mean')
 
# plot of 4 variables
ax=sns.kdeplot(df['Min'], shade=True, color="r")
ax=sns.kdeplot(df['Mean'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['Max'], shade=True, color="b")
ax=sns.kdeplot(df['1stQ'], shade=True, color="#65318e")
ax=sns.kdeplot(df['3rdQ'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
plt.title("Kernel Density Esimation: \nprobability of the statistical depth ranges, profiles 1-25")
ax.annotate('F', xy=(0.03, .90), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
plt.show()


# In[ ]:




