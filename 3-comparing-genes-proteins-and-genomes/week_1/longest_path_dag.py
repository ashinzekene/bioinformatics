from collections import defaultdict, OrderedDict

def LongestPathDAG(out_graph: dict, in_graph: dict, start: int, end: int):
    max_values = defaultdict(int)
    queue = []

    # remove nodes without in degrees recursively
    in_degreeless = []
    for node in in_graph.keys():
        if node not in out_graph and node != start:
            in_degreeless.append(node)
    while len(in_degreeless):
        node = in_degreeless.pop(0)
        if node not in in_graph:
            continue
        node_outs = list(in_graph[node].keys())
        in_graph.pop(node)
        for out in node_outs:
            # if no other node is coming in remove it
            if len(out_graph[out]) == 1:
                in_degreeless.append(out)
            # remove this node
            out_graph[out].pop(node)


    # topological sort
    topological_ordering = []
    in_degrees = defaultdict(int)
    for node in in_graph.keys():
        in_degrees[node] = 0
    for node, in_nodes in out_graph.items():
        in_degrees[node] = len(in_nodes.keys())

    topological_sort_queue = []
    for node, in_degree in in_degrees.items():
        if in_degree == 0:
            topological_sort_queue.append(node)
    while len(topological_sort_queue):
        node = topological_sort_queue.pop(0)
        topological_ordering.append(node)
        if node not in in_graph:
            continue
        for out in in_graph[node].keys():
            in_degrees[out] -= 1
            if in_degrees[out] == 0:
                topological_sort_queue.append(out)


    # get max values of each node
    for node in topological_ordering:
        max_value = 0
        for out, weight in out_graph[node].items():
            max_value = max(
                max_values[out] + weight, max_value
            )
        max_values[node] = max_value


    # backtracking: get path from end to start
    current_out = end
    while current_out != start:
        queue.append(current_out)
        out_weights = out_graph[current_out]
        max_out, max_weight = 0, 0
        for out, weight in out_weights.items():
            if max_values[out] + weight > max_weight:
                max_weight = max_values[out] + weight
                max_out = out
            current_out = max_out
    queue.append(start)
    queue.reverse()
    return max_values[end], queue 
    


path = './datasets./dataset_245_7.txt'

if __name__ == "__main__":
    with open(path) as f:
        start = int(f.readline())
        end = int(f.readline())

        in_graph = OrderedDict()
        out_graph = defaultdict(dict)
        for line in f:
            in_, right = line.split('->')
            out, weight = right.split(':')

            in_ = int(in_)
            out = int(out)
            weight = int(weight)

            if in_ in in_graph:
                in_graph[in_][out] = weight
            else:
                in_graph[in_] = { out: weight}

            out_graph[out][in_] = weight

    max_value, ordering = LongestPathDAG(out_graph, in_graph, start, end)
    with open('./results/longest_path_dag.txt', 'w') as f:
        f.write(str(max_value) + "\n")
        f.write("->".join(map(str, ordering)))