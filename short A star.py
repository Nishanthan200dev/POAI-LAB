import heapq

class Node:
    def __init__(self, pos, parent=None, g=0, h=0):
        self.pos = pos
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))
    closed = set()
    while open_list:
        curr = heapq.heappop(open_list)
        if curr.pos == goal:
            path = []
            while curr:
                path.append(curr.pos)
                curr = curr.parent
            return path[::-1]
        closed.add(curr.pos)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = curr.pos[0] + dr, curr.pos[1] + dc
            new_pos = (nr, nc)
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and new_pos not in closed:
                heapq.heappush(open_list, Node(new_pos, curr, curr.g+1, heuristic(new_pos, goal)))
    return None

# Example
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)
print("Optimal Path:", path)
