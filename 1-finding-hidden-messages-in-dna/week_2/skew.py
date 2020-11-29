def Skew(genome):
    result = [0]
    skew_map = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    for char in genome:
        prev = result[-1]
        result.append(prev + skew_map[char])
    return result


if __name__ == "__main__":
    print(" ".join(map(str, Skew("GAGCCACCGCGATA"))))
