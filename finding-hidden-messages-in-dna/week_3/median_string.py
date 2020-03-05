from distance import PatternDNAsDistance
from kmers import Kmers

def MedianString(dnas, k):
    distance = len(dnas) * k
    kmer_result = ''
    for kmer in Kmers(k):
        d = PatternDNAsDistance(kmer, dnas)
        if d < distance:
            distance = d
            kmer_result = kmer 

    return kmer_result
            


if __name__ == "__main__":
    print(MedianString([
        "CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
        "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
        "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG",
    ], 7))