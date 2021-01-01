def FittingAlignment(a, b, ru):
    la = len(a)
    lb = len(b)

    scores_matrix = [[0] * (lb+1) for i in range(la+1)]
    backtrack = [[0] * (lb+1) for i in range(la+1)]
    for i in range(1, la+1):
        scores_matrix[i][0] = 0
        backtrack[i][0] = a[i-1]
    for j in range(1, lb+1):
        scores_matrix[0][j] = scores_matrix[0][j-1] - ru 
        backtrack[0][j] = b[j-1]

    for i in range(1, len(scores_matrix)):
        for j in range(1, len(scores_matrix[0])):
            symbol_a = a[i-1]
            symbol_b = b[j-1]
            match = -1
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
    for i in range(la+1):
        if scores_matrix[i][-1] > max_val:
            max_val = scores_matrix[i][-1]
            max_index = i


    result_a = ""
    result_b = ""
    i, j = max_index, lb
    while i > 0 and j > 0:
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
    a = "GTAGGCTTAAGGTTA"
    b = "TAGATA"
    ru = 1
    path = "./datasets/dataset_248_5.txt"
    with open(path) as f:
        a = f.readline().strip()
        b = f.readline().strip()

    max_alignment_score, string_a, string_b = FittingAlignment(a, b, ru)
    print(max_alignment_score, string_a, string_b)
    with open("./results/fitting_alignment.txt", "w") as f:
        f.write(str(max_alignment_score) + "\n")
        f.write(string_a + "\n")
        f.write(string_b + "\n")