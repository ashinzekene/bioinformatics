import sys
import os

sys.path.append(os.path.abspath(".."))
from week_2.neighbors import Neighbors
from week_2.hamming_distance import HammingDistance

def MotifEnumeration(dnas, k, d):
    result = {}
    possible_kmers = {}
    for i in range(len(dnas[0]) - k +1):
        kmer = dnas[0][i:i+k]
        neighbors = Neighbors(kmer, d)
        for neighbor in neighbors:
            possible_kmers[neighbor] = 0

    for kmer in possible_kmers:
        counts = 0
        for dna in dnas[1:]:
            if IsPresent(dna, kmer, d):
                counts += 1
        if counts == len(dnas[1:]):
            result[kmer] = 0
            
    
    return list(result.keys())
        
def IsPresent(dna, pattern, d):
    for i in range(len(dna) - len(pattern) +1):
        kmer = dna[i:i+len(pattern)]
        diff = HammingDistance(kmer, pattern)
        if diff <= d:
            return True
    return False
    
    
dnas = [
    "ATTTGGC",
    "TGCCTTA",
    "CGGTATC",
    "GAAAATT"
]

result = MotifEnumeration(dnas, 3, 1)

print(" ".join(list(map(str, result))))