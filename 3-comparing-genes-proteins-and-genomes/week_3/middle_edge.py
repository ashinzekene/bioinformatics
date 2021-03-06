from blosom_62 import Blosom_62

def GetScoreMatrix(v, w, indel):
    lv = len(v)
    lw = len(w)
    previous_matrix = [0] * (lv+1)
    current_matrix = [0] * (lv+1)
    for i in range(1, lv+1):
        current_matrix[i] = current_matrix[i-1] - indel

    for j in range(1, lw+1):
        previous_matrix = current_matrix.copy()
        current_matrix[0] = -indel * j
        for i in range(1, lv+1):
            v_val = v[i-1]
            w_val = w[j-1]

            insertion = previous_matrix[i] - indel
            deletion = current_matrix[i-1] - indel
            match_mismatch = previous_matrix[i-1] + Blosom_62[v_val][w_val]
            current_matrix[i] = max(insertion, deletion, match_mismatch)

    matrix = [[previous_matrix[i], current_matrix[i]] for i in range(lv+1)] 
    return matrix


def MiddleEdge(v, w, indel):
    lw = len(w)
    middle_col_index = lw//2

    from_source = GetScoreMatrix(v, w[0:middle_col_index+1], indel)
    from_sink = GetScoreMatrix(v, w[lw:middle_col_index-1:-1], indel)

    middle_column = [from_source[i][0] + from_sink[i][1] for i in range(len(v)+1)]
    next_column = [from_source[i][1] for i in range(len(from_source))]

    mid_index = middle_column.index(max(middle_column))

    insertion = next_column[mid_index]
    deletion = middle_column[mid_index + 1]
    match_mismatch = next_column[mid_index + 1]
    max_value = max(insertion, deletion, match_mismatch)

    if max_value == insertion:
        return (mid_index, middle_col_index), (mid_index, middle_col_index+1), "-"
    elif max_value == deletion:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index), "|"
    else:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index+1), "+"

    return "IMPOSSIBLE ;-)"


if __name__ == "__main__":
    v = "FPPF"
    w = "FFPF"
    indel = 5
    path = './datasets/dataset_250_12.txt'
    with open(path) as f:
        v = f.readline().strip()
        w = f.readline().strip()
    edge1, edge2, _ = MiddleEdge(v, w, indel)
    with open('./results/middle_edge.txt', 'w') as f:
        f.write(str(edge1) + " " + str(edge2))