import sys
import os

sys.path.append(os.path.abspath(".."))

from week_1.de_bruijn_kmers import DeBruijnKmers
from week_1.genome_path import GenomePath
from eulerian_path import EulerianPath

def StringReconstruction(kmers):
    db = DeBruijnKmers(kmers)
    path = EulerianPath(db)
    return GenomePath(path)

def GenerateKmers(k):
    kmers = []
    formatter = "{0:0>%db}" % k
    for i in range(2**k):
        kmers.append(formatter.format(i))
    return kmers

if __name__ == "__main__":
    count = 0
    with open('./datasets/dataset_203_11.txt') as f:
        count = int(f.read().strip())
    kmers = GenerateKmers(count)
    result = StringReconstruction(kmers)[:2**count]
    print(result)
    with open('./results/universal_circular_string.txt', 'w') as f:
        f.write(result)
    