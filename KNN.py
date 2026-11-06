from ratings import *

chosen = []
total = 0
k = 3

def distance(a, b):
    across = ratings[a]["chocolate"] - ratings[b]["chocolate"]
    up = ratings[a]["fruit"] - ratings[b]["fruit"]
    return across * across + up * up

def find_closest():
    lowest = float("inf")
    closest = None
    for name in ratings:
        if name != "Priya" and name not in chosen:
            if distance("Priya", name) < lowest:
                lowest = distance("Priya", name)
                closest = name
    return closest

for _ in range(k):
    freind = find_closest()
    chosen.append(freind)

for freind in chosen:
    total = total + ratings[freind]["smoothie"]

