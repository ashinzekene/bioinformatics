nucleotides = ['A', 'C', 'T', 'G']

def Neighbors(pattern, d):
    result = {}
    def Neighbors(pattern, d, result):
        result[pattern] = 0
        if d == 0:
            return
        for i in range(len(pattern)):
            for n in nucleotides:
                if n != pattern[i]:
                    mismatch = pattern[:i] + n +pattern[i+1:]
                    Neighbors(mismatch, d-1, result)

    Neighbors(pattern, d, result)
    return list(result.keys())


if __name__ == "__main__":
    text = "\n".join(map(str, Neighbors(
        "ACGGCTCTAGTG",
        3
    )))
    with open('test.txt', 'w') as f:
        f.write(text)
    print('Done...')

    