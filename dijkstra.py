import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv('metro.csv', index_col=None)

METRO = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Longitud')
# print(METRO.nodes())
# print(METRO.edges())
# print(METRO.order())

# for x in METRO.nodes():
#     if METRO.degree(x) > 2:
#         print(x)
#

djk_path = nx.dijkstra_path(METRO, source='Pantitlan', target='Tacubaya',weight=True)
print(djk_path)

ruta1 = METRO.subgraph(djk_path)

nx.draw(ruta1, with_labels=True)