import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5 # The random.random() function calls for a random float number
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")