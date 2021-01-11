from blosom_62 import Blosom_62

def GetScoreMatrix(v, w, indel):
    lv = len(v)
    lw = len(w)
    scores_matrix = [[0] * (lw+1) for i in range(lv+1)]

    for i in range(1, lv+1):
        scores_matrix[i][0] = scores_matrix[i][0] - indel

    for j in range(1, lw+1):
        scores_matrix[0][j] = scores_matrix[0][j] - indel

    for i in range(1, lv+1):
        for j in range(1, lw+1):
            v_val = v[i-1]
            w_val = w[j-1]

            insertion = scores_matrix[i-1][j] - indel
            deletion = scores_matrix[i][j-1] - indel
            match_mismatch = scores_matrix[i-1][j-1] + Blosom_62[v_val][w_val]
            scores_matrix[i][j] = max(insertion, deletion, match_mismatch)

    matrix = [scores_matrix[i][-2:] for i in range(lv+1)] 
    return matrix

def GetMiddleNode(middle_column):
    mid_val, mid_index = middle_column[0], 0
    for i, val in enumerate(middle_column):
        if val > mid_val:
            mid_val = val
            mid_index = i
    return mid_index


def MiddleEdge(v, w, indel):
    lw = len(w)
    middle_col_index = lw//2

    from_source = GetScoreMatrix(v, w[0:middle_col_index+1], indel)
    from_sink = GetScoreMatrix(v, w[lw:middle_col_index-2:-1], indel)

    middle_column = [from_source[i][0] + from_sink[i][1] for i in range(len(v)+1)]
    next_column = [from_source[i][1] + from_sink[i][1] for i in range(len(v)+1)]

    mid_index = GetMiddleNode(middle_column)

    insertion = next_column[mid_index]
    deletion = middle_column[mid_index + 1]
    match_mismatch = next_column[mid_index + 1]
    max_value = max(insertion, deletion, match_mismatch)

    if max_value == insertion:
        return (mid_index, middle_col_index), (mid_index, middle_col_index+1)
    elif max_value == deletion:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index)
    else:
        return (mid_index, middle_col_index), (mid_index+1, middle_col_index+1)

    return "IMPOSSIBLE ;-)"


if __name__ == "__main__":
    v = "PLEASANTLY"
    w = "MEASNLY"
    indel = 5
    path = './datasets/dataset_250_12.txt'
    with open(path) as f:
        v = f.readline().strip()
        w = f.readline().strip()
    edge1, edge2 = MiddleEdge(v, w, indel)
    with open('./results/midle_edge.txt', 'w') as f:
        f.write(str(edge1) + " " + str(edge2))