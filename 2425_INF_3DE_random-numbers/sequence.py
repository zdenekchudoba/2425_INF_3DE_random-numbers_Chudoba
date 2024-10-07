import random

def generate_sequence(n):
    # Generujeme sekvenci n náhodných čísel
    return [random.randint(1, 100) for _ in range(n)]  # Čísla mezi 1 a 100

# Otestování funkce
print(generate_sequence(10))  # Vygeneruje 10 náhodných čísel
