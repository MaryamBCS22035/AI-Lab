class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    # Depth Limited Search
    def DLS(self, src, target, limit, path=None):
        if path is None:
            path = [src]

        if src == target:
            return True, path
        if limit <= 0:
            return False, path

        if src not in self.adj:
            return False, path

        for neighbor in self.adj[src]:
            found, new_path = self.DLS(neighbor, target, limit - 1, path + [neighbor])
            if found:
                return True, new_path

        return False, path

    # Iterative Deepening Search
    def IDDFS(self, src, target, max_depth):
        for depth in range(max_depth + 1):
            found, path = self.DLS(src, target, depth)
            if found:
                return True, path
        return False, []


# Build the tree from the image
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')

g.add_edge('B', 'K')
g.add_edge('B', 'J')

g.add_edge('K', 'N')
g.add_edge('K', 'M')

g.add_edge('D', 'G')

g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')

g.add_edge('I', 'L')

# Apply DLS with limits
print("DLS (limit = 1):", g.DLS('A', 'G', 1))   # should fail
print("DLS (limit = 2):", g.DLS('A', 'G', 2))   # should succeed
print("DLS (limit = 3):", g.DLS('A', 'G', 3))   # still succeeds

# Apply IDDFS
print("IDDFS (max depth = 3):", g.IDDFS('A', 'G', 3))
