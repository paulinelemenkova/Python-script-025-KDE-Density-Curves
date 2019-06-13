#!/usr/bin/env python
# coding: utf-8

# In[5]:


import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os
#
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
dfM = pd.read_csv("Tab-Morph.csv")
sns.set_style('darkgrid')
sns.set_context("paper")
#
fig = plt.figure(figsize=(10.0, 6.0), dpi=300)
fig.suptitle('Kernel Density Esimation: probability of depth ranges',
            fontsize=10, fontweight='bold', x=0.5, y=0.99)
#
# subplot 1
ax = fig.add_subplot(231)
ax=sns.kdeplot(df['profile1'], shade=True, color="r")
ax=sns.kdeplot(df['profile2'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile3'], shade=True, color="b")
ax=sns.kdeplot(df['profile4'], shade=True, color="#e95295")
ax=sns.kdeplot(df['profile5'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("profiles 1-5", fontsize=9, fontfamily='serif')
ax.annotate('A', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 2
ax = fig.add_subplot(232)
ax=sns.kdeplot(df['profile6'], shade=True, color="r")
ax=sns.kdeplot(df['profile7'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile8'], shade=True, color="b")
ax=sns.kdeplot(df['profile9'], shade=True, color="#e95295")
ax=sns.kdeplot(df['profile10'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("profiles 6-10", fontsize=9, fontfamily='serif')
ax.annotate('B', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 3
ax = fig.add_subplot(233)
ax=sns.kdeplot(df['profile11'], shade=True, color="r")
ax=sns.kdeplot(df['profile12'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile13'], shade=True, color="b")
ax=sns.kdeplot(df['profile14'], shade=True, color="#e95295")
ax=sns.kdeplot(df['profile15'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("profiles 11-15", fontsize=9, fontfamily='serif')
ax.annotate('C', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 4
ax = fig.add_subplot(234)
ax=sns.kdeplot(df['profile16'], shade=True, color="r")
ax=sns.kdeplot(df['profile17'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile18'], shade=True, color="b")
ax=sns.kdeplot(df['profile19'], shade=True, color="#c3d825")
ax=sns.kdeplot(df['profile20'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("profiles 16-20", fontsize=9, fontfamily='serif')
ax.annotate('D', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 5
ax = fig.add_subplot(235)
ax=sns.kdeplot(df['profile21'], shade=True, color="r")
ax=sns.kdeplot(df['profile22'], shade=True, color="#ffd900")
ax=sns.kdeplot(df['profile23'], shade=True, color="b")
ax=sns.kdeplot(df['profile24'], shade=True, color="#c3d825")
ax=sns.kdeplot(df['profile25'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("profiles 21-25")
ax.annotate('E', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
# subplot 6
ax = fig.add_subplot(236)
ax=sns.kdeplot(dfM['Min'], shade=True, color="r")
ax=sns.kdeplot(dfM['Mean'], shade=True, color="#ffd900")
ax=sns.kdeplot(dfM['Max'], shade=True, color="b")
ax=sns.kdeplot(dfM['1stQ'], shade=True, color="#65318e")
ax=sns.kdeplot(dfM['3rdQ'], shade=True, color="#00a3af")
ax.set(xlabel='Depths, m', ylabel='KDE')
ax.legend(loc='upper right', fontsize=6)
ax.tick_params(axis='x', labelsize=7)
ax.tick_params(axis='y', labelsize=7)
plt.title("bathymetric depth ranges, profiles 1-25")
ax.annotate('F', xy=(0.03, .90), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
#
plt.tight_layout()
fig.savefig('plot_KDE.png', dpi=300)
plt.show()


# In[ ]:




