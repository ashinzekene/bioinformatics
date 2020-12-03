def LCSBackTrack(v, w):
    lv = len(v)
    lw = len(w)
    s = [[0] * (lw+1) for i in range(lv+1) ] 
    backtrack = [[0] * (lw+1) for i in range(lv+1) ] 
    s[0][0] = 0
    backtrack[0][0] = 0
    for i in range(1, lw):
        s[0][i] = 0
        backtrack[0][i] = w[i-1]
    for i in range(1, lv):
        s[i][0] = 0
        backtrack[i][0] = v[i-1]
    for i in range(1, lv+1):
        for j in range(1, lw+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            s[i][j] = max(
                s[i][j-1], s[i-1][j], s[i-1][j-1] + match,
            )
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = "|"
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = "-"
            elif s[i][j] == s[i-1][j-1]+match:
                backtrack[i][j] = "+"
    return backtrack

if __name__ == "__main__":
    v = "AACCTTGG"
    w = "ACACTGTGA"
    print(LCSBackTrack(v, w))