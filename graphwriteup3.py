import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Defining the celebrities and their connections
celebrities = {
    "Taylor Swift": ["Ed Sheeran", "Selena Gomez", "Ariana Grande", "Justin Bieber"],
    "Ed Sheeran": ["Taylor Swift", "Justin Bieber", "Beyoncé", "Selena Gomez"],
    "Selena Gomez": ["Taylor Swift", "Ariana Grande", "Kim Kardashian", "Kylie Jenner"],
    "Ariana Grande": ["Selena Gomez", "Beyoncé", "Justin Bieber", "Dwayne Johnson", "Kim Kardashian"],
    "Justin Bieber": ["Ed Sheeran", "Ariana Grande", "Kim Kardashian", "Taylor Swift"],
    "Beyoncé": ["Kim Kardashian", "Jay-Z"],
    "Jay-Z": ["Beyoncé"],
    "Kim Kardashian": ["Beyoncé", "Taylor Swift", "Justin Bieber", "Kylie Jenner"],
    "Dwayne Johnson": ["Beyoncé", "Ariana Grande", "Kevin Hart"],
    "Kevin Hart": ["Dwayne Johnson", "Ellen DeGeneres"],
    "Ellen DeGeneres": ["Kevin Hart", "Oprah Winfrey"],
    "Oprah Winfrey": ["Ellen DeGeneres", "Jay-Z", "Michelle Obama"],
    "Michelle Obama": ["Oprah Winfrey", "Beyoncé"],
    "Kylie Jenner": ["Kim Kardashian", "Kendall Jenner", "Selena Gomez"],
    "Kendall Jenner": ["Kylie Jenner", "LeBron James"],
    "LeBron James": ["Kendall Jenner", "Taylor Swift", "Beyoncé"]
}

# Creating a list of all unique celebrities
unique_celebrities = list(set([celeb for connections in celebrities.values() for celeb in connections] + list(celebrities.keys())))
unique_celebrities.sort()

# Creating an adjacency matrix
adjacency_matrix = np.zeros((len(unique_celebrities), len(unique_celebrities)))

# Populating the adjacency matrix
for i, celeb in enumerate(unique_celebrities):
    for connection in celebrities.get(celeb, []):
        j = unique_celebrities.index(connection)
        adjacency_matrix[i][j] = 1

# Creating a directed graph
G = nx.DiGraph()

# Adding nodes and edges to the graph
for celeb in unique_celebrities:
    G.add_node(celeb)
    for connection in celebrities.get(celeb, []):
        G.add_edge(celeb, connection)

# Plotting the directed graph
plt.figure(figsize=(12, 12))
nx.draw_networkx(G, with_labels=True, pos=nx.spring_layout(G), node_color="red", alpha=0.9, edge_color="black", font_size=11, font_family = "Times new roman")
plt.title("Celebrity Connection Graph")
plt.show()

# Displaying the adjacency matrix
print(adjacency_matrix, unique_celebrities)
