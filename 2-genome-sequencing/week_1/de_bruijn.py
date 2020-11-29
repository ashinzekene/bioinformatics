from collections import defaultdict

def DeBruijn(dna, k):
    k-=1
    kmer_map = defaultdict(list)
    for i in range(1, len(dna)-k+1):
        prev = dna[i-1:i+k-1]
        current = dna[i:i+k]
        kmer_map[prev].append(current)
    return kmer_map
    
if __name__ == "__main__":
    k = 0
    dna = ""
    with open("./datasets/dataset_199_6.txt") as f:
        k = int(f.readline())
        dna = f.readline().strip()
    result = DeBruijn(dna, k)
    
    result_string = ""
    for k, v in result.items():
        result_string += "{} -> {}\n".format(k, ", ".join(v))

    with open('./results/de_bruijn.txt', 'w') as f:
        f.write(result_string)
    