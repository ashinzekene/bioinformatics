from math import inf
from blosom_62 import Blosom_62


def AffineGapPenalties(v, w, go, ge):
    lv = len(v)
    lw = len(w)
    lower_scores_matrix = [[0] * (lw+1) for i in range(lv+1)]
    middle_scores_matrix = [[0] * (lw+1) for i in range(lv+1)]
    upper_scores_matrix = [[0] * (lw+1) for i in range(lv+1)]

    lower_backtrack_matrix = [[0] * (lw+1) for i in range(lv+1)]
    middle_backtrack_matrix = [[0] * (lw+1) for i in range(lv+1)]
    upper_backtrack_matrix = [[0] * (lw+1) for i in range(lv+1)]

    for i in range(1, lv+1):
        upper_scores_matrix[i][0] = -inf
        middle_scores_matrix[i][0] = -go - (ge * (i - 1))
        lower_scores_matrix[i][0] = -go - (ge * (i - 1))

        upper_backtrack_matrix[i][0] = v[i-1]
        middle_backtrack_matrix[i][0] = v[i-1]
        lower_backtrack_matrix[i][0] = v[i-1]

    for j in range(1, lw+1):
        upper_scores_matrix[0][j] = -go - (ge * (j - 1))
        middle_scores_matrix[0][j] = -go - (ge * (j - 1))
        lower_scores_matrix[0][j] = -inf

        upper_backtrack_matrix[0][j] = w[j-1]
        middle_backtrack_matrix[0][j] = w[j-1]
        lower_backtrack_matrix[0][j] = w[j-1]
    
    for i in range(1, lv+1):
        for j in range(1, lw+1):
            v_val = v[i-1]
            w_val = w[j-1]
            score = Blosom_62[v_val][w_val]

            lower_im1_j = lower_scores_matrix[i-1][j]
            middle_im1_j = middle_scores_matrix[i-1][j]
            upper_i_jm1 = upper_scores_matrix[i][j-1]
            middle_i_jm1 = middle_scores_matrix[i][j-1]
            middle_im1_jm1 = middle_scores_matrix[i-1][j-1]

            lower_scores_matrix[i][j] = max(lower_im1_j - ge, middle_im1_j - go)
            lower_backtrack_matrix[i][j] = "-"
            if lower_scores_matrix[i][j] == middle_im1_j - go:
                lower_backtrack_matrix[i][j] = "M"

            upper_scores_matrix[i][j] = max(upper_i_jm1 - ge, middle_i_jm1 - go)
            upper_backtrack_matrix[i][j] = "|"
            if upper_scores_matrix[i][j] == middle_i_jm1 - go:
                upper_backtrack_matrix[i][j] = "M"

            middle_scores_matrix[i][j] = max(
                upper_scores_matrix[i][j], middle_im1_jm1 + score, lower_scores_matrix[i][j],
            )
            middle_backtrack_matrix[i][j] = "+"
            if middle_scores_matrix[i][j] == upper_scores_matrix[i][j]:
                middle_backtrack_matrix[i][j] = "U"
            elif middle_scores_matrix[i][j] == lower_scores_matrix[i][j]:
                middle_backtrack_matrix[i][j] = "L"

    score = middle_scores_matrix[i][j]
    i, j = lv, lw
    v_result, w_result = "", ""
    current_backtrack_matrix = middle_backtrack_matrix
    current_matrix_type = "M"
    # L, M, U, +, -, |
    while i > 0 and j > 0:
        direction = current_backtrack_matrix[i][j]
        if direction == "+":
            v_result = v[i-1] + v_result
            w_result = w[j-1] + w_result
            i -= 1
            j -= 1
        elif direction == "-":
            v_result = v[i-1] + v_result
            w_result = "-" + w_result
            i -= 1
        elif direction == "|":
            v_result = "-" + v_result
            w_result = w[j-1] + w_result
            j -= 1
        elif direction == "L":
            current_matrix_type = "L"
            current_backtrack_matrix = lower_backtrack_matrix
        elif direction == "U":
            current_matrix_type = "U"
            current_backtrack_matrix = upper_backtrack_matrix
        elif direction == "M":
            if current_matrix_type == "U":
                v_result = "-" + v_result
                w_result = w[j-1] + w_result
                j -= 1
            else:
                v_result = v[i-1] + v_result
                w_result = "-" + w_result
                i -= 1
            current_backtrack_matrix = middle_backtrack_matrix
            current_matrix_type = "M"
    return score, v_result, w_result


if __name__ == "__main__":
    v = "PRTEINS"
    w = "PRTWPSEIN"
    go = 11
    ge = 1
    path = "./datasets/dataset_249_8.txt"
    with open(path) as f:
        v = f.readline().strip()
        w = f.readline().strip()

    max_alignment_score, string_v, string_w = AffineGapPenalties(v, w, go, ge)
    print(max_alignment_score, string_v, string_w)
    with open("./results/affine_gap_penalties.txt", "w") as f:
        f.write(str(max_alignment_score) + "\n")
        f.write(string_v + "\n")
        f.write(string_w + "\n")