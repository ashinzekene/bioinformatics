from neighbors import Neighbors

def FrequentKmerMismatch(genome, k, d):
    result = []
    kmers = {}
    for i in range(len(genome) - k + 1):
        pattern = genome[i:i+k]
        mismatches = Neighbors(pattern, d)
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
    cases = [
        {
            "genome":   "ACGTTGCATGTCGCATGATGCATGAGAGCT",
            "k": 4,
            "d": 1,
            "expected": "ATGC ATGT GATG",
        },
        {
            "genome":   "AAAAAAAAAA",
            "k": 2,
            "d": 1,
            "expected": "AA AC AG CA AT GA TA",
        },
        {
            "genome":   "AGTCAGTC",
            "k": 4,
            "d": 2,
            "expected": "TCTC CGGC AAGC TGTG GGCC AGGT ATCC ACTG ACAC AGAG ATTA TGAC AATT CGTT GTTC GGTA AGCA CATC",
        },
        {
            "genome":   "AATTAATTGGTAGGTAGGTA",
            "k": 4,
            "d": 0,
            "expected": "GGTA",
        },
        {
            "genome":   "ATA",
            "k": 3,
            "d": 1,
            "expected": "GTA ACA AAA ATC ATA AGA ATT CTA TTA ATG",
        },
        {
            "genome":   "AAT",
            "k": 3,
            "d": 0,
            "expected": "AAT",
        },
        {
            "genome":   "TAGCG",
            "k": 2,
            "d": 1,
            "expected": "GG TG",
        }
    ]
    # for case in cases:
    #     print(case['expected'], " ---- ", " ".join(map(str,
    #         FrequentKmerMismatch(
    #             case['genome'],
    #             case['k'],
    #             case['d']
    #         )
    #     )), "\n")