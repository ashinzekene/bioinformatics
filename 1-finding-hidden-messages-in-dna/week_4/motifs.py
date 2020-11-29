import sys
import os

sys.path.append(os.path.abspath("."))
from week_2.hamming_distance import HammingDistance

nucleotides = {'A':0, 'C':1, 'G':2, 'T':3}

def Motifs(profile, dnas):
    k = len(profile[0])
    result = []
    for dna in dnas:
        score = 0
        best_kmer = ""
        for i in range(len(dna) - k + 1):
            kmer = dna[i:i+k]
            kmer_score = KmerScore(kmer, profile)
            if kmer_score > score:
                score = kmer_score
                best_kmer = kmer
        result.append(best_kmer)

    return result


def KmerScore(kmer, profile):
    score = 0
    for i, nucleotide in enumerate(kmer):
        nucleotide_index = nucleotides[nucleotide]
        val = profile[nucleotide_index][i]
        score += val
    return score
    
    

if __name__ == "__main__":
    dnas = [
        "TTACCTTAAC",
        "GATGTCTGTC",
        "ACGGCGTTAG",
        "CCCTAACGAG",
        "CGTCAGAGGT",
    ]
    profile = {
        "A": [0.8, 0, 0, 0.2],
        "C": [0, 0.6, 0.2, 0],
        "G": [0.2, 0.2, 0.8, 0],
        "T": [0, 0.2, 0, 0.8],
    }
    print(Motifs(profile, dnas))