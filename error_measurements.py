# Function to calculate mean squared error manually
def mean_squared_error(y_true, y_pred):
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)

# Function to get top N nodes by betweenness centrality
def get_top_n_betweenness(betweenness_dict, n):
    return sorted(betweenness_dict.items(), key=lambda item: item[1], reverse=True)[:n]