def EditDistance(a, b):
    la = len(a)
    lb = len(b)
    matrix = [[0] * (lb+1) for i in range(la+1)]
    for i in range(1, la+1):
        matrix[i][0] = i
    for j in range(1, lb+1):
        matrix[0][j] = j

    for i in range(1, la+1):
        for j in range(1, lb+1):
            str_a = a[i-1]
            str_b = b[j-1]
            match = 1
            if str_a == str_b:
                match = 0
            matrix[i][j] = min(
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + match
            )
    return matrix[-1][-1]


if __name__ == "__main__":
    a = "PLEASANTLY"
    b = "MEANLY"
    with open("./datasets/dataset_248_3.txt") as f:
        a = f.readline().strip()
        b = f.readline().strip()

    with open("./results/edit_distance.txt", "w") as f:
        f.write(str(EditDistance(a, b)))

