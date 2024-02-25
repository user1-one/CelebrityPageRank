import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges (connections) to the graph (Edge,Edge)
connections = [
    ('Taylor Swift', 'Ed Sheeran'), ('Taylor Swift', 'Selena Gomez'),
    ('Taylor Swift', 'Ariana Grande'), ('Taylor Swift', 'Justin Bieber'),
    ('Ed Sheeran', 'Taylor Swift'), ('Ed Sheeran', 'Justin Bieber'),
    ('Ed Sheeran', 'Beyoncé'), ('Ed Sheeran', 'Selena Gomez'),
    ('Selena Gomez', 'Taylor Swift'), ('Selena Gomez', 'Ariana Grande'),
    ('Selena Gomez', 'Kim Kardashian'), ('Selena Gomez', 'Kylie Jenner'),
    ('Ariana Grande', 'Selena Gomez'), ('Ariana Grande', 'Beyoncé'),
    ('Ariana Grande', 'Justin Bieber'), ('Ariana Grande', 'Dwayne Johnson'),
    ('Ariana Grande', 'Kim Kardashian'), ('Justin Bieber', 'Ed Sheeran'),
    ('Justin Bieber', 'Ariana Grande'), ('Justin Bieber', 'Kim Kardashian'),
    ('Justin Bieber', 'Taylor Swift'), ('Beyoncé', 'Kim Kardashian'),
    ('Beyoncé', 'Jay-Z'), ('Jay-Z', 'Beyoncé'),
    ('Kim Kardashian', 'Beyoncé'), ('Kim Kardashian', 'Taylor Swift'),
    ('Kim Kardashian', 'Justin Bieber'), ('Kim Kardashian', 'Kylie Jenner'),
    ('Dwayne Johnson', 'Beyoncé'), ('Dwayne Johnson', 'Ariana Grande'),
    ('Dwayne Johnson', 'Kevin Hart'), ('Kevin Hart', 'Dwayne Johnson'),
    ('Kevin Hart', 'Ellen DeGeneres'), ('Ellen DeGeneres', 'Kevin Hart'),
    ('Ellen DeGeneres', 'Oprah Winfrey'), ('Oprah Winfrey', 'Ellen DeGeneres'),
    ('Oprah Winfrey', 'Jay-Z'), ('Oprah Winfrey', 'Michelle Obama'),
    ('Michelle Obama', 'Oprah Winfrey'), ('Michelle Obama', 'Beyoncé'),
    ('Kylie Jenner', 'Kim Kardashian'), ('Kylie Jenner', 'Kendall Jenner'),
    ('Kylie Jenner', 'Selena Gomez'), ('Kendall Jenner', 'Kylie Jenner'),
    ('Kendall Jenner', 'LeBron James'), ('LeBron James', 'Kendall Jenner'),
    ('LeBron James', 'Taylor Swift'), ('LeBron James', 'Beyoncé')
]

G.add_edges_from(connections) # G is the directed graph containing our celebrities

# Compute PageRank
pagerank = nx.pagerank(G, alpha=0.15)  # alpha is the damping factor p 

# Sort the PageRank  in descending order
sorted_ranks = sorted(pagerank.items(), key=lambda item: item[1], reverse=True)

# Iterate over the sorted ranks and print them
for celebrity, rank in sorted_ranks:
    print(f"{celebrity}: {(rank):.3f}") # prints to 3 decimal places

