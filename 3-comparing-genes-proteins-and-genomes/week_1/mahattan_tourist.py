def MahattanTourist(n, m, down, right):
    dpMatrix = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        dpMatrix[i][0] = dpMatrix[i-1][0] + down[i-1][0]
    for i in range(1, m+1):
        dpMatrix[0][i] = dpMatrix[0][i-1] + right[0][i-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dpMatrix[i][j] = max(
                dpMatrix[i-1][j] + down[i-1][j],
                dpMatrix[i][j-1] + right[i][j-1]
            )
    return dpMatrix[n][m]

if __name__ == "__main__":
    n = 0
    m = 0
    down = []
    right = []
    with open('./datasets/dataset_261_10.txt') as f:
        a = [int(v) for v in f.readline().strip().split(' ')]
        n, m = a
        for i in range(n):
            row = f.readline().strip().split(' ')
            down.append([int(v) for v in row])
        assert f.readline().strip() == "-"
        for i in range(n+1):
            row = f.readline().strip().split(' ')
            right.append([int(v) for v in row])
    result = MahattanTourist(n, m, down, right)
    with open('./results/mahattan_tourist.txt', 'w') as f:
        f.write(str(result))