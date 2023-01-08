pairs = [("Ana", "Carlos"), ("John", "Nikhil"), ("Ana", "Li")]

# Create an empty dictionary
groups = {}

# Iterate over the pairs in the list
for person1, person2 in pairs:
  # If either person is not in the dictionary, create a new entry with an empty set
  if person1 not in groups:
    groups[person1] = set()
  if person2 not in groups:
    groups[person2] = set()

  # Add both people to the set associated with each person
  groups[person1].add(person2)
  groups[person2].add(person1)

# Print the groups
for person, group in groups.items():
  print(f"{group}")