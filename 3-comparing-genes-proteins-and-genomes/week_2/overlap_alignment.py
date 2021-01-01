def OverlapAlignment(a, b, ru):
    la = len(a)
    lb = len(b)

    scores_matrix = [[0] * (lb+1) for i in range(la+1)]
    backtrack = [[0] * (lb+1) for i in range(la+1)]
    for i in range(1, la+1):
        scores_matrix[i][0] = 0
        backtrack[i][0] = a[i-1]
    for j in range(1, lb+1):
        scores_matrix[0][j] = 0
        backtrack[0][j] = b[j-1]

    for i in range(1, len(scores_matrix)):
        for j in range(1, len(scores_matrix[0])):
            symbol_a = a[i-1]
            symbol_b = b[j-1]
            match = -2
            if symbol_a == symbol_b:
                match = 1
            insertion = scores_matrix[i-1][j] - ru
            deletion = scores_matrix[i][j-1] - ru
            match_mismatch = scores_matrix[i-1][j-1] + match

            scores_matrix[i][j] = max(insertion, deletion, match_mismatch)

            if scores_matrix[i][j] == insertion:
                backtrack[i][j] = "|"
            elif scores_matrix[i][j] == deletion:
                backtrack[i][j] = "-"
            elif scores_matrix[i][j] == match_mismatch:
                backtrack[i][j] = "+"

    max_val = scores_matrix[0][-1]
    max_index = 0
    for j in range(lb+1):
        if scores_matrix[-1][j] >= max_val:
            max_val = scores_matrix[-1][j]
            max_index = j


    result_a = ""
    result_b = ""
    i, j = la, max_index
    while i > 0 and j > 0:
        if backtrack[i][j] == "0":
            return max_val, result_a, result_b
        if backtrack[i][j] == "+":
            result_a = a[i-1] + result_a 
            result_b = b[j-1] + result_b
            i-=1
            j-=1
        elif backtrack[i][j] == "|":
            result_a = a[i-1] + result_a
            result_b = "-" + result_b
            i-=1
        elif backtrack[i][j] == "-":
            result_a = "-" + result_a
            result_b = b[j-1] + result_b
            j-=1

    return max_val, result_a, result_b


if __name__ == "__main__":
    a = "PAWHEAE"
    b = "HEAGAWGHEE"
    ru = 2
    path = "./datasets/dataset_248_7.txt"
    with open(path) as f:
        a = f.readline().strip()
        b = f.readline().strip()

    max_alignment_score, string_a, string_b = OverlapAlignment(a, b, ru)
    print(max_alignment_score, string_a, string_b)
    with open("./results/overlap_alignment.txt", "w") as f:
        f.write(str(max_alignment_score) + "\n")
        f.write(string_a + "\n")
        f.write(string_b + "\n")