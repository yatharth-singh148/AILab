# Alpha-Beta Pruning for Batch 3 Tree

def alpha_beta(node, alpha, beta, is_max, tree, path, pruned):
    path.append(node)

    # Leaf node → direct numeric value
    if isinstance(node, int):
        return node

    # Internal node → look up children
    children = tree[node]

    if is_max:
        value = float('-inf')
        for child in children:
            child_value = alpha_beta(child, alpha, beta, False, tree, path, pruned)
            value = max(value, child_value)
            alpha = max(alpha, value)

            # Pruning
            if beta <= alpha:
                pruned.append((node, child))
                break
        return value

    else:  # MIN node
        value = float('inf')
        for child in children:
            child_value = alpha_beta(child, alpha, beta, True, tree, path, pruned)
            value = min(value, child_value)
            beta = min(beta, value)

            if beta <= alpha:
                pruned.append((node, child))
                break
        return value

tree = {
    "A": ["B", "C"],

    "B": ["D", "E"],
    "C": ["F", "G"],

    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],

    "H": [10, 11],
    "I": [9, 12],
    "J": [14, 15],
    "K": [13, 14],
    "L": [5, 2],
    "M": [4, 1],
    "N": [3, 22],
    "O": [20, 21]
}

path = []
pruned = []

# Start α = -∞, β = +∞, root is MAX node
result = alpha_beta("A", float('-inf'), float('inf'), True, tree, path, pruned)

print("\n=== Alpha-Beta Pruning (Batch 3) ===")
print("Root Value:", result)
print("Visited Path:", path)
print("Pruned Branches:", pruned)
