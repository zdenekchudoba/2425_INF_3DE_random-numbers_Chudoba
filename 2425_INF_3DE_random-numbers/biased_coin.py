import random

def flip_biased_coin(p):
    # Generujeme náhodné číslo mezi 0 a 1
    rand_num = random.random()
    # Porovnáme náhodné číslo s pravděpodobností p
    if rand_num < p:
        return "Heads"
    else:
        return "Tails"

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na Heads
