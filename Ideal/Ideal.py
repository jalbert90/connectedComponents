pairs = [("Ana", "Carlos"), ("Nikhil", "John"), ("Ana", "Li")]

# Create dictionaries to represent the parent and rank of each element
parent = {}
rank = {}

# Helper function to find the parent
def find(person):
  if parent[person] != person:
    parent[person] = find(parent[person]) 
  return parent[person]

# Helper function to replace two disjoint sets with their union
def union(person1, person2):
  root1 = find(person1)
  root2 = find(person2)
 
  # Rank is used to keep the tree flat
  if root1 != root2:
    if rank[root1] > rank[root2]:
      parent[root2] = root1
    else:
      parent[root1] = root2
      if rank[root1] == rank[root2]: 
        rank[root2] += 1

# Set each person as their own parent, and set their rank to 0
for pair in pairs:
  for person in pair:
    if person not in parent:
      parent[person] = person
      rank[person] = 0
      
# Take the union of every pair in the pairs list
for person1, person2 in pairs:
  union(person1, person2)

# Group that will store each connected component
groups = {}

# Iterate through each person, and group them by their parent
for person in parent.keys():
  # Find the representative of the group
  root = find(person)
  # Create an empty list for the representative of each group
  if root not in groups:
    groups[root] = []
  groups[root].append(person)

# Print out the connected components
for representative in groups:
    print(groups[representative])