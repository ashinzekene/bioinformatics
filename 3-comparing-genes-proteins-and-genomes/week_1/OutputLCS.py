from LCSBackTrack import LCSBackTrack

def OutputLCS(backtrack, v, i, j):
    lcs = ""
    while i > 0 and j > 0:
        if i == 0 or j == 0:
            return ""
        if backtrack[i][j] == "|":
            i -= 1
        elif backtrack[i][j] == "-":
            j -= 1
        else:
            lcs = v[i-1] + lcs
            j -= 1
            i -= 1
    return lcs

if __name__ == "__main__":
    v = "AACCTTGG"
    w = "ACACTGTGA"
    # with open("./datasets/dataset_245_5.txt") as f:
    #     v = f.readline().strip()
    #     w = f.readline().strip()

    backtrack = LCSBackTrack(v, w)
    lcs = OutputLCS(backtrack, v, len(v), len(w))
    print(lcs)
    # with open("./results/OutputLCS.txt", "w") as f:
    #     f.write(lcs)