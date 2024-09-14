import graph_tool.all as gt
import networkx as nx
import time
import os

graph_name = "Drosophila"
# Crea la cartella se non esiste
os.makedirs(f"datasets/saved/{graph_name}", exist_ok=True)

# Carica il grafo
g = gt.collection.ns["genetic_multiplex/Drosophila"]

# Converti il grafo in un formato compatibile con NetworkX
nx_g = nx.Graph()
for v in g.vertices():
    nx_g.add_node(int(v))
for e in g.edges():
    nx_g.add_edge(int(e.source()), int(e.target()))

# Calcola la betweenness centrality e misura il tempo di esecuzione
start_time = time.time()
betweenness = nx.betweenness_centrality(nx_g)
end_time = time.time()
execution_time = end_time - start_time

# Salva la betweenness centrality in un file
with open(f"datasets/saved/{graph_name}/betweenness.txt", "w") as f:
    for v, b in betweenness.items():
        f.write(f"{v} {b}\n")

# Salva il tempo di esecuzione in un file
with open(f"datasets/saved/{graph_name}/execution_time.txt", "w") as f:
    f.write(str(execution_time))

# Salva il grafo in un file
nx.write_graphml(nx_g, f"datasets/saved/{graph_name}/graph.graphml")