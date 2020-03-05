from hamming_distance import HammingDistance

def ApproximatePatternMatch(genome, pattern, d):
    result = []
    for i in range(len(genome) - len(pattern) + 1):
        if HammingDistance(genome[i:i+len(pattern)], pattern) <= d:
            result.append(i)
    return result
    
    
if __name__ == "__main__":
    result = ApproximatePatternMatch(
            "CGTGACAGTGTATGGGCATCTTT",
            "TGT",
            1
        )
    print(
        " ".join(map(str, result))
    )