import sys
sys.path.append('/Users/ashinzekene/code/personal-projects/bioinformatics/')

from neighbors import Neighbors

from week_1.compliment import Compliment

def FrequentKmerMismatchWithReverse(genome, k, d):
    result = []
    kmers = {}
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i+k]
        mismatches = Neighbors(pattern, d)
        mismatches.extend(Neighbors(Compliment(pattern), d))
        for mismatch in mismatches:
            if kmers.get(mismatch) == None:
                kmers[mismatch] = 1
            else:
                kmers[mismatch] += 1

    max_kmer_count = 0
    for count in kmers.values():
        max_kmer_count = max(max_kmer_count, count)

    # print(max_kmer_count, kmers)
    for kmer, count in kmers.items():
        if count == max_kmer_count:
            result.append(kmer)

    return result

if __name__ == "__main__":
    print(FrequentKmerMismatchWithReverse(
        "AACTCTACCTACGACTAACTAAGACTGAACGAAAAAGAACTGAACAAACACCTACCTAAAACTAAACAAAAGAAGAAGAAACTGAGAAGAAGAAGAAAAGAACTAAACGAGAACGAAAACACGAAACGAGAACAAAAGACTCTGAAGAAACACACGAAACCTACCTGAGAGAAACGAAAGAAAAGAACGAACTAAGAGAAAGAAAAGAAACTCTGAACACACGAAACT",
        6,
        2
    ))