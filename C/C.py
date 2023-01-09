# Initialize our union_find dictionary with elements as keys and themselves as values
def initialize(pairs):
    union_find = {}
    for pair in pairs:
        person1, person2 = pair
        union_find[person1] = person1
        union_find[person2] = person2
    return union_find

# Function to get the representative of a person, all linked people have the same parent 
def get_repres(union_find, person):
    if person == union_find[person]:
        return person
    else:
        union_find[person] = get_repres(union_find, union_find[person]) 
        return union_find[person]
    
# iterate through the pairs and unite them.
def unite_people(pairs, union_find):
    for person1, person2 in pairs:
        representative1 = get_repres(union_find, person1)
        representative2 = get_repres(union_find, person2)
        if representative1 != representative2: 
            union_find[representative2] = representative1
    
# create groups. Iterate over the representatives to get the groups that are connected.
def create_groups(pairs):
    groups = {}
    for person in union_find:
        representative = get_repres(union_find, person)
        if representative in groups:
            groups[representative].add(person)
        else:
            groups[representative] = {person}

    return groups


pairs = [("Ana", "Carlos"), ("John", "Nikhil"), ("Ana", "Li")]

union_find = initialize(pairs)
unite_people(pairs, union_find)
groups = create_groups(union_find)

for group in groups.values():
  print(group)