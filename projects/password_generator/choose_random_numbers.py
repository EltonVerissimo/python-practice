import random

def chooseRandomNumbers(indexList, min, max):
    return random.choices(indexList, k=random.randint(min, max))