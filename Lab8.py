import heapq

#Task 1
def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [(heuristic[start], start)]
    closed_list = set()
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current
    return None



# Task 2
def a_star_search(graph, start, goal, heuristic):
    open_list = [(heuristic[start], 0, start)]
    closed_list = set()
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, cost, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)
        for neighbor, weight in graph[current]:
            new_cost = g_cost[current] + weight
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, new_cost, neighbor))
                parent[neighbor] = current
    return None



# Romania Map Example

romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,
    'Zerind': 374
}

print(" Greedy Best First Search ")
gbfs_path = greedy_best_first_search(romania_map, 'Arad', 'Bucharest', heuristic)
print("Path (GBFS):", gbfs_path)

print("\n A* Search ")
astar_path = a_star_search(romania_map, 'Arad', 'Bucharest', heuristic)
print("Path (A*):", astar_path)


# Task 3
import heapq
class PuzzleState:
    def __init__(self, board, parent=None, move=None, g=0, h=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def get_neighbors(self):
        neighbors = []
        idx = self.board.index(0)
        x, y = divmod(idx, 3)
        moves = [(-1,0,"Up"), (1,0,"Down"), (0,-1,"Left"), (0,1,"Right")]
        for dx,dy,move in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nidx = nx*3 + ny
                new_board = list(self.board)
                new_board[idx], new_board[nidx] = new_board[nidx], new_board[idx]
                neighbors.append(PuzzleState(tuple(new_board), self, move, self.g+1))
        return neighbors

def misplaced_tiles(board, goal):
    return sum(1 for i in range(len(board)) if board[i] != 0 and board[i] != goal[i])

def a_star_puzzle(start, goal):
    open_list = []
    start_state = PuzzleState(start, g=0, h=misplaced_tiles(start, goal))
    heapq.heappush(open_list, start_state)
    closed = set()

    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal:
            path, moves = [], []
            while current:
                path.append(current.board)
                if current.move:
                    moves.append(current.move)
                current = current.parent
            return path[::-1], moves[::-1]

        closed.add(current.board)
        for neighbor in current.get_neighbors():
            if neighbor.board not in closed:
                neighbor.h = misplaced_tiles(neighbor.board, goal)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(open_list, neighbor)
    return None, None




print("\n 8 Puzzle Problem with A*")
start = (0, 3, 2,
        4, 1, 6,
        7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution, moves = a_star_puzzle(start, goal)
print("Moves to solve puzzle:", moves)
print("Solution path (boards):")
for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print("-----")
