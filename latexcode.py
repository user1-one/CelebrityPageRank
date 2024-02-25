import numpy as np

# Define your celebrities and their connections
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

# Create a list of all unique celebrities
unique_celebrities = sorted(set(celeb for connections in celebrities.values() for celeb in connections).union(celebrities.keys()))

# Create an adjacency matrix
adjacency_matrix = np.zeros((len(unique_celebrities), len(unique_celebrities)), dtype=int)

# Populate the adjacency matrix
for i, celeb in enumerate(unique_celebrities):
    for connection in celebrities.get(celeb, []):
        j = unique_celebrities.index(connection)
        adjacency_matrix[i, j] = 1

# Function to format the matrix for LaTeX
def matrix_to_latex(matrix, labels):
    latex = "\\begin{bmatrix}\n"
    for row in matrix:
        latex += " & ".join(map(str, row)) + " \\\\\n"
    latex += "\\end{bmatrix}\n"
    return latex

# Convert the matrix to LaTeX format
latex_matrix = matrix_to_latex(adjacency_matrix, unique_celebrities)

# Print the LaTeX formatted matrix
print(latex_matrix)
