from collections import defaultdict

def DeBruijnPairedKmers(pairs):
    kmer_map = defaultdict(list)
    for kmers in pairs:
        prefix = "{}|{}".format(kmers[0][:-1], kmers[1][:-1])
        suffix = "{}|{}".format(kmers[0][1:], kmers[1][1:])
        kmer_map[prefix].append(suffix)
    return kmer_map
    
if __name__ == "__main__":
    pair_length = 0
    divider = 0
    pairs = []
    with open("./datasets/reconstruction.txt") as f:
        params = f.readline().strip().split(" ")
        pair_length = int(params[0])
        divider = int(params[1])

        for line in f.readlines():
            pairs.append(line.strip().split("|"))

    result = DeBruijnPairedKmers(pairs)
    
    result_string = ""
    for k, v in result.items():
        result_string += "{} -> {}\n".format(k, ", ".join(v))

    print(result_string)
    with open('./results/de_bruijn_paired_kmers.txt', 'w') as f:
        f.write(result_string)
    