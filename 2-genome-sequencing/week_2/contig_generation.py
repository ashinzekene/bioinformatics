import sys
import os
from collections import defaultdict

sys.path.append(os.path.abspath(".."))

from week_1.de_bruijn_kmers import DeBruijnKmers

def getIns(graph):
    ins = defaultdict(list)
    for kmer, outs in graph.items():
        for out in outs:
            ins[out].append(kmer)
    return ins

def isOneInOneOut(kmer, ins, outs):
    return len(ins[kmer]) == len(outs[kmer]) == 1

def ContigGeneration(kmers):
    result = []
    outs_graph = DeBruijnKmers(kmers)
    ins_graph = getIns(outs_graph)
    for kmer in list(outs_graph.keys()):
        outs = outs_graph[kmer]
        if not isOneInOneOut(kmer, ins_graph, outs_graph):
            contigs = [kmer] * len(outs)
            for i, out in enumerate(outs):
                current = out
                contigs[i] += current[-1]
                while isOneInOneOut(current, ins_graph, outs_graph):
                    current = outs_graph[current][0]
                    contigs[i] += current[-1]
            result += contigs

    return result


if __name__ == "__main__":
    kmers = []
    with open('./datasets/dataset_205_5.txt') as f:
        kmers = [kmer.strip() for kmer in f.readlines()]

    result = ContigGeneration(kmers)
    result.sort()

    with open('./results/contig_generation.txt', 'w') as f:
        f.write('\n'.join(result))
