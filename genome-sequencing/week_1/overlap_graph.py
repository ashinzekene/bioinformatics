from collections import defaultdict

def OverlapGraph(motifs):
    result_dict = defaultdict(list)
    for motif in motifs:
        suffix = motif[1:]
        for i in range(len(motifs)):
            if motif != motifs[i] and motifs[i].startswith(suffix):
                 result_dict[motif].append(motifs[i])
    return result_dict
    
if __name__ == "__main__":
    motifs = []
    with open('./datasets/dataset_198_10.txt') as f:
        motifs = f.read().strip().split()
    result = OverlapGraph(motifs)
    string_result = ""
    for k, v in result.items():
        string_result += "{} -> {}\n".format(k, ", ".join(v))

    with open('./results/overlap_graph.txt', 'w') as f:
        f.write(string_result)