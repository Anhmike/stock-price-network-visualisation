#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Zhongjiulu
"""

import pandas as pd
import networkx as nx
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sys

# data wrangling
stock = pd.read_csv('asset_prices.csv')
df = pd.DataFrame(stock)
df = df.set_index('Date') # set the data column as row names
matrix = df.corr() # correlation matrix

"""
The below graphs show matrix as a network using different graph layouts, 
they are circular, random, spectral and spring. 
As I can see that circular graph is able to display all the relationship 
across different assets, 
meanwhile, although other graph layouts display the correlation between 
different assets, it does not provide as explicit as circular layout. 
Therefore, I believe circular graph layout is the best.
"""

# read the correlation matrix as an adjacency matrix as a undirected graph
G = nx.to_networkx_graph(matrix)
#check if read correctly
#nx.write_weighted_edgelist(G,sys.stdout)
#different type of graphs
plt.subplot(221)
nx.draw_circular(G, with_labels=True, node_size = 400)
plt.subplot(222)
nx.draw_random(G, with_labels=True, node_size = 400)
plt.subplot(223)
nx.draw_spectral(G, with_labels=True, node_size = 400)
plt.subplot(224)
nx.draw_spring(G, with_labels=True, node_size = 400)

plt.rcParams['figure.figsize'] = [15,15]
#nx.draw_shell(G, with_labels=True, node_size = 400) # looks the same as circular

"""
We are interested in the weak correlation between different assets for 
investment point of view, as investors want to diversify their portfolio
 to reduce the risk. It would be ideal to invest on the the assets that have 
 the least correlation between each other.

This leads to an ideal graph that can clearly display the assets with 
weak correlations and having their name clearly shown.

"""
width = [G[u][v]['weight'] for u,v in G.edges()] # put weight on the edges according to its correlation
degreez_size = nx.degree(G)
nx.draw_circular(G, with_labels=True, 
                 node_color = 'lightblue', 
                 font_size = 8,width = width, 
                 edge_color = 'lightblue',node_size = 100)

"""
find out assets with weak correlations
"""

matrix_new = matrix.copy()
for i in list(range(39)):
    for j in list(range(39)):
        if abs(matrix_new.iloc[i ,j]) >= 0.5:
            matrix_new.iloc[i ,j] = 0







