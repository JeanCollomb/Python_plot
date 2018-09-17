# -*- coding: utf-8 -*-
"""
Quelques scripts pour les tracés usuels sous Python
"""

###############################################################################
#####----> PACKAGES

import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

###############################################################################
#####----> DONNEES ALEATOIRES

x       = [1,2,3,4,5]
y       = [random.random() for i in range(5)]
y2      = [random.random() for i in range(5)]
y3      = [random.random() for i in range(5)]


###############################################################################
#--- Trace simple d'une figure
plt.plot(x, y)                          # trace de y fonction de x
plt.grid(True)                          # activation de la grille
plt.xlim([1,5])                         # limites de l'axe x
plt.ylim([0,1])                         # limites de l'axe y
plt.xlabel('axe x')                     # nom de l'axe x
plt.ylabel('axe y')                     # nom de l'axe y
plt.title('Titre du graphique')         # titre du graphique
plt.show()                              # affichage de la figure


#--- Trace rigoureux d'une figure
fig, ax = plt.subplots()               # creation de la figure et des axes
ax.plot(x, y)                          # trace de y fonction de x
ax.grid(True)                          # activation de la grille
ax.set_xlim([1,5])                     # limites de l'axe x
ax.set_ylim([0,1])                     # limites de l'axe y
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique
fig.show()                             # affichage de la figure


#--- Trace multi-courbes simple
plt.plot(x, y, label='courbe 1')        # trace de y fonction de x
plt.plot(x, y2,label='courbe 2')        # trace de y2 fonction de x
plt.plot(x, y3,label='courbe 3')        # trace de y3 fonction de x
plt.grid(True)                          # activation de la grille
plt.xlim([1,5])                         # limites de l'axe x
plt.ylim([0,1])                         # limites de l'axe y
plt.legend(loc='best')                  # activation de la legende
plt.xlabel('axe x')                     # nom de l'axe x
plt.ylabel('axe y')                     # nom de l'axe y
plt.title('Titre du graphique')         # titre du graphique
plt.show() 


#--- Trace multi-courbes rigoureux
fig, ax = plt.subplots()               # creation de la figure et des axes
ax.plot(x, y, label='courbe 1')        # trace de y fonction de x
ax.plot(x, y2,label='courbe 2')        # trace de y2 fonction de x
ax.plot(x, y3,label='courbe 3')        # trace de y3 fonction de x
ax.grid(True)                          # activation de la grille
ax.set_xlim([1,5])                     # limites de l'axe x
ax.set_ylim([0,1])                     # limites de l'axe y
ax.legend(loc='best')                  # activation de la legende
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique
fig.show() 


###############################################################################
#--- Courbes subplot - axe y en commun
fig, axes = plt.subplots(1, 2, sharey=True) # creation des subplots
axes[0].plot(x, y, label='courbe 1')        # premier plot 1
axes[0].plot(x, y2,label='courbe 2')        # premier plot 2
axes[0].set_title('SubFig 1')               # titre du premier plot
axes[0].grid(True)                          # activation de la grille
axes[0].set_xlim([1,5])                     # limites de l'axe x
axes[0].set_ylim([0,1])                     # limites de l'axe y
axes[0].legend(loc='best')                  # activation de la legende
axes[0].set_xlabel('axe x 1')               # nom de l'axe x
axes[0].set_ylabel('axe y 1')               # nom de l'axe y
axes[1].plot(x, y, label='courbe 1')        # premier plot 1
axes[1].plot(x, y3,label='courbe 3')        # premier plot 3
axes[1].set_title('SubFig 2')               # titre du premier plot
axes[1].grid(True)                          # activation de la grille
axes[1].set_xlim([1,5])                     # limites de l'axe x
axes[1].set_ylim([0,1])                     # limites de l'axe y
axes[1].legend(loc='best')                  # activation de la legende
axes[1].set_xlabel('axe x 2')               # nom de l'axe x
fig.show() 


#--- Courbes subplot - axes y differents
fig, axes = plt.subplots(2, 2)                # creation des subplots
axes[0,0].plot(x, y, label='courbe 1')        # premier plot 1
axes[0,0].plot(x, y2,label='courbe 2')        # premier plot 2
axes[0,0].grid(True)                          # activation de la grille
axes[0,0].set_xlim([1,5])                     # limites de l'axe x
axes[0,0].set_ylim([0,1])                     # limites de l'axe y
axes[0,0].legend(loc='best')                  # activation de la legende
axes[1,0].plot(x, y, label='courbe 1')        # premier plot 1
axes[1,0].plot(x, y3,label='courbe 3')        # premier plot 3
axes[1,0].grid(True)                          # activation de la grille
axes[1,0].set_xlim([1,5])                     # limites de l'axe x
axes[1,0].set_ylim([0,1])                     # limites de l'axe y
axes[1,0].legend(loc='best')                  # activation de la legende
axes[0,1].plot(x, y, label='courbe 1')        # premier plot 1
axes[0,1].plot(x, y3,label='courbe 3')        # premier plot 3
axes[0,1].grid(True)                          # activation de la grille
axes[0,1].set_xlim([1,5])                     # limites de l'axe x
axes[0,1].set_ylim([0,1])                     # limites de l'axe y
axes[0,1].legend(loc='best')                  # activation de la legende
axes[1,1].plot(x, y, label='courbe 1')        # premier plot 1
axes[1,1].plot(x, y3,label='courbe 3')        # premier plot 3
axes[1,1].grid(True)                          # activation de la grille
axes[1,1].set_xlim([1,5])                     # limites de l'axe x
axes[1,1].set_ylim([0,1])                     # limites de l'axe y
axes[1,1].legend(loc='best')                  # activation de la legende
fig.show() 


