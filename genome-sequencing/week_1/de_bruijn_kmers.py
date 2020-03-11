from collections import defaultdict

def DeBruijnKmers(kmers):
    kmer_map = defaultdict(list)
    for kmer in kmers:
        kmer_map[kmer[:-1]].append(kmer[1:])
    return kmer_map
    
if __name__ == "__main__":
    kmers = []
    with open("./datasets/dataset_200_8.txt") as f:
        kmers = list(map(lambda x: x.strip(), f.readlines()))
    result = DeBruijnKmers(kmers)
    
    result_string = ""
    for k, v in result.items():
        result_string += "{} -> {}\n".format(k, ", ".join(v))

    with open('./results/de_bruijn_kmers.txt', 'w') as f:
        f.write(result_string)
    