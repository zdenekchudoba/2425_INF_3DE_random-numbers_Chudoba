import random

def flip_coin():
    # Generujeme náhodné číslo mezi 0 a 1
    rand_num = random.random()
    # Pokud je číslo menší než 0.5, vrátíme "Heads", jinak "Tails"
    if rand_num < 0.5:
        return "Heads"
    else:
        return "Tails"

# Otestování funkce
print(flip_coin())  # Simulace hodu s rovnou šancí na Heads nebo Tails
