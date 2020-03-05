from skew import Skew

def MinimumSkew(genome):
    result = []
    skews = Skew(genome)
    min_skew = skews[0] 

    for skew in skews:
        min_skew = min(min_skew, skew)

    for i in range(len(skews)):
        if skews[i] == min_skew:
            result.append(i)
    return result
    
if __name__ == "__main__":
    print(
        " ".join(map(str, MinimumSkew("GATACACTTCCCGAGTAGGTACTG")))
    )