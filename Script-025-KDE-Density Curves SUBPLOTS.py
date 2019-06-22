#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import matplotlib.pylab as pylab
from matplotlib import pyplot as plt
import matplotlib.artist as martist
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
dfM = pd.read_csv("Tab-Morph.csv")
sns.set_style('darkgrid')
sns.set_context("paper")

params = {'figure.figsize': (10, 6),
    'figure.dpi': 300,
        'figure.titlesize': 14,
            'font.family': 'Palatino',
                'axes.labelsize': 10,
                    'legend.fontsize': 8,
                        'legend.loc': 'best',
                            'xtick.labelsize': 8,
                                'ytick.labelsize': 8,
                                    'axes.labelpad':2,
                                    }
pylab.rcParams.update(params)

fig, axes = plt.subplots(nrows = 2, ncols = 3)
fig.suptitle('Kernel Density Esimation: probability of the depth ranges, Mariana Trench',
             x=0.5, y=0.99)

def add_at(axes, t, loc=1):
    fp = dict(size=11)
    _at = AnchoredText(t, loc=loc, prop=fp)
    axes.add_artist(_at)
    return _at

for ax in axes.flat:
    ax.set(xlabel='Depths, m', ylabel='KDE')

# subplot 1
axes[0,0] = fig.add_subplot(231)
axes[0,0] = sns.kdeplot(df['profile1'], shade=True, color="r")
axes[0,0] = sns.kdeplot(df['profile2'], shade=True, color="#ffd900")
axes[0,0] = sns.kdeplot(df['profile3'], shade=True, color="b")
axes[0,0] = sns.kdeplot(df['profile4'], shade=True, color="#e95295")
axes[0,0] = sns.kdeplot(df['profile5'], shade=True, color="#00a3af")
plt.title("profiles 1-5", fontsize=9)
add_at(axes[0,0], "A", loc=2)


# subplot 2
axes[0,1] = fig.add_subplot(232)
axes[0,1] = sns.kdeplot(df['profile6'], shade=True, color="r")
axes[0,1] = sns.kdeplot(df['profile7'], shade=True, color="#ffd900")
axes[0,1] = sns.kdeplot(df['profile8'], shade=True, color="b")
axes[0,1] = sns.kdeplot(df['profile9'], shade=True, color="#e95295")
axes[0,1] = sns.kdeplot(df['profile10'], shade=True, color="#00a3af")
plt.title("profiles 6-10", fontsize=9)
add_at(axes[0,1], "B", loc=2)

# subplot 3
axes[0,2] = fig.add_subplot(233)
axes[0,2] = sns.kdeplot(df['profile11'], shade=True, color="r")
axes[0,2] = sns.kdeplot(df['profile12'], shade=True, color="#ffd900")
axes[0,2] = sns.kdeplot(df['profile13'], shade=True, color="b")
axes[0,2] = sns.kdeplot(df['profile14'], shade=True, color="#e95295")
axes[0,2] = sns.kdeplot(df['profile15'], shade=True, color="#00a3af")
plt.title("profiles 11-15", fontsize=9)
add_at(axes[0,2], "C")

# subplot 4
axes[1,0] = fig.add_subplot(234)
axes[1,0] = sns.kdeplot(df['profile16'], shade=True, color="r")
axes[1,0] = sns.kdeplot(df['profile17'], shade=True, color="#ffd900")
axes[1,0] = sns.kdeplot(df['profile18'], shade=True, color="b")
axes[1,0] = sns.kdeplot(df['profile19'], shade=True, color="#c3d825")
axes[1,0] = sns.kdeplot(df['profile20'], shade=True, color="#00a3af")
plt.title("profiles 16-20")
add_at(axes[1,0], "D")

# subplot 5
axes[1,1] = fig.add_subplot(235)
axes[1,1] = sns.kdeplot(df['profile21'], shade=True, color="r")
axes[1,1] = sns.kdeplot(df['profile22'], shade=True, color="#ffd900")
axes[1,1] = sns.kdeplot(df['profile23'], shade=True, color="b")
axes[1,1] = sns.kdeplot(df['profile24'], shade=True, color="#c3d825")
axes[1,1] = sns.kdeplot(df['profile25'], shade=True, color="#00a3af")
plt.title("profiles 21-25")
add_at(axes[1,1], "E")

# subplot 6
axes[1,2] = fig.add_subplot(236)
axes[1,2] = sns.kdeplot(dfM['Min'], shade=True, color="r")
axes[1,2] = sns.kdeplot(dfM['Mean'], shade=True, color="#ffd900")
axes[1,2] = sns.kdeplot(dfM['Max'], shade=True, color="b")
axes[1,2] = sns.kdeplot(dfM['1stQ'], shade=True, color="#65318e")
axes[1,2] = sns.kdeplot(dfM['3rdQ'], shade=True, color="#00a3af")
plt.title("bathymetric depth ranges, profiles 1-25")
add_at(axes[1,2], "F")

# visualizing and saving
plt.tight_layout()
plt.subplots_adjust(top=0.90, bottom=0.08,
                    left=0.10, right=0.95,
                    hspace=0.3, wspace=0.3
                    )
plt.savefig('plot_KDE.png', dpi=300)
plt.show()
