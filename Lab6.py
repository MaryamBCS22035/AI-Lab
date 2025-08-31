class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def dfs_iterative(self, s):
        visited = set()
        stack = []
        stack.append(s)

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                if node in self.adj:
                    for neighbour in reversed(self.adj[node]):
                        if neighbour not in visited:
                            stack.append(neighbour)

    def dfs_recursive(self, s, visited=None):
        if visited is None:
            visited = set()

        visited.add(s)
        print(s, end=" ")

        if s in self.adj:
            for w in self.adj[s]:
                if w not in visited:
                    self.dfs_recursive(w, visited)

# Example usage
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(2, 1)
g.addEdge(3, 1)

print("\nDFS Iterative:")
g.dfs_iterative(1)

print("\nDFS Recursive:")
g.dfs_recursive(1)


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def DFS(self, start, goal):
        visited = set()
        stack = []
        stack.append(start)

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                if node == goal:
                    print("Goal Node found")
                    return

                
                if node in self.adj:
                    for neighbour in reversed(self.adj[node]):
                        if neighbour not in visited:
                            stack.append(neighbour)

# Build graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('B', 'A')
g.add_edge('D', 'G')
g.add_edge('D', 'A')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('E', 'A')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('K', 'B')
g.add_edge('F', 'A')
g.add_edge('G', 'D')
g.add_edge('C', 'E')
g.add_edge('H', 'E')
g.add_edge('I', 'L')
g.add_edge('I', 'E')
g.add_edge('N', 'K')
g.add_edge('M', 'K')
g.add_edge('L', 'I')


print("\nThe DFS Traversal of the Graph is:")
g.DFS('A', 'G')

