def dfs(visited,person,groups,connections):
    visited.add(person)
    groups.add(person)
    for p in connections[person]:
        if p not in visited:
            dfs(visited,p,groups,connections)

pairs = [("Ana", "Carlos"), ("John", "Nikhil"), ("Ana", "Li")]

groups = []
connections = {}
visited = set()

for person1, person2 in pairs:
    if person1 not in connections:
        connections[person1] = []
    connections[person1].append(person2)
    if person2 not in connections:
        connections[person2] = []
    connections[person2].append(person1)        
        
for person in connections:
    if person not in visited:
        groupsSet = set()
        dfs(visited,person,groupsSet,connections)
        groups.append(groupsSet)
        
print(groups)