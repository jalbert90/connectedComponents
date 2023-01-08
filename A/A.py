pairs = [("Ana", "Carlos"), ("Nikhil", "John"), ("Ana", "Li")]

# Create an dictionary that will serve as a structure for the disjoint sets
parent = {}
rank = {}

# Helper function for find the parent
def find(person):
  if parent[person] != person:
    parent[person] = find(parent[person]) 
  return parent[person]

# Helper function for union  
def union(person1, person2):
  root1 = find(person1)
  root2 = find(person2)
 
  #Rank is used to keep the tree flat
  if root1 != root2:
    if rank[root1] > rank[root2]:
      parent[root2] = root1
    else:
      parent[root1] = root2
      if rank[root1] == rank[root2]: 
        rank[root2] += 1

# Initialize and create struture for the disjoint-set of every person.
for pair in pairs:
  for person in pair:
    if person not in parent:
      parent[person] = person
      rank[person] = 0
      
      
# Union every pair in the pairs list
for person1, person2 in pairs:
  union(person1, person2)

#Group that will store each connected component
groups = {}

# Iterate to group the people by components
for person in parent.keys():
  # find the representative of the  group
  root = find(person)
  # Create an empty list for the representative of each group
  if root not in groups:
    groups[root] = []
  groups[root].append(person)

print(f"{groups.values()}")