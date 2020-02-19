from minimum_skew import MinimumSkew
from frequent_kmer_mismatch_with_reverse import FrequentKmerMismatchWithReverse
from compute_count import CountD

genome = ""
result_text = ""

with open('./test/Salmonella_enterica.txt') as f:
    skip_first = False
    i = 0
    for line in f.readlines():
        if not skip_first:
            skip_first = True
            continue
        genome += line.strip()

print("Reading complete...")

min_skews = MinimumSkew(genome)
result_text += "Skew Points \n{} \n".format(
    " ".join(list(map(str, min_skews)))
    )
print("Skew Points", min_skews)


t = 9
# d = 2
kmers = {}

for d in range(3):
    for skew in min_skews:
        oris = genome[skew-250: skew+250]
        possible_kmers = FrequentKmerMismatchWithReverse(oris, t, d)
        count = 1
        if len(possible_kmers) > 0:
            count = CountD(oris, possible_kmers[0], d)
            print("No of occurrences {}: kmer counts: {}".format(count, len(possible_kmers)))
        if count == 1 and len(possible_kmers) > 5:
            result_text += "\nToo many possible kmers with {} mismatch: Occurences: {}\n".format(d, len(possible_kmers))
            continue
        for kmer in possible_kmers:
            kmers[kmer] = 0
        result_text += "\nMax KMers at min skew point {} with {} mismatch:\n {} \nOccurences: {}\n".format(
            skew, d, possible_kmers, count
        )
        
print(list(kmers.keys()))

result_text += "\n\nKMers :\n {}".format(list(map(str, kmers.keys())))

with open('./test/Salmonella_enterica_result.txt', 'w') as f:
    f.write(result_text)
