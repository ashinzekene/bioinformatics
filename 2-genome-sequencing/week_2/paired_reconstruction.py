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
    return PairedGenomePath(path, n, d)

if __name__ == "__main__":
    pair_length = 0
    divider = 0
    pairs = []
    
    # with open('./datasets/dataset_204_16.txt') as f:
    #     params = f.readline().strip().split(" ")
    pair_length = 3
    divider = 1
    v = [
        "ACC|ATA",
        "ACT|ATT",
        "ATA|TGA",
        "ATT|TGA",
        "CAC|GAT",
        "CCG|TAC",
        "CGA|ACT",
        "CTG|AGC",
        "CTG|TTC",
        "GAA|CTT",
        "GAT|CTG",
        "GAT|CTG",
        "TAC|GAT",
        "TCT|AAG",
        "TGA|GCT",
        "TGA|TCT",
        "TTC|GAA",
    ]
    for line in v:
        pairs.append(line.strip().split("|"))

    a = PairedReconstruction(pairs, pair_length, divider)
    print(a)
    # with open('./results/paired_reconstruction.txt', 'w') as f:
    #     f.write(PairedReconstruction(pairs, pair_length, divider))