###############################################################################
#--- Courbes avec marqueurs et couleurs
fig, ax = plt.subplots()               # creation de la figure et des axes
ax.plot(x, y, 
        label='courbe 1', 
        color='blue',
        linestyle='-',
        marker='o',
        markevery=1)                   # trace de y fonction de x
ax.plot(x, y2, 
        label='courbe 2', 
        color='red',
        linestyle='--',
        marker='+',
        markevery=1)                   # trace de y2 fonction de x
ax.plot(x, y3, 
        label='courbe 3', 
        color='green',
        linestyle='-.',
        marker='s',
        markevery=1)                   # trace de y3 fonction de x
ax.grid(True)                          # activation de la grille
ax.set_xlim([1,5])                     # limites de l'axe x
ax.set_ylim([0,1])                     # limites de l'axe y
ax.legend(loc='best')                  # activation de la legende
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique
fig.show()


#--- Incertitudes

x       = [i for i in range(10)]
y1      = [random.randint(1,10) for i in range(10)]
y2      = [random.randint(1,10) for i in range(10)]
std1    = [random.randint(0,2) for i in range(10)]
std2    = [random.randint(0,2) for i in range(10)]

fig, ax = plt.subplots()               # creation de la figure et des axes
ax.plot(x, y1, 
        label='courbe 1', 
        color='blue',
        linestyle='-',
        marker='o',
        markevery=1)                   # trace de y fonction de x
ax.plot(x, y2, 
        label='courbe 2', 
        color='red',
        linestyle='--',
        marker='+',
        markevery=1)                   # trace de y2 fonction de x

ax.fill_between(x, np.array(y1) - np.array(std1), 
                np.array(y1) + np.array(std1))

ax.fill_between(x, np.array(y2) - np.array(std2), 
                np.array(y2) + np.array(std2))

ax.grid(True)                          # activation de la grille
ax.set_xlim([0,10])                    # limites de l'axe x
ax.set_ylim([0,10])                    # limites de l'axe y
ax.legend(loc='best')                  # activation de la legende
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique
fig.show()


###############################################################################
#--- Exemple de trace et d'export après recuperation dans un excel
data = pd.read_excel('exemple.xlsx')

fig, ax = plt.subplots()               # creation de la figure et des axes
ax.plot(data['temps'], data['T1'], 
        label='courbe 1', 
        color='blue',
        linestyle='-',
        marker='o',
        markevery=1)                   # trace de y fonction de x
ax.plot(data['temps'], data['T2'], 
        label='courbe 2', 
        color='red',
        linestyle='--',
        marker='+',
        markevery=1)                   # trace de y2 fonction de x
ax.plot(data['temps'], data['T3'], 
        label='courbe 3', 
        color='green',
        linestyle='-.',
        marker='s',
        markevery=1)                   # trace de y3 fonction de x

ax.fill_between(data['temps'], data['T1'] - data['std1'], 
                data['T1'] + data['std1'], alpha=0.4)

ax.fill_between(data['temps'],data['T2'] -data['std2'], 
                data['T2'] + data['std2'], alpha=0.4)

ax.fill_between(data['temps'],data['T3'] -data['std3'], 
                data['T3'] + data['std3'], alpha=0.4)

ax.grid(True)                          # activation de la grille
ax.set_xlim([1,20])                    # limites de l'axe x
ax.set_ylim([0,60])                    # limites de l'axe y
ax.legend(loc='best')                  # activation de la legende
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique
fig.savefig('exemple.png', dpi=300)
fig.savefig('exemple.pdf')
fig.savefig('exemple.svg')


###############################################################################
#--- Exemple de trace automatique après recuperation dans un excel

data = pd.read_excel('exemple.xlsx')

labels = list(data)                     # recuperation des labels
labels.pop(0)                           # suppression du label 'temps'

colors      = ['red', 'blue', 'green']
linestyles  = ['-', '--', '-.']
markers     = ['o', 's', '+']

fig, ax = plt.subplots()                # creation de la figure et des axes

for label in range(3):
    
    ax.plot(data['temps'], data[labels[label]], 
            label='{nom_label}'.format(nom_label = 'courbe ' + labels[label]), 
            color='{nom_couleur}'.format(nom_couleur = colors[label]),
            linestyle='{nom_style}'.format(nom_style = linestyles[label]),
            marker='{nom_markeur}'.format(nom_markeur = markers[label]),
            markevery=1)                   # trace de y fonction de x
    
    ax.fill_between(data['temps'], data[labels[label]] - data[labels[label+9]], 
                    data[labels[label]] + data[labels[label+9]], alpha=0.4)

ax.grid(True)                          # activation de la grille
ax.set_xlim([1,20])                    # limites de l'axe x
ax.set_ylim([0,60])                    # limites de l'axe y
ax.legend(loc='best')                  # activation de la legende
ax.set_xlabel('axe x')                 # nom de l'axe x
ax.set_ylabel('axe y')                 # nom de l'axe y
ax.set_title('Titre du graphique')     # titre du graphique

