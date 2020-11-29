from collections import defaultdict

def getIns(graph):
    ins = defaultdict(list)
    for kmer, outs in graph.items():
        for out in outs:
            ins[out].append(kmer)
    return ins

def isOneInOneOut(kmer, ins, outs):
    return len(ins[kmer]) == len(outs[kmer]) == 1

def MaximalNonBranchingPaths(outs_graph):
    result = []
    ins_graph = getIns(outs_graph)
    completed = {}
    for kmer in list(outs_graph.keys()):
        completed[kmer] = False
        outs = outs_graph[kmer]
        if not isOneInOneOut(kmer, ins_graph, outs_graph):
            completed[kmer] = True
            contigs = [[kmer] for i in outs]
            for i, out in enumerate(outs):
                completed[kmer] = True
                current = out
                contigs[i].append(current)
                while isOneInOneOut(current, ins_graph, outs_graph):
                    completed[kmer] = True
                    current = outs_graph[current][0]
                    contigs[i].append(current)
            result += contigs

    isolated_cycles = []
    for kmer in list(outs_graph.keys()):
        cycle = []
        current_kmer = kmer
        if kmer not in completed or completed[kmer]:
            continue
        while isOneInOneOut(current_kmer, ins_graph, outs_graph):
            cycle.append(current_kmer)
            current_kmer = outs_graph[current_kmer][0]
            completed[current_kmer] = True
            if current_kmer == kmer:
                cycle.append(kmer)
                isolated_cycles.append(cycle)
                break

    return result + isolated_cycles

if __name__ == "__main__":
    file_name = 'sample'
    outs_graph = defaultdict(list)
    with open('./datasets/dataset_6207_2.txt') as f:
        for line in f:
            kmer, outs = line.split('->')
            for out in outs.strip().split(','):
                outs_graph[kmer.strip()].append(out.strip())
    results = MaximalNonBranchingPaths(outs_graph)
    with open('./results/maximum_non_branching_path.txt', 'w') as f:
        for result in results:
            f.write(" -> ".join(result))
            f.write('\n')
