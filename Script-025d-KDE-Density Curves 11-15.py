#!/usr/bin/env python
# coding: utf-8

# In[24]:


# library and dataset
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
sns.set_style('darkgrid')

ax=sns.kdeplot(df['profile11'], shade=True, color="r")
ax=sns.kdeplot(df['profile12'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile13'], shade=True, color="b")
ax=sns.kdeplot(df['profile14'], shade=True, color="#e95295")
ax=sns.kdeplot(df['profile15'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
plt.title("Kernel Density Esimation: \nprobability of depth ranges by profiles 11-15")
ax.annotate('C', xy=(0.03, .90), xycoords="axes fraction", fontsize=18,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))

plt.show()


# In[ ]:




