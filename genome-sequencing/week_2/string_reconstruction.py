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

if __name__ == "__main__":
    motifs = []
    with open('./datasets/dataset_203_7.txt') as f:
        motifs = [motif.strip() for motif in f.readlines()[1:]]

    result = StringReconstruction(motifs)
    with open('./results/string_reconstruction.txt', 'w') as f:
        f.write(result)
    