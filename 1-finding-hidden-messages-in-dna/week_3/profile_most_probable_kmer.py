import sys
import os
import random

sys.path.append(os.path.abspath(".."))

from week_3.profile_matrix import ProfileMatrix

def ProfileMostProbableKMer(profile, k, dna):
    max_profile_matrix = -1
    kmer_result = ""
    for i in range(len(dna) - k + 1):
        motif = dna[i:i+k]
        profile_mat = ProfileMatrix(profile, motif)
        if profile_mat > max_profile_matrix:
            max_profile_matrix = profile_mat
            kmer_result = motif

    return kmer_result



if __name__ == "__main__":
    A = [
        [0.2, 0.2, 0.3, 0.2, 0.3],
        [0.4, 0.3, 0.1, 0.5, 0.1],
        [0.3, 0.3, 0.5, 0.2, 0.4],
        [0.1, 0.2, 0.1, 0.1, 0.2],
    ]
    print(ProfileMostProbableKMer(
        A,
        5,
        "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    ))