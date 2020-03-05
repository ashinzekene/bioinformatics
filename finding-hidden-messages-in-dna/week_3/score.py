nucleotide_index = {'A':0,'C':1,'G':2, 'T':3 }

def Score(motifs):
    result = 0
    for i in range(len(motifs[0])):
        scores = [0] * 4
        for motif in motifs:
            index = nucleotide_index[motif[i]]
            scores[index]+=1
        result += sum(scores) - max(scores)
            
    return result
    
if __name__ == "__main__":
    print(Score([
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC",
    ]))

