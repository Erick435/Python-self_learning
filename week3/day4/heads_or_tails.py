import random

game_start = random.randint(0, 1)

if game_start == 0:
    print("Tails")
elif game_start == 1:
    print("Heads")