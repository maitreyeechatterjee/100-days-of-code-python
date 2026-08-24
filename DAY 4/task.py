import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option 1
random_item = random.choice(friends)
print(random_item)

#option 2
random_index = random.randint(0,4)
print(friends[random_index])
