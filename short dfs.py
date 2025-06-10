graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(g, start, goal, visited=set(), path=[]):
    visited.add(start)
    path = path + [start]
    if start == goal:
        return path
    for neighbor in g[start]:
        if neighbor not in visited:
            res = dfs(g, neighbor, goal, visited, path)
            if res:
                return res
    return None

print("DFS Path from A to F:", dfs(graph, 'A', 'F'))
