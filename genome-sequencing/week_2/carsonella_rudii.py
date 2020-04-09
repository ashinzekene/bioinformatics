import sys
import os

sys.path.append(os.path.abspath(".."))

from week_1.genome_path import GenomePath

from de_bruijn_paired_kmers import DeBruijnPairedKmers
from eulerian_path import EulerianPath
from paired_genome_path import PairedGenomePath

def PairedReconstruction(pairs, n, d):
    graph = DeBruijnPairedKmers(pairs)
    path = EulerianPath(graph)
    print(path)
    return PairedGenomePath(path, n, d)

if __name__ == "__main__":
    pair_length = 120
    divider = 1000
    pairs = []
    with open('./datasets/carsonella_rudii.txt') as f:
        for line in f:
            pairs.append(line.strip().split("|"))

    a = PairedReconstruction(pairs, pair_length, divider)

    with open('./results/carsonella_rudii.txt', 'w') as f:
        f.write(PairedReconstruction(pairs, pair_length, divider))    