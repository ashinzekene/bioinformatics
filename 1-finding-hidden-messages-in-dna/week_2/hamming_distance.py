def HammingDistance(genome1, genome2):
    distance = 0
    for i in range(len(genome1)):
        if genome1[i] != genome2[i]:
            distance+=1
    return distance
    
if __name__ == "__main__":
    print(HammingDistance(
        "GGGCCGTTGGT",
        "GGACCGTTGAC"
    ))