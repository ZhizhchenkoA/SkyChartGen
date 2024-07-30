import random


def random_cords(min_phi=-90.0, max_phi=90.0):
    time = random.randint(0, 3599)
    phi = round(random.uniform(min_phi, max_phi), 2)
    return time, phi

print(random_cords())