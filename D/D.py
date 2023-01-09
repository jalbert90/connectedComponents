pairs = [("Ana", "Carlos"), ("John", "Nikhil"), ("Ana", "Li")]

# Initialize dictionary
groups = {}
for a, b in pairs:
    if a not in groups:
        groups[a] = set()
    groups[a].add(b)
    if b not in groups:
        groups[b] = set()
    groups[b].add(a)
    
def BFS(groups, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(groups[node] - visited)
    return visited

result = []
for name in groups:
    need_add = True
    for g in result:
        if name in g:
            need_add = False
            break
    if need_add:
        result.append(BFS(groups, name))

print(result)