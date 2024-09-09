import time
import networkx as nx
    
def calculate_betweenness_centrality(graph):

    start_time = time.time()
    betweenness = nx.betweenness_centrality(graph, normalized=True)
    end_time = time.time()

    computation_time = end_time - start_time
    return betweenness, computation_time


def calculate_betweenness_centrality_approximated(graph, approximation_factor, seed=42):

    start_time = time.time()
    betweenness = nx.betweenness_centrality(graph, k=int(graph.number_of_nodes()*approximation_factor), normalized=True, seed=seed)
    end_time = time.time()

    computation_time = end_time - start_time
    return betweenness, computation_time
