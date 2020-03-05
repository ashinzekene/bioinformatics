import sys
import os

sys.path.append(os.path.abspath("."))

from week_2.hamming_distance import HammingDistance
from week_3.profile_matrix import ProfileMatrix
from week_4.random_number import RandomNumber

def ProfileRandomlyGeneratedKmer(profile, k, dna):
    probablilites = []
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        probablilites.append(ProfileMatrix(profile, kmer))
    index = RandomNumber(probablilites)
    return dna[index: index+k]
