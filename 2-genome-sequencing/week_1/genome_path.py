def GenomePath(motifs):
    result = motifs[0]
    for i in range(1, len(motifs)):
        result += motifs[i][-1]

    return result


if __name__ == "__main__":
    motifs = []
    with open('./datasets/dataset_198_3.txt') as f:
        for motif in f:
            motifs.append(motif.strip())

    with open('./results/genome-path.txt', 'w') as f:
        f.write(GenomePath(motifs))
