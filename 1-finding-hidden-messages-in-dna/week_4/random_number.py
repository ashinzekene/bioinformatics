from random import choices
from functools import reduce
from math import gcd

def RandomNumber(probs):
    population = list(range(len(probs)))
    probs_sum  = sum(probs)
    probs = list(map(lambda x: x/probs_sum, probs))
    return choices(population, probs)[0]


if __name__ == "__main__":
    print(RandomNumber([1/4, 1/12, 1/2]))
