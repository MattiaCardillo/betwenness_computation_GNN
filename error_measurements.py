def get_betweenness_comparison_table(top_x_exact, top_x_approx, computation_time, computation_time_approx, classification_nodes):
    import pandas as pd  # Aggiungi questa riga

    # Creazione del DataFrame
    df = pd.DataFrame({
        'Rank': range(1, classification_nodes+1),
        'Exact Calc.': [node for node, _ in top_x_exact],
        'Approx Calc.': [node for node, _ in top_x_approx],
        'Exact comp. time': computation_time,
        'Approx comp. time': computation_time_approx,
        'Time diff': computation_time - computation_time_approx
    })

    df['Correct'] = (df['Exact Calc.'] == df['Approx Calc.'])

    return df
