import math

def entropy(motifs):
    motif_count = len(motifs)
    scores = []
    entropy = 0
    for i in range(len(motifs[0])):
        score = {'A':0,'G':0,'T':0, 'C':0 }
        for motif in motifs:
            score[motif[i]]+=1
        scores.append(score)

    for score in scores:
        for count in score.values():
            prob = count/motif_count
            if prob != 0:
                a = prob * math.log(prob, 2)
                entropy += abs(a)

    return entropy

def EntropyFromProfile(profile):
    result = 0
    for prob in profile:
        if prob != 0:
            a = prob * math.log(prob, 2)
            result += abs(a)
    return result
    

if __name__ == "__main__":
    Motifs = [
        "TCGGGGGTTTTT",
        "CCGGTGACTTAC",
        "ACGGGGATTTTC",
        "TTGGGGACTTTT",
        "AAGGGGACTTCC",
        "TTGGGGACTTCC",
        "TCGGGGATTCAT",
        "TCGGGGATTCCT",
        "TAGGGGAACTAC",
        "TCGGGTATAACC"
    ]
    profile = [
        [0.5, 0, 0, 0.5],
        [0.25, 0.25, 0.25, 0.25],
        [0, 0, 0, 1],
        [0.25, 0, 0.5, 0.25],
    ]
    print("\n".join(list(map(str, map(EntropyFromProfile, profile)))))

    # print(entropy(Motifs))