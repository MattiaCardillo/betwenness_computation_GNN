import os
import networkx as nx

def create_graph_from_mtx_library(file_path, library):
    if(library != None):
        return library
    
    # Crea un grafo vuoto
    g = nx.Graph()

    # Percorso assoluto del file .mtx
    abs_file_path = os.path.abspath(file_path)

    # Verifica se il file esiste
    if not os.path.exists(abs_file_path):
        raise FileNotFoundError(f"Il file {abs_file_path} non esiste.")

    # Leggi il file .mtx
    with open(abs_file_path, 'r') as file:
        for line in file:
            # Salta i commenti e la prima linea con dimensioni (inizia con '%')
            if line.startswith('%'):
                continue

            # Split per ottenere gli elementi di ogni riga
            row = line.strip().split()

            # Se la riga contiene 2 o 3 numeri, è un arco
            if len(row) >= 2:
                u, v = int(row[0]), int(row[1])

                # Aggiungi l'arco al grafo
                g.add_edge(u, v)
    
    num_nodes_graph = g.number_of_nodes()
    num_edges_graph = g.number_of_edges()
    
    print(f"Graph: {file_path} loaded")
    print(f"Number of nodes: {num_nodes_graph}")
    print(f"Number of edges: {num_edges_graph}")

    return